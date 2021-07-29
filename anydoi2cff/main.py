import requests
import json
import yaml

BASE_URL = 'https://api.crossref.org/works/'

def norm_doi(doi):
    for prefix in ['http://doi.org/',
            'https://doi.org/']:
        if doi.startswith(prefix):
            return doi[len(prefix):]
    return doi

def get_doi_meta(doi):
    '''Looks up DOI metadata on crossref'''
    doi = norm_doi(doi)
    r = requests.get(BASE_URL + doi)
    if r.status_code != 200:
        raise IOError("Yeah, something bad happened")
    data = r.json()
    return data['message']

def generate_cff(data):
    [title] = data['title']
    doi = data['DOI']
    authors = []
    for aut in data.get('author', []):
        authors.append({
                  'family-names': aut['family'],
                  'given-names': aut['given'],
                  'orcid': aut.get('ORCID'),
                  })
    if not authors:
        import sys
        sys.stderr.write("Author information is missing.\n")
        sys.stderr.write("Proceeding... but check results manually\n")
    [date_parts] = data['published-print']['date-parts']
    if len(date_parts) == 3:
        year, month, day = date_parts
    elif len(date_parts) == 2:
        year, month = date_parts
        day = 1
    else:
        raise ValueError(f"Cannot parse date parts of form '{date_parts}'")
    return {
        'cff-version': '1.1.0',
        'message': "If you use this software, please cite it as below.",
        'title': title,
        'authors': authors,
        'doi': doi,
        'date-released': f'{year}-{month}-{day}',
        'version': '0.0.0',
        }


def main(argv):
    if len(argv) != 2:
        import sys
        sys.stderr.write('Usage:\n')
        sys.stderr.write(f'\t{argv[0]} <DOI>\n')
        sys.exit(1)
    _,doi = argv
    meta = get_doi_meta(doi)
    cff = generate_cff(meta)
    print(yaml.dump(cff, sort_keys=False))

if __name__ == '__main__':
    import sys
    main(sys.argv)

