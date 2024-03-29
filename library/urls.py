"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from web import views
from web import account

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('manager/',views.manager),
    path('reader/',views.reader),
    path('manager/card/',views.manager_card),
    path('manager/card/add/',views.manager_card_add),
    path('manager/card/delete/',views.manager_card_delete),
    path('book/add/',views.book_add),
    path('book/add/suc/',views.book_add_suc),
    path('book/list/',views.book_list),
    path('book/list2/',views.book_list2),
    path('login/',account.login),
    path('logout/',account.logout),
    path('book/borrow/',views.book_borrow),
    path('book/borrow2/',views.book_borrow2),
    path('book/reborrow/',views.book_reborrow),
    path('book/reborrow2/',views.book_reborrow2),
    path('book/return/',views.book_return),
    path('book/return2/',views.book_return2),
    path('book/modify/',views.book_modify),
    path('book/modify2/',views.book_modify2),
    path('register/',account.register),
    ]
