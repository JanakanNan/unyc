from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from unycAPI import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'stocks', views.ListStock)
router.register(r'bar/ranking', views.ListRanking)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('references/', views.ListBieres.as_view()),
    path('references/<int:pk>/', views.BiereDetail.as_view()),
    path('bars/', views.ListComptoirs.as_view()),
    path('bars/<int:pk>/', views.ComptoirsDetail.as_view()),
    path('admin/', admin.site.urls),
    path('stock/<int:coid>/', views.StockDetailView.as_view()),
    path('bars/ranking/', views.RankingComptoir.as_view()),
]