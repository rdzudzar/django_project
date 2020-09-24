#run
python manage.py shell
#import
In [1]: from blog.models import Post

In [2]: from django.contrib.auth.models import User
#see users
In [3]: User.objects.all()
Out[3]: <QuerySet [<User: rdzudzar>, <User: TestUser>]>

In [4]: User.objects.first()
Out[4]: <User: rdzudzar>
#query with filter
In [5]: User.objects.filter(username='rdzudzar')
Out[5]: <QuerySet [<User: rdzudzar>]>

In [6]: User.objects.filter(username='rdzudzar').first()
Out[6]: <User: rdzudzar>

In [7]: user = User.objects.filter(username='rdzudzar').first()

In [8]: user
Out[8]: <User: rdzudzar>
#get id
In [9]: user.id
Out[9]: 1
#gets primary key
In [10]: user.pk
Out[10]: 1

In [12]: user = User.objects.get(id=1)

In [13]: user
Out[13]: <User: rdzudzar>

In [14]: Post.objects.all()
Out[14]: <QuerySet []>
#create a post
In [15]: post_1 = Post(title='Blog 1', content='Fist post content!', author=user)

In [16]: Post.objects.all()
Out[16]: <QuerySet []>
#save a post
In [17]: post_1.save()
#now the post is in the DB
In [18]: Post.objects.all()
Out[18]: <QuerySet [<Post: Post object (1)>]>

#what to be printed out as post object - we do this with 
# def __str__ method (see models.py)

In [3]: Post.objects.all()
Out[3]: <QuerySet [<Post: Blog 1>]>

In [4]: user = User.objects.filter(username='rdzudzar').first()

In [5]: user
Out[5]: <User: rdzudzar>

In [7]: post_2 = Post(title='Blog 2', content='Second post content!', author_id=user.id)

In [8]: post_2.save()
# now the post object is printed as the post title
In [9]: Post.objects.all()
Out[9]: <QuerySet [<Post: Blog 1>, <Post: Blog 2>]>

In [10]: post = Post.objects.first()

In [11]: post.content
Out[11]: 'Fist post content!'
# get the date
In [12]: post.date_posted
Out[12]: datetime.datetime(2020, 9, 24, 4, 9, 52, 556904, tzinfo=<UTC>)

In [13]: post.author
Out[13]: <User: rdzudzar>

In [14]: post.author.email
Out[14]: 'robertdzudzar@gmail.com'

In [15]: user.post_set
Out[15]: <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager at 0x209ed62c588>

In [16]: user.post_set.all()
Out[16]: <QuerySet [<Post: Blog 1>, <Post: Blog 2>]>
#this way we create posts directly using post_set
In [17]: user.post_set.create(title='Blog 3', content='Third post content!')
Out[17]: <Post: Blog 3>

In [18]: Post.objects.all()
Out[18]: <QuerySet [<Post: Blog 1>, <Post: Blog 2>, <Post: Blog 3>]>