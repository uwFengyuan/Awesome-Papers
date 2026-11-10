"""Independent paper attributes; never infer paper type from PDF page count."""
import re


def award_types(paper):
    """Keep original award names separate from normalized, non-overlapping types."""
    result = []
    for name in paper.get('awards', []):
        text = name.casefold()
        if re.search(r'honou?rable|runner.?up|finalist', text):
            kind = 'honorable_mention'
        elif re.search(r'^(?:sac|area chair)', text):
            kind = 'area_chair_honour'
        elif 'student' in text:
            kind = 'student_award'
        elif re.search(r'resource|social|theme|linguistic|reproduction|choice|new direction', text):
            kind = 'special_award'
        elif 'outstanding' in text:
            kind = 'outstanding'
        elif 'best' in text:
            kind = 'best'
        else:
            kind = 'other_award'
        result.append({'type': kind, 'original_name': name,
                       'evidence': list(paper.get('award_evidence', []))})
    return result


def paper_length(paper):
    """Return an evidenced category, or unverified for mixed proceedings volumes.

    Anthology long/short volume names are authoritative. A bibliography page
    range or a downloaded PDF's page count is deliberately not used here.
    """
    title = paper.get('booktitle', '')
    ident = paper['id']
    if re.search(r'\bshort papers?\b', title, re.I) or re.search(r'\.acl-short\.', ident):
        return 'short', 'official Anthology short-paper volume'
    if any(re.search(r'\bbest short paper\b', a, re.I) for a in paper.get('awards', [])):
        return 'short', 'official Best Short Paper award'
    if re.search(r'\blong papers?\b', title, re.I) or re.search(r'\.acl-long\.', ident):
        return 'long', 'official Anthology long-paper volume'
    # Legacy ACL identifies long and short proceedings as Pyy-1 and Pyy-2.
    if paper.get('venue') == 'ACL' and re.fullmatch(r'P\d{2}-[12]\d{3}', ident):
        if ident[4] == '1':
            return 'long', 'legacy ACL long-paper volume'
        return 'short', 'legacy ACL short-paper volume'
    explicit = paper.get('paper_length') or paper.get('paper_type')
    if explicit in {'long', 'short'} and paper.get('paper_length_evidence'):
        return explicit, paper['paper_length_evidence']
    if paper.get('venue') in {'ICML', 'ICLR', 'NeurIPS', 'AAAI'} and paper.get('track') in {
            'main', 'datasets_benchmarks', 'evaluations'} and paper.get('metadata_sources'):
        return 'long', 'verified regular full-paper track: ' + paper['metadata_sources'][0]
    return 'unverified', 'requires official paper-type or full-paper-track evidence'


def presentation_types(paper):
    result = []
    if paper.get('oral') and paper.get('oral_evidence'):
        result.append('Oral')
    for text in paper.get('presentation_original', []):
        if re.fullmatch(r'spotlight(?: presentation)?', text, re.I):
            result.append('Spotlight')
        if re.fullmatch(r'poster(?: presentation)?', text, re.I):
            result.append('Poster')
    if paper.get('oral_candidate'):
        result.append('Oral candidate (unverified)')
    return list(dict.fromkeys(result)) or ['Unverified']


def publication_track(paper):
    if 'findings' in paper.get('booktitle', '').casefold() or 'findings-' in paper['id']:
        return 'findings'
    return paper.get('track', 'unverified')
