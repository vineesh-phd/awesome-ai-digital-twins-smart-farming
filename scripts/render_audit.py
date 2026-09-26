"""Build the citation-audit PDF from its Markdown source (requires ReportLab)."""
import re
from html import escape
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'citation-audit/Citation_Integrity_Audit.md'
DEST = SOURCE.with_suffix('.pdf')


def inline(text):
    text = escape(text)
    # Local repository links remain readable labels in the standalone PDF.
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
                  lambda m: f'<link href="{m[2]}">{m[1]}</link>' if m[2].startswith('https://') else m[1], text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', text)
    return re.sub(r'`([^`]+)`', r'\1', text)


def main():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle('AuditBody', fontName='Helvetica', fontSize=10.5, leading=15, spaceAfter=9))
    styles.add(ParagraphStyle('AuditTitle', fontName='Helvetica-Bold', fontSize=22, leading=27, spaceAfter=16, keepWithNext=True))
    styles.add(ParagraphStyle('AuditHeading', fontName='Helvetica-Bold', fontSize=13, leading=17, spaceBefore=12, spaceAfter=7, keepWithNext=True))
    styles.add(ParagraphStyle('AuditCell', fontName='Helvetica', fontSize=8.2, leading=11, alignment=TA_LEFT))
    doc = SimpleDocTemplate(str(DEST), pagesize=A4, rightMargin=43, leftMargin=43,
                            topMargin=49, bottomMargin=44,
                            title='Citation Integrity Audit: AI and Digital Twins for Smart Farming',
                            author='AI-assisted research repository')
    story = []
    blocks = re.split(r'\n\s*\n', SOURCE.read_text().strip())
    for block in blocks:
        if block.startswith('# '):
            story.append(Paragraph(inline(block[2:]), styles['AuditTitle']))
        elif block.startswith('## '):
            story.append(Paragraph(inline(block[3:]), styles['AuditHeading']))
        elif block.startswith('|'):
            rows = []
            for line in block.splitlines():
                if re.fullmatch(r'[| :\-]+', line):
                    continue
                cells = [c.strip() for c in line.strip('|').split('|')]
                rows.append([Paragraph(inline(c), styles['AuditCell']) for c in cells])
            table = Table(rows, colWidths=[29, 169, 99, doc.width - 297], repeatRows=1, hAlign='LEFT')
            table.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e9edef')),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')]),
                ('LINEBELOW', (0, 0), (-1, 0), .6, colors.HexColor('#667780')),
                ('LINEBELOW', (0, 1), (-1, -1), .25, colors.HexColor('#d7dddf')),
                ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                ('TOPPADDING', (0, 0), (-1, -1), 7), ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
            ]))
            story.extend([table, Spacer(1, 8)])
        elif block.startswith('- ') or re.match(r'^\d+\. ', block):
            for line in block.splitlines():
                text = line[2:] if line.startswith('- ') else line
                prefix = '- ' if line.startswith('- ') else ''
                story.append(Paragraph(prefix + inline(text), styles['AuditBody']))
        else:
            text = inline(block).replace('  \n', '<br/>').replace('\n', ' ')
            story.append(Paragraph(text, styles['AuditBody']))

    def page(canvas, document):
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.HexColor('#53616a'))
        canvas.drawString(43, A4[1] - 29, 'SMART FARMING / CITATION INTEGRITY')
        canvas.drawString(43, 25, 'AI-assisted audit | Student full-text review pending')
        canvas.drawRightString(A4[0] - 43, 25, str(document.page))
        canvas.restoreState()

    doc.build(story, onFirstPage=page, onLaterPages=page)
    print(DEST)


if __name__ == '__main__':
    main()
