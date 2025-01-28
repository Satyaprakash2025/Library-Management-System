"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import ahome,shome,index,book_management,books_avail,issue_book,issue_list,delete_book
from login.views import login,logout_view
from register.views import register

urlpatterns = [
    path('admin/', admin.site.urls),

    #home
    path('',index,name='dashboard'),
    path('ahome',ahome,name='ahome'),
    path('shome',shome,name='shome'),
    path('books',book_management,name='books'),
    path('delete_book/<str:isbn_no>/',delete_book,name='delete_book'),
    path('books_avail',books_avail,name='books_avail'),
    path('issue_book',issue_book,name='issue_book'),
    path('book_issue_list',issue_list,name='book_issue_list'),
    path('approve/', issue_list, name='approve_issue'),  # Same view for POST handling
    path('decline/', issue_list, name='decline_issue'),

    #login
    path('login/', login),
    path('logout/',logout_view, name="logout"),

    #register
    path('register/', register),

]
