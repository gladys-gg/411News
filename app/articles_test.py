import unittest
from models import articles
Articles = articles.Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles("","","","","","")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))


if __name__ == '__main__':
    unittest.main()