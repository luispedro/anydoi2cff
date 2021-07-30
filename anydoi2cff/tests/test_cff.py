from anydoi2cff.main import generate_cff

data_macrel = {
    'DOI': '10.7717/peerj.10555',
    'ISSN': ['2167-8359'],
    'URL': 'http://dx.doi.org/10.7717/peerj.10555',
    'abstract': 'Very good software.',
    'alternative-id': ['10.7717/peerj.10555'],
    'archive': ['CLOCKSS', 'LOCKSS', 'Portico'],
    'article-number': 'e10555',
    'author': [{'ORCID': 'http://orcid.org/0000-0002-1974-1736',
                'affiliation': [{'name': 'Institute of Science and Technology for '
                                         'Brain-Inspired Intelligence, Fudan '
                                         'University, Shanghai, China'},
                                {'name': 'Ministry of Education, Key Laboratory '
                                         'of Computational Neuroscience and '
                                         'Brain-Inspired Intelligence, Shanghai, '
                                         'China'}],
                'authenticated-orcid': True,
                'family': 'Santos-Júnior',
                'given': 'Célio Dias',
                'sequence': 'first'},
               {'affiliation': [{'name': 'Institute of Science and Technology for '
                                         'Brain-Inspired Intelligence, Fudan '
                                         'University, Shanghai, China'},
                                {'name': 'Ministry of Education, Key Laboratory '
                                         'of Computational Neuroscience and '
                                         'Brain-Inspired Intelligence, Shanghai, '
                                         'China'}],
                'family': 'Pan',
                'given': 'Shaojun',
                'sequence': 'additional'},
               {'ORCID': 'http://orcid.org/0000-0002-4531-3970',
                'affiliation': [{'name': 'Institute of Science and Technology for '
                                         'Brain-Inspired Intelligence, Fudan '
                                         'University, Shanghai, China'},
                                {'name': 'Ministry of Education, Key Laboratory '
                                         'of Computational Neuroscience and '
                                         'Brain-Inspired Intelligence, Shanghai, '
                                         'China'}],
                'authenticated-orcid': True,
                'family': 'Zhao',
                'given': 'Xing-Ming',
                'sequence': 'additional'},
               {'ORCID': 'http://orcid.org/0000-0002-9280-7885',
                'affiliation': [{'name': 'Institute of Science and Technology for '
                                         'Brain-Inspired Intelligence, Fudan '
                                         'University, Shanghai, China'},
                                {'name': 'Ministry of Education, Key Laboratory '
                                         'of Computational Neuroscience and '
                                         'Brain-Inspired Intelligence, Shanghai, '
                                         'China'}],
                'authenticated-orcid': True,
                'family': 'Coelho',
                'given': 'Luis Pedro',
                'sequence': 'additional'}],
    'container-title': ['PeerJ'],
    'content-domain': {'crossmark-restriction': False, 'domain': []},
    'created': {'date-parts': [[2020, 12, 18]],
                'date-time': '2020-12-18T10:25:02Z',
                'timestamp': 1608287102000},
    'deposited': {'date-parts': [[2020, 12, 18]],
                  'date-time': '2020-12-18T10:25:49Z',
                  'timestamp': 1608287149000},
    'funder': [{'award': ['2020YFA0712403, 2018YFC0910500'],
                'name': 'National Key R&D Program of China'},
               {'DOI': '10.13039/501100001809',
                'award': ['61932008, 61772368'],
                'doi-asserted-by': 'crossref',
                'name': 'National Natural Science Foundation of China'},
               {'award': ['19511101404'],
                'name': 'Shanghai Science and Technology Innovation Fund'},
               {'award': ['2018SHZDZX01'],
                'name': 'Shanghai Municipal Science and Technology Major '
                        'Project'}],
    'indexed': {'date-parts': [[2021, 6, 4]],
                'date-time': '2021-06-04T22:12:28Z',
                'timestamp': 1622844748464},
    'is-referenced-by-count': 2,
    'issn-type': [{'type': 'electronic', 'value': '2167-8359'}],
    'issued': {'date-parts': [[2020, 12, 18]]},
    'language': 'en',
    'license': [{'URL': 'https://creativecommons.org/licenses/by/4.0/',
                 'content-version': 'unspecified',
                 'delay-in-days': 0,
                 'start': {'date-parts': [[2020, 12, 18]],
                           'date-time': '2020-12-18T00:00:00Z',
                           'timestamp': 1608249600000}}],
    'link': [{'URL': 'https://peerj.com/articles/10555.pdf',
              'content-type': 'application/pdf',
              'content-version': 'vor',
              'intended-application': 'text-mining'},
             {'URL': 'https://peerj.com/articles/10555.xml',
              'content-type': 'application/xml',
              'content-version': 'vor',
              'intended-application': 'text-mining'},
             {'URL': 'https://peerj.com/articles/10555.html',
              'content-type': 'text/html',
              'content-version': 'vor',
              'intended-application': 'text-mining'},
             {'URL': 'https://peerj.com/articles/10555.pdf',
              'content-type': 'unspecified',
              'content-version': 'vor',
              'intended-application': 'similarity-checking'}],
    'member': '4443',
    'original-title': [],
    'page': 'e10555',
    'prefix': '10.7717',
    'published': {'date-parts': [[2020, 12, 18]]},
    'published-online': {'date-parts': [[2020, 12, 18]]},
    'publisher': 'PeerJ',
    'reference-count': 60,
    'references-count': 60,
    'relation': {'has-review': [{'asserted-by': 'object',
                                 'id': '10.7287/peerj.10555v0.2/reviews/1',
                                 'id-type': 'doi'},
                                {'asserted-by': 'object',
                                 'id': '10.7287/peerj.10555v0.1/reviews/2',
                                 'id-type': 'doi'},
                                {'asserted-by': 'object',
                                 'id': '10.7287/peerj.10555v0.2/reviews/2',
                                 'id-type': 'doi'},
                                {'asserted-by': 'object',
                                 'id': '10.7287/peerj.10555v0.1/reviews/1',
                                 'id-type': 'doi'}]},
    'score': 1,
    'short-container-title': [],
    'short-title': [],
    'source': 'Crossref',
    'subject': ['General Agricultural and Biological Sciences',
                'General Biochemistry, Genetics and Molecular Biology',
                'General Medicine',
                'General Neuroscience'],
    'subtitle': [],
    'title': ['Macrel: antimicrobial peptide screening in genomes and '
              'metagenomes'],
    'type': 'journal-article',
    'volume': '8'
    }


def test_generate_cff():
    cff = generate_cff(data_macrel)
    assert 'date-released' in cff
