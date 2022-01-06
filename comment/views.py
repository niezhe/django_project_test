from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from article.models import ArticlePost
from .forms import CommentForm
from .models import Comment


# 文章评论
@login_required(login_url='/userprofile/login/')
# 新增参数parent_comment_id
def post_comment(request, article_id, parent_comment_id=None):
    article = get_object_or_404(ArticlePost, id=article_id)

    # 处理POST请求
    if request.method == 'POST':
        comment_for = CommentForm(request.POST)
        if comment_for.is_valid():
            new_comment = comment_for.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            # 二级回复
            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                # 若回复层级超过二级，则转换为二级
                new_comment.parent_id = parent_comment.get_root().id
                # 被回复的人
                new_comment.reply_to = parent_comment.user
                new_comment.save()
                return HttpResponse('200 OK')

            new_comment.save()
            return redirect(article)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
        # 处理GET请求
    elif request.method == 'GET':
        comment_form = CommentForm()
        context = {
            'comment_form': comment_form,
            'article_id': article_id,
            'parent_comment_id': parent_comment_id
        }
        return render(request,'comment/reply.html',context)
    # 处理其他请求
    else:
        return HttpResponse("仅接受GET/POST请求。")