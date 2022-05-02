class Sources:
    '''
    Source class to define News Objects
    '''

    def __init__(self,id,name,category,description,url):
        self.id = id
        self.name = name
        self.category = category
        self.description = description
        self.url = url
       
        



class Articles:
    '''
    Source class to define News Objects
    '''

    def __init__(self,title,urlToImage,content,url,author,publishedAt):
        self.title = title
        self.urlToImage = urlToImage
        self.content = content
        self.url = url
        self.author = author
        self.publishedAt = publishedAt
        
 