from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.fizzbuzz_list_create_view),
    # path('', views.fizzbuzz_create_view),
    # path('', views.fizzbuzz_list_view),
    path('<int:pk>/', views.fizzbuzz_detail_view),
]



# '''
# VVVV This works  VVVVV
# '''
# urlpatterns = [
#     path('', views.api_home),

# ]
# '''
# ^^^^
# '''