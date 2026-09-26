"""Record HTTP reachability without treating access restrictions as broken links."""
import json
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from check_repository import ROOT, links


def collect_urls():
    urls = set()
    for path in ROOT.rglob('*.md'):
        parts = path.relative_to(ROOT).parts
        if any(p in {'.git', '.venv', 'tmp', 'archive'} for p in parts) or path.name == 'link-check.md':
            continue
        urls.update(url for url in links(path.read_text()) if url.startswith(('https://', 'http://')))
    data = json.loads((ROOT / 'references/references.json').read_text())
    for p in data['papers']:
        urls.update((p['url'], p['verification']['metadata_source'], p['verification']['primary_source']))
    return sorted(urls)


def check(url):
    result = {'url': url, 'status': 'inconclusive', 'http': None, 'detail': ''}
    for method in ('HEAD', 'GET'):
        try:
            request = Request(url, method=method, headers={'User-Agent': 'ResearchRepositoryLinkCheck/1.0'})
            with urlopen(request, timeout=15) as response:
                result.update(status='reachable', http=response.status, detail=f'{method}; final URL: {response.url}')
            break
        except HTTPError as error:
            result.update(http=error.code, detail=f'{method}: {error.reason}')
            if method == 'HEAD':
                continue
            result['status'] = 'not-found' if error.code in (404, 410) else 'inconclusive'
        except (URLError, TimeoutError, OSError) as error:
            result['detail'] = str(error.reason if isinstance(error, URLError) else error)
            break
    return result


def main():
    urls = collect_urls()
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(check, urls))
    timestamp = datetime.now(timezone.utc).isoformat(timespec='seconds')
    counts = Counter(r['status'] for r in results)
    payload = {'checked_at_utc': timestamp, 'method': 'HEAD, then GET on HTTP error; response bodies not downloaded', 'results': results}
    (ROOT / 'references/link-check.json').write_text(json.dumps(payload, indent=2) + '\n')
    rows = ['# External Link Check', '', '[Back to collection](../README.md)', '',
            f'Checked at **{timestamp}**. {len(results)} unique active-collection URLs: ' + ', '.join(f'{n} {s}' for s, n in sorted(counts.items())) + '.', '',
            'HEAD requests were followed by GET on HTTP errors; response bodies were not downloaded. This is a reachability check, not a content, metadata, or scientific-validity check. A 200 response can still be a login or challenge page. HTTP 401/403/429, server errors, and network failures remain inconclusive, not proof of a broken citation. The historical archive is excluded.', '',
            'Run `python3 scripts/check_links.py` to refresh this time-specific report. Full response details are in [link-check.json](link-check.json). Literature verification dates in the bibliography are separate from this HTTP check.', '',
            '| URL | Result | HTTP |', '| --- | --- | --- |']
    rows.extend(f'| [Source]({r["url"]}) | {r["status"]} | {r["http"] or "network error"} |' for r in results)
    (ROOT / 'references/link-check.md').write_text('\n'.join(rows) + '\n')
    print(f'{len(results)} URLs: {dict(counts)}')
    for r in results:
        if r['status'] == 'not-found':
            print('NOT FOUND:', r['url'])
    return 1 if counts['not-found'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
