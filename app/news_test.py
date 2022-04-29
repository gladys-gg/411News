import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("reuters","Reuters","Russian users sue Apple after payment service pulled -lawyers - Reuters", "https://www.reuters.com/resizer/KmoBUq7O3ko1-HAK_opxKq_NvRA=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/CSTERWE76FL5JPXLJY5FWFDJOY.jpg","2022-04-29T10:28:00Z","Posted \r\n04/29 Apple on Thursday forecast bigger problems as COVID-19 lockdowns snarl production and demand in China, the war in Ukraine dents sales and growth slows in services, which the iPhone mak… [+64 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()