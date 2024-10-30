from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import get_object_or_404


# Create your views here.
def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)  # Paginator with three posts per page.
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(
            paginator.num_pages
        )  # If page_number is out of range get last page of results

    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No post found.")
    # return render(request, "blog/post/detail.html", {"post": post})
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post/detail.html", {"post": post})
