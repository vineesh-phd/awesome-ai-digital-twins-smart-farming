"""Regenerate bibliography, BibTeX, and metadata evidence from curated JSON."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def author_text(paper):
    names = [f"{a['family']}, {a['given']}" for a in paper['authors']]
    return '; '.join(names[:6]) + ('; et al.' if len(names) > 6 else '')


def venue_text(paper):
    text = paper['venue']
    if paper.get('volume'):
        text += ', ' + paper['volume']
    if paper.get('issue'):
        text += '(' + paper['issue'] + ')'
    if paper.get('pages'):
        text += ', ' + paper['pages']
    return text


def bib_escape(value):
    return str(value).replace('\\', r'\textbackslash{}').replace('&', r'\&').replace('%', r'\%').replace('_', r'\_')


def outputs(data):
    papers = data['papers']
    published = sum(p['kind'] == 'published-paper' for p in papers)
    lines = ['# Annotated Research Bibliography', '', '[Back to collection](../README.md)', '',
             f"Checked: {data['checked_on']}. **{published} published scholarly papers**, plus a technical guide and a preprint.", '',
             'R01-R20 preserve manuscript numbering. R21-R25 are repository additions. Complete author lists are in [references.json](references.json); long lists below use et al. See [verification records](verification.md) and the [claim audit](../citation-audit/Citation_Integrity_Audit.md).', '']
    for category in data['categories']:
        lines += ['## ' + category, '']
        for p in papers:
            if p['category'] != category:
                continue
            lines += [f"### {p['id']} {p['title']}", '',
                      f"{author_text(p)} ({p['year']}). *{venue_text(p)}*.", '',
                      f"[Primary record]({p['url']}) | **Type:** {p['kind']}", '',
                      '**Relevance:** ' + p['relevance'], '', '**Evidence limit:** ' + p['limitation'], '']
    evidence = ['# Reference Verification Record', '', '[Back to bibliography](references.md)', '',
                'Bibliographic identity checks are AI-assisted checks against external metadata, not an independent human full-text review. The record covers title, author list, publication year, venue, and identifier where available. No DOI was invented for the FAO guide or NeurIPS proceedings item.', '',
                'Twenty-three items are published scholarly papers. R06 is a technical guide and R18 is a preprint; neither is needed for the minimum count. Publication year follows the cited journal issue rather than the year embedded in a DOI.', '',
                '| ID | Year | Type | Metadata evidence | Primary material | Checked |',
                '| --- | --- | --- | --- | --- | --- |']
    bib = []
    for p in papers:
        v = p['verification']
        evidence.append(f"| {p['id']} | {p['year']} | {p['kind']} | [Record]({v['metadata_source']}) | [Source]({v['primary_source']}) | {v['date']} |")
        entry_type = 'misc' if p['kind'] != 'published-paper' else 'inproceedings' if p['id'] == 'R17' else 'article'
        fields = dict(title='{' + bib_escape(p['title']) + '}',
                      author=' and '.join(bib_escape(a['family'] + ', ' + a['given']) for a in p['authors']),
                      year=str(p['year']))
        fields['booktitle' if entry_type == 'inproceedings' else 'journal' if entry_type == 'article' else 'howpublished'] = bib_escape(p['venue'])
        for k in ['volume', 'issue', 'pages', 'doi', 'url']:
            if p.get(k):
                fields['number' if k == 'issue' else k] = p[k].replace('-', '--') if k == 'pages' else p[k]
        bib.append('@' + entry_type + '{' + p['id'] + ',\n' + ',\n'.join('  ' + k + ' = {' + v + '}' for k, v in fields.items()) + '\n}\n')
    evidence += ['', '## Interpretation', '',
                 'A resolved DOI or matching Crossref record verifies identity, not the truth of a scientific conclusion. Selected primary material was inspected for topical fit; some publisher access is limited to summaries. The [audit](../citation-audit/Citation_Integrity_Audit.md) states the narrower claim-check scope. Student full-text review remains pending for all entries until the student records completion.', '',
                 '## Reproducibility', '',
                 'The structured catalogue preserves complete author lists and verification URLs. `python3 scripts/build_catalog.py --check` detects stale generated files without changing them. Bibliography generation makes no network requests and does not re-verify scientific claims.', '']
    return {'references/references.md': '\n'.join(lines),
            'references/verification.md': '\n'.join(evidence),
            'references/references.bib': '\n'.join(bib)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = json.loads((ROOT / 'references/references.json').read_text())
    mismatches = []
    for path, text in outputs(data).items():
        dest = ROOT / path
        if args.check:
            if not dest.exists() or dest.read_text() != text:
                mismatches.append(path)
        else:
            dest.write_text(text)
    if mismatches:
        raise SystemExit('Stale generated files: ' + ', '.join(mismatches))
    print('Catalogue outputs match curated data.' if args.check else 'Generated bibliography, BibTeX, and verification record.')


if __name__ == '__main__':
    main()
