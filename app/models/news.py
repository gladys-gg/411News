class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,title,poster,publishedAt,content):
        self.id = id
        self.name = name
        self.title = title
        self.poster = poster
        self.publishedAt = publishedAt
        self.content = content