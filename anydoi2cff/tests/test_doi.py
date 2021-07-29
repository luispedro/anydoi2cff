def test_simple_doi():
    doi = 'http://doi.org/10.5334/jors.161'

    assert norm_doi(doi) == '10.5334/jors.161'
    assert norm_doi(norm_doi(doi)) == '10.5334/jors.161'

