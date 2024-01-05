from django.urls import path
from .views import RegisterView,LoginUserView,ViewProfile,LogoutView,CategoryList


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginUserView.as_view()),
    path('profile',ViewProfile.as_view()),
    path('logout',LogoutView.as_view()),
    path('categories', CategoryList.as_view()),
]
