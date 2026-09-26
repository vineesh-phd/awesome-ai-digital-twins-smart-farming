"""Check this collection's links, resource counts, generated files, and example."""
import json
import math
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build_catalog import outputs

ROOT = Path(__file__).resolve().parents[1]


def prose(text):
    return re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M | re.S)


def links(text):
    # All curated pages use inline Markdown links with unspaced destinations.
    return re.findall(r'\[[^\]\n]*\]\(([^\s]+?)\)', prose(text))


def anchors(text):
    result, seen = set(), {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', prose(text), flags=re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        number = seen.get(slug, 0)
        seen[slug] = number + 1
        result.add(slug + (f'-{number}' if number else ''))
    return result


def validate(root):
    errors, local_count = [], 0
    for path in root.rglob('*.md'):
        if any(part in {'.git', '.venv', 'tmp'} for part in path.relative_to(root).parts):
            continue
        for link in links(path.read_text()):
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            local_count += 1
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not target.is_relative_to(root.resolve()) or not target.exists():
                errors.append(f'{path.relative_to(root)}: missing or outside-root target {link}')
            elif parsed.fragment and target.suffix == '.md':
                if unquote(parsed.fragment) not in anchors(target.read_text()):
                    errors.append(f'{path.relative_to(root)}: missing heading {link}')
    data = json.loads((root / 'references/references.json').read_text())
    papers = data['papers']
    if [p['id'] for p in papers] != [f'R{i:02d}' for i in range(1, 26)]:
        errors.append('Reference IDs must be unique and ordered R01-R25.')
    published = sum(p['kind'] == 'published-paper' for p in papers)
    if published != 23:
        errors.append(f'Published-paper count changed: expected 23, found {published}. Update all count claims.')
    for index, paper in enumerate(papers, 1):
        for field in ('title', 'authors', 'year', 'venue', 'url', 'relevance', 'limitation', 'verification'):
            if not paper.get(field):
                errors.append(f'{paper["id"]}: missing {field}')
        expected = index if index <= 20 else None
        if paper.get('manuscript_reference') != expected:
            errors.append(f'{paper["id"]}: incorrect manuscript mapping')
        if paper['category'] not in data['categories']:
            errors.append(f'{paper["id"]}: unknown category')
    counts = {}
    for prefix, file, expected in [
        ('D', 'datasets/datasets.md', 5), ('T', 'tools/tools.md', 7),
        ('I', 'implementations/github-repositories.md', 5),
        ('L', 'tutorials/learning-resources.md', 7),
    ]:
        ids = re.findall(r'^## (' + prefix + r'\d{2})\b', (root / file).read_text(), re.M)
        counts[prefix] = len(ids)
        if ids != [f'{prefix}{i:02d}' for i in range(1, expected + 1)]:
            errors.append(f'{file}: expected consecutive unique IDs for {expected} resources')
    for name, body in outputs(data).items():
        if (root / name).read_text() != body:
            errors.append(f'{name}: stale generated catalogue')
    for name in ('paper/AI_Assisted_Research_Paper.pdf', 'citation-audit/Citation_Integrity_Audit.pdf'):
        path = root / name
        if not path.exists() or not path.read_bytes().startswith(b'%PDF-'):
            errors.append(f'{name}: missing or invalid PDF header')
    if 'unlicensed' not in (root / 'LICENSE').read_text().lower():
        errors.append('Unlicensed status notice was changed; review owner instruction.')
    taw = 1000 * .4 * (.30 - .15)
    depletion = 1000 * .4 * (.30 - .24)
    net = depletion + 6 - 12
    actual = (taw, .5 * taw, depletion, net, net / .9, net / .9 / 1000 * 10000, 1000 * .4 * .02)
    if not all(math.isclose(a, b) for a, b in zip(actual, (60, 30, 24, 18, 20, 200, 8))):
        errors.append('Illustrative irrigation arithmetic failed.')
    return errors, local_count, published, counts


if __name__ == '__main__':
    errors, local_count, published, counts = validate(ROOT)
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {local_count} local links; {published} published papers; resources {counts}.')
    print('PASS: catalogue consistency, manuscript mapping, PDF headers, unlicensed notice, irrigation arithmetic.')
    print('Not checked: scientific truth, full-text human review, external URLs, PDF layout, or field performance.')
