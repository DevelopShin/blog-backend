from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from api.utils import obj_to_post, prev_next_post
from post.models import Post


# Create your views here.


class ApiPostLV(BaseListView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        qs = context['object_list']
        postList = [obj_to_post(obj, True) for obj in qs]
        return JsonResponse(data=postList, safe=False, status=200)


class ApiPostDV(BaseDetailView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        obj = context['object']
        post = obj_to_post(obj)
        prevPost, nextPost = prev_next_post(obj)
        data = {
            'post': post,
            'prevPost': prevPost,
            'nextPost': nextPost
        }
        return JsonResponse(data=data, safe=False, status=200)
