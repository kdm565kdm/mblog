from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect


def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render({'posts':posts,'now':now})
    #post_lists = list()
    #for count, post in enumerate(posts):
        #tem = count+1
        #post_lists.append("No.{}:".format(str(tem)) + str(post) +"<hr>")
        #post_lists.append("<small>"+str(post.body)+"</small><br><br>")
    #return HttpResponse(post_lists)
    return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render({'post':post})
            return HttpResponse(html)
    except:
        return redirect('/')