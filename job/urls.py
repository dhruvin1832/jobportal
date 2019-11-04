from django.urls import path,include
from .import views
print("job_urls")
urlpatterns = [
    path('',views.index,name='index'),
    path('search/job/',views.search,name='search_job'),
    path('otp/',views.otp,name='otp'),
    path('otp_company',views.otp_company,name='otp_company'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('base/',views.base,name='base'),
    path('contact/',views.contact,name='contact'),
    path('job-post/',views.job_post,name='job-post'),
    path("register/", views.register, name="register"),
    path("register_company/", views.register_company, name="register_company"),
    path('new-post/',views.new_post,name='new-post'),   
    path("login/", views.login, name="login"),
    path("login_company/", views.login_company, name="login_company"),
    path('logout/',views.logout,name='logout'),
    path('logout/company/',views.logout_company,name='logout_company'),
    path('company_index',views.company_index,name='company_index'),
    path('post_job/<int:pk>/',views.post_job,name='post_job'),
    path('view-job/<int:pk>/',views.view_job,name='view-job'),
    path('show/candidate',views.show_candidate,name='view_candidate'),
    path('view/candidate/<int:pk>/',views.view_candidate,name='view_candidate'),
    path("add_job/<int:pk>/", views.add_job, name="add_job"),
    path('post/edit/<int:pk>/',views.post_edit,name='post_edit'),
    path('post/edit/done/<int:pk>/',views.edit_job_done,name='edit_job_done'),
    path('post/delete/<int:pk>/<int:pk1>/',views.delete_job,name='delete_job'),
    path('show/job/',views.show_job,name='show_job'),
    path('apply/job/',views.apply_job,name='apply_job'),
    path('apply/<int:pk1>/<int:pk2>/',views.apply,name='apply'),
    path('result/<int:pk>/',views.result,name='result'),
    path('mcq/<int:pk>/',views.mcq,name='mcq'),
    path('contact/',views.contact,name='contact'),
    path('company/detail/<int:pk>/',views.company_details,name='company_details')


]