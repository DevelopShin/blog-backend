from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from api.utils import obj_to_comment, obj_to_post, prev_next_post
from post.models import Post, Category, Tag, Comment
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import BaseCreateView


# Create your views here.


class ApiPostLV(BaseListView):
    paginate_by = 3

    def get_queryset(self):
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
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
        totalPage = context['paginator'].num_pages
        currentPage = context['page_obj'].number
        data = {
            "postList": postList,
            "totalPage": totalPage,
            "currentPage": currentPage,
        }
        return JsonResponse(data=data, safe=True, status=200)


class ApiPostDV(BaseDetailView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        obj = context['object']
        obj.watch += 1
        obj.save()
        post = obj_to_post(obj)
        prevPost, nextPost = prev_next_post(obj)
        comments = [obj_to_comment(c) for c in obj.comment_set.all()]
        data = {
            'post': post,
            'prevPost': prevPost,
            'nextPost': nextPost,
            'comments': comments
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


class ApiAddComment(BaseCreateView):
    model = Comment
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        comment = obj_to_comment(self.object)
        return JsonResponse(data=comment, safe=True, status=201)

    def form_invalid(self, form):
        return JsonResponse(data=form.errors, safe=True, status=400)
