class Sources:
    '''
    Source class to define News Objects
    '''

    def __init__(self,id,name,category,description,url):
        self.id = id
        self.name = name
        self.url = url
        self.category = category
        self.description = description
        