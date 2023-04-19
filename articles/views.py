from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import pluralize, dictsort
from .models import Article


def main(request: HttpResponse):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/main.html', context)


def title(request, article_id: int):
    article = get_object_or_404(Article, id=article_id)
    context = {'article': article}
    return render(request, 'articles/title.html', context)


def like(request, article_id: int):
    article = get_object_or_404(Article, id=article_id)
    like_session = request.session.get("like_object", [])
    if article_id in like_session:
        like_session.remove(article_id)
        article.like_count -= 1
    else:
        like_session.append(article_id)
        article.like_count += 1
    request.session['like_object'] = like_session
    article.save()
    return redirect('articles:title', article.id)
