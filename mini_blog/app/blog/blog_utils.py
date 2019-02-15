from django.db import models
from django.shortcuts import render
from .models import *

POST_PER_PAGE = 5
MAX_TEXT_BLOG = 800

def get_post_context(post_tag):
    try:
        post = Post.objects.all().filter(tag=post_tag)[0]
        print(str(post.tag))
        if post:
            context = {
                "title" : post.title,
                "content" : post.content,
                "cover" : post.cover.url,
                "caption" : post.caption,
                "id" : str(post.tag),
                "good" : True,
                "date" : post.date,
            }
            return context
        else:
            return {"good": False}
    except Exception as e:
        print(e)
        return {"good": False}

def get_posts_page(page_num):
    if page_num <= 0:
        page_num =1
    page_num -= 1
    content = Post.objects.all()
    try:
        if (len(content) < page_num * POST_PER_PAGE):
            return []
        else:
            items = content[(page_num) * POST_PER_PAGE:]
            page =[]
            i =0
            for item in items:
                post = {
                    "title" : item.title,
                    "content" : item.content[:MAX_TEXT_BLOG - 3] + "...",
                    "cover" : item.cover.url,
                    "caption" : item.caption,
                    "id" : str(item.tag),
                    "date" : item.date,
                }
                page.append(post)
                i +=1
                if i > POST_PER_PAGE-1:
                    return page
            return page
    except Exception as e:
        print(e)
        return [] 