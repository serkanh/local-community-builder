from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from techfl.classified.views import ClassifiedListView, ClassifiedDetailView

urlpatterns = patterns("",
    url("^classifieds/$",
        ClassifiedListView.as_view(),
        name="classified_list"),
    url("^classified/(?P<slug>.*)/$",
        ClassifiedDetailView.as_view(),
        name="classified_detail"),
    #url("^$",
    #    LinkList.as_view(),
    #    name="home"),
    #url("^newest/$",
    #    LinkList.as_view(), {"by_score": False},
    #    name="link_list_latest"),
    #url("^comments/$",
    #    CommentList.as_view(), {"by_score": False},
    #    name="comment_list_latest"),
    #url("^best/$",
    #    CommentList.as_view(),
    #    name="comment_list_best"),
    #url("^link/create/$",
    #    login_required(LinkCreate.as_view()),
    #    name="link_create"),
    #url("^link/(?P<slug>.*)/$",
    #    LinkDetail.as_view(),
    #    name="link_detail"),
    #url("^users/(?P<username>.*)/links/$",
    #    LinkList.as_view(), {"by_score": False},
    #    name="link_list_user"),
    #url("^users/(?P<username>.*)/links/$",
    #    LinkList.as_view(), {"by_score": False},
    #    name="link_list_user"),
    #url("^users/(?P<username>.*)/comments/$",
    #    CommentList.as_view(), {"by_score": False},
    #    name="comment_list_user"),
)