from django.conf.urls import include
from django.urls import path
from rest_framework import routers
# from .views import article_list,article_detail
from .views import LogViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('log',LogViewset,basename='log')

urlpatterns = [
    path('viewset/',include(router.urls)),
    # path('viewset/<int:pk>/',include(router.urls)),
    # # path('articles/',article_list),
    # path('articles/',ArticleAPIView.as_view()),
    # # path('detail/<int:pk>',article_detail)
    # path('detail/<int:pk>',ArticleAPIView.as_view()),
    # # path('generic/articles/',GenericAPIView.as_view()),
    # path('generic/articles/<int:id>/',GenericAPIView.as_view()),
]