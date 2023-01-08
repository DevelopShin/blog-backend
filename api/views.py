from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from api.utils import obj_to_post, prev_next_post
from post.models import Post, Category, Tag


# Create your views here.


class ApiPostLV(BaseListView):

    def get_queryset(self):
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        print('keyword: ', category, tag)
        if category:
            qs = Post.objects.filter(category__name__iexact=category)
        elif tag:
            qs = Post.objects.filter(tags__name__iexact=tag)
        else:
            qs = Post.objects.all()
        return qs

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


class ApiCateTagView(View):

    def get(self, request, *args, **kwargs):
        c = [v.name for v in Category.objects.all()]
        t = [v.name for v in Tag.objects.all()]

        json = {
            'cateList': c,
            'tagList': t,
        }
        return JsonResponse(data=json, safe=True, status=200)
