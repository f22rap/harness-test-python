import unittest
from search import search
class SearchTests(unittest.TestCase):
    def test_empty_and_whitespace(self):
        for query in ('','  ','\t\n'):
            self.assertEqual(search(query,['alpha']),[])
    def test_normal_input_retains_order(self):
        self.assertEqual(search('AL',['alpha','beta','Alpine']),['alpha','Alpine'])
    def test_no_match_and_unicode(self):
        self.assertEqual(search('東京',['東京都','大阪府']),['東京都'])
        self.assertEqual(search('z',['alpha']),[])
if __name__=='__main__': unittest.main()
