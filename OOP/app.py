# import pymongo
#
# uri = "mongodb://127.0.0.1:27017"
# client = pymongo.MongClient(uri)
# database = client["fullstack"]
# collection = database['students']
#
#
# students = [student for student in collection.find({})]
#
#
# print(students)

#---------------------------------------------------------------

# from models.post import Post
#
# post = Post()
# post2 = Post()
#
# print(post.content)
#
# print(post2.content)
# print(post.author)
# post2.author = "Danny"
# print(post2.author)

# ----------------------------------------------------------------

from post import Post
from database import Database

Database.initialize()

post = Post(blog_id='123',
            title='Another Great Post',
            content='some content',
            author='jose')

post.save_to_mongo()
