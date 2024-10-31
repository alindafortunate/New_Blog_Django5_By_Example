from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import ListView
from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import get_object_or_404
from .forms import EmailPostForm


# Create your views here.
class PostListView(ListView):
    """
    Alternative post list view
    """

    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)  # Paginator with three posts per page.
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)  # If page is not an integer, get the first page.
    except EmptyPage:
        posts = paginator.page(
            paginator.num_pages
        )  # If page_number is out of range get last page of results

    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):

    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post/detail.html", {"post": post})


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    if request.method == "POST":
        # Form was submitted.
        form = EmailPostForm(request.POST)
    if form.is_valid():
        # Form fields passed validation.
        cd = form.cleaned_data
    # send email
    else:
        form = EmailPostForm()
    return render(request, "blog/post/share.html", {"post": post, "form": form})
