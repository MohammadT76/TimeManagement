from django.urls import path
import user.views as user_views

urlpatterns = [
    path('Hello/' , user_views.Hello.as_view() , name = "user_Hello"),
]
