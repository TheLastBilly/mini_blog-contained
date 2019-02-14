from django.shortcuts import render
from .blog_utils import *
from django.http import HttpResponse

PAGE_NAME = "LastcWroks"

def get_icon():
    try:
        icon_image = PageIcon.objects.all()[0]
        return icon_image.icon.url
    except Exception as e:
        return " "

def page_not_found(request):
    post = {
        "title" : "Oops!, there's nothing here!",
    }
    return render(request, "blog/article.html", {"title": PAGE_NAME, "post" : post, "icon" : get_icon()})

def render_post(request, post_tag):
    context = get_post_context(post_tag)
    context["icon"] = get_icon()
    if context["good"]:
        return render(request, "blog/article.html", {"post": context})
    else:
        return page_not_found(request)

def render_posts_page(request, page_num):
    posts = get_posts_page(page_num)
    if len(posts) > 0:
        foot_links =[]
        psts = Post.objects.all()
        i =0
        pages = 1
        print(psts)
        for page in psts:
            i += 1
            if i > POST_PER_PAGE:
                pages += 1
        print(pages)
        for i in range(1, pages+1):
            foot_links.append({"number" : str(i)})
        context = {
            "posts" : posts,
            "title" : PAGE_NAME,
            "footer_links" : foot_links,
            "icon" : get_icon(),
        }
        context["alone"] = False
        return render(request, "blog/blog.html", context)
    else:
        return page_not_found(request)

def blog_index(request):
    return render_posts_page(request, 1)

def blog(request, page_num):
    return render_posts_page(request, page_num)

def get_post(request, post_tag):
    return render_post(request, post_tag)

def latest_post(request):
    post = Post.objects.all().order_by("-pk")[:1]
    return render_post(request, post[0].id)