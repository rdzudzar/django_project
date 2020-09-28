# Read in .json file, loop through posts and save them into Post

In [1]: import json

In [3]: from blog.models import Post

In [4]: with open('posts.json') as f:
   ...:     posts_json = json.load(f)
   ...:

In [6]: for post in posts_json:
   ...:     post = Post(title=post['title'], content=post['content'], author_id = post['user_id'])
   ...:     post.save()
   ...:
