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

from models.post import Post

post = Post("Great Gatsby","About Rich people being rich ", "White Guy")

print(post.content)
