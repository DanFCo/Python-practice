from database import Database
import datetime
import uuid


class Post(object):

    # def __init__(self):
    #     self.title = "this is my title"
    #     self.content = "this is some content"
    #     self.author = "Jose"

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id

#-----------VVV This inserts it into our database VVV-----------------

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())
#----------------------------------------------------------------------

# ----VVV--This creates a JSON representation of the post, so we can save it to our database--VVV----

    def json(self):
        return{
            'id': self.id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }
#-------^^^^^----^^^^^-------^^^^^^^^---------------
@staticmethod
def from_mongo(id):
    #Post.from_mongo(123)
    return Database.find_one(collection='posts',query={'id':id})


@staticmethod
def from_blog(id):
    return[post for post in Database.find(collection='posts', query={'blog_id':id})]
