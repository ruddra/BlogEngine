# Create your views here.
from blog.models import Post
from django.shortcuts import render_to_response
from django.shortcuts import render
from blog.utils import *
from django.template import RequestContext

def search(request):
    query_string = ''
    found_entries = None
    #q=request.POST['q']
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['title','body',])

        found_entries = Post.objects.all().filter(entry_query).order_by('-created')

    return render(request,'searchResult.html',
        { 'query_string': query_string, 'found_entries': found_entries },
        context_instance=RequestContext(request))

#def searchResult(request):
#    return render('searchResult.html')

def tagpage(request, tag):
    PostsInTags=Post.objects.filter(tags__name=tag)
    return render(request,"tagpage.html",{"post": PostsInTags,"tag":tag})

def showpage(request):
    return render(request,"about.html")

def contactpage(request):
    return render(request,"contact.html")