#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
# JPM modified distribution, 2026-09-24. See package-root NOTICE.md and CHANGES.md.
"""Read DOCX into ordered review records with the optional python-docx library.

Usage: read_word.py draft.docx --out NEW_DIRECTORY
The output is evidence for an agent to review, not a final article or a promise
of page-layout fidelity. Plain-text, Markdown and JSON rendering do not need docx.
"""
from pathlib import Path
import argparse
import hashlib
import json
import mimetypes


def collect_document(source, destination):
    try:
        from docx import Document
        from docx.text.paragraph import Paragraph
        from docx.text.hyperlink import Hyperlink
        from docx.drawing import Drawing
    except ImportError as exc:
        raise ValueError('Word import requires python-docx 1.2 or newer; use an available document runtime or supply Markdown.') from exc
    if destination.exists():
        raise ValueError('Choose a new output directory; existing files are not overwritten.')
    document = Document(source)
    if not hasattr(document, 'iter_inner_content'):
        raise ValueError('This python-docx version lacks ordered content traversal; use version 1.2 or newer.')
    destination.mkdir(parents=True)
    assets = []
    warnings = []
    saved = {}

    def picture(drawing, part):
        tokens = []
        for node in drawing._drawing.iter():
            if node.tag.rsplit('}', 1)[-1] != 'blip':
                continue
            for attr, relationship_id in node.attrib.items():
                role = attr.rsplit('}', 1)[-1]
                if role not in {'embed', 'link'}:
                    continue
                relationship = part.rels.get(relationship_id)
                if relationship is None:
                    warnings.append('Image relationship is missing: ' + relationship_id)
                    continue
                if relationship.is_external:
                    tokens.append({'kind': 'image', 'source': relationship.target_ref, 'external': True})
                    continue
                media = relationship.target_part
                digest = hashlib.sha256(media.blob).hexdigest()
                if digest not in saved:
                    extension = mimetypes.guess_extension(media.content_type) or '.bin'
                    folder = destination / 'media'
                    folder.mkdir(exist_ok=True)
                    name = digest[:20] + extension
                    (folder / name).write_bytes(media.blob)
                    saved[digest] = 'media/' + name
                    assets.append({'source': saved[digest], 'sha256': digest, 'mime': media.content_type})
                tokens.append({'kind': 'image', 'source': saved[digest]})
        if not tokens:
            warnings.append('A drawing has no supported image payload; inspect it in the source document.')
        return tokens

    def run_tokens(run):
        tokens = []
        for item in run.iter_inner_content():
            if isinstance(item, str):
                # Keep formatting as data; do not inject Markdown delimiters or alter punctuation.
                tokens.append({'kind': 'text', 'value': item,
                               'bold': bool(run.bold), 'italic': bool(run.italic),
                               'underline': bool(run.underline)})
            elif isinstance(item, Drawing):
                tokens.extend(picture(item, run.part))
        return tokens

    def paragraph_record(paragraph):
        tokens = []
        for chunk in paragraph.iter_inner_content():
            if isinstance(chunk, Hyperlink):
                tokens.append({'kind': 'link', 'url': chunk.url,
                               'content': [token for run in chunk.runs for token in run_tokens(run)]})
            else:
                tokens.extend(run_tokens(chunk))
        numbering = paragraph._p.xpath('./w:pPr/w:numPr')
        return {'kind': 'paragraph', 'style': paragraph.style.name if paragraph.style else '',
                'hasNumbering': bool(numbering), 'tokens': tokens}

    def records(container):
        result = []
        for item in container.iter_inner_content():
            if isinstance(item, Paragraph):
                result.append(paragraph_record(item))
                continue
            # A merged cell is stored once; the row matrix retains references to it.
            # This avoids repeating its text when the agent assembles an article.
            identities = {}
            cell_records = []
            matrix = []
            for row in item.rows:
                cell_ids = []
                for cell in row.cells:
                    key = cell._tc
                    if key not in identities:
                        identities[key] = len(cell_records)
                        cell_records.append(records(cell))
                    cell_ids.append(identities[key])
                matrix.append({'before': row.grid_cols_before, 'cells': cell_ids, 'after': row.grid_cols_after})
            result.append({'kind': 'table', 'rows': matrix, 'cells': cell_records})
        return result

    body = records(document)
    special = {'txbxContent': 'text boxes', 'footnoteReference': 'footnotes',
               'endnoteReference': 'endnotes', 'ins': 'tracked insertions',
               'del': 'tracked deletions', 'sdt': 'content controls',
               'pict': 'legacy graphics', 'oMath': 'equations',
               'fldSimple': 'fields', 'fldChar': 'field instructions',
               'altChunk': 'embedded documents', 'smartTag': 'smart tags'}
    present = {node.tag.rsplit('}', 1)[-1] for node in document.element.iter()}
    for key, label in special.items():
        if key in present:
            warnings.append('Source contains ' + label + '; inspect and recover content before rendering.')
    result = {'format': 'jpm-word-review-v1', 'sourceFile': source.name,
              'sourceSha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'records': body, 'assets': assets, 'warnings': warnings,
              'reviewRequired': True,
              'limits': ['Headers and footers are excluded from the article body.',
                         'Numbering, inherited formatting, floating-object layout and complex fields require review.']}
    (destination / 'word-review.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    try:
        result = collect_document(args.input, args.out)
    except Exception as exc:
        parser.exit(1, 'Word import incomplete: ' + str(exc) + '\n')
    print(json.dumps({'review': str(args.out / 'word-review.json'),
                      'mediaFiles': len(result['assets']), 'warnings': result['warnings']}, ensure_ascii=False))

if __name__ == '__main__':
    main()
