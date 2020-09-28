#How to acces pages with Paginator and extract information
#about those pages

In [1]: from django.core.paginator import Paginator

In [2]: posts = ['1', '2', '3', '4', '5']

In [3]: p = Paginator(posts, 2)

In [4]: p.num_pages
Out[4]: 3

In [5]: for page in p.page_range:
   ...:     print(page)
   ...:
1
2
3

In [6]: p1 = p.page(1)

In [7]: p1
Out[7]: <Page 1 of 3>

In [8]: p1.number
Out[8]: 1

In [9]: p1.object_list
Out[9]: ['1', '2']

In [10]: p1.has_previous()
Out[10]: False

In [11]: p1.has_next()
Out[11]: True

In [12]: p1.next_page_number()
Out[12]: 2