from django.urls import path

from feedback.views import feedback_add, feedback_list

app_name = 'feedback'

urlpatterns = [
    path('list/', feedback_list, name="feedback_list"),
    path('add/', feedback_add, name="feedback_add")
]
