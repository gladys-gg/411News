class Articles:
    '''
    Source class to define News Objects
    '''

    def __init__(self,title,urlToImage,content,author,publishedAt,url):
        self.title = title
        self.urlToImage = urlToImage
        self.content = content
        self.author = author
        self.publishedAt = publishedAt
        self.url = url