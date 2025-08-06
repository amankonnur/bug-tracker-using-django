from defects import views
from django.urls import path

urlpatterns = [
    path('defects_list', views.defect_list, name='defect_list'),
    path('<int:id>', views.description, name='description'),
    path('edit/<int:id>',views.edit_defect,name='edit'),
]

