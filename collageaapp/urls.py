from django.urls import path,include
from. import views

urlpatterns = [
    path('',views.admin,name='admin'),
    path('signup',views.signup,name='signup'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('addcoursedb',views.addcoursedb,name='addcoursedb'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('addstudentdb',views.addstudentdb,name='addstudentdb'),
    path('showstudents',views.showstudents,name='showstudents'),
    path('adminnhomepage',views.adminnhomepage,name='adminnhomepage'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('edit_db/<int:pk>',views.edit_db,name='edit_db'),
    path('logout',views.logout,name='logout'),
    path('teacherprofilehome',views.teacherprofilehome,name='teacherprofilehome'),
    path('addsignup',views.addsignup,name='addsignup'),
    path('loginn',views.loginn,name='loginn'),
    path('edittch',views.edittch,name='edittch'),
    path('edittchdb/<int:pk>',views.edittchdb,name='edittchdb'),
    path('dlttch/<int:pk>',views.dlttch,name='dlttch'),
    path('viewpr',views.viewpr,name='viewpr'),
    path('showteacher',views.showteacher,name='showteacher'),


]