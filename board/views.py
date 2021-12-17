from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from .models import Post, Category, Comment
from .forms import CommentForm
from django.core.exceptions import PermissionDenied
# redirect 오류가 나던 이유 : redirect 를 import 하지 않았다.


# 글 삭제 view 
def PostDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/board/')

# 댓글 삭제 view.
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else :
        raise PermissionDenied

# 댓글 수정 view
class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else :
            raise PermissionDenied

# 댓글 작성 view
def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else :
            return redirect(post.get_absolute_url())
    else :
        raise PermissionDenied

# 게시판의 글을 보여주는 view.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

# 게시판에서 글을 클릭했을 때 게시글의 내용을 보여주는 view
class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm # commentForm 적용하기
        return context

# 게시물을 만들 때의 view
class PostCreate(LoginRequiredMixin, CreateView): # LoginRequiredMixin 추가하여 로그인했을때만 정상적으로 페이지 보이게 수정.
    model = Post
    fields = ['title', 'content', 'upload_image', 'category']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated :
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else :
            return redirect('/board/')

# 게시물을 수정할때의 view이다.
class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'upload_image', 'category']

    template_name = 'board/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else :
            raise PermissionDenied

# 우측으 카테고리 목록에서 카테고리를 클릭했을 때의 view.
def category_page(request, slug):
    if slug == 'no_category':
        category = '기타'
        post_list = Post.objects.filter(category=None)
    else :
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render (
        request,
        'board/post_list.html',
        {
            'post_list' : post_list,
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
            'category' : category,
        }
    )

# 우측 검색창에서 검색을 했을때의 view.
class PostSearch(PostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(title__contains=q)
        ).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context
