from django.urls import path #type:ignore
from.import views
urlpatterns=[
       path('pagehtml/',views.pagehtml),
       path('index/',views.index),
       path('display/',views.display)
]