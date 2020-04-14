### Markdown语法
* pip install markdown
```python
def blog_detail(request,id):
    blog=get_object_or_404(Blog,id=id)
    blog.body = markdown.markdown(blog.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])
    return render(request,'blog/detail.html',context={'blog':blog})
```



