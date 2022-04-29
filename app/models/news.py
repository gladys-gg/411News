class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,title,poster,publishedAt,content):
        self.id = id
        self.name = name
        self.title = title
        self.poster = "https://www.reuters.com/resizer/KmoBUq7O3ko1-HAK_opxKq_NvRA=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/CSTERWE76FL5JPXLJY5FWFDJOY.jpg"+ poster
        self.publishedAt = publishedAt
        self.content = content