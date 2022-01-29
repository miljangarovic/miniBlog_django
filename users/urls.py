from django.urls import path
from . import views

urlpatterns = [
    path('',views.profiles,name='profiles'),
    # path('profile/<pk>', views.profile, name='profile'),
    path('account/',views.userAccount,name='account'),
    # path('account/edit', views.editAccount, name='account-edit'),
    # path('skill/add',views.createSkill,name='skill-create'),
    # path('skill/update/<pk>',views.updateSkill,name='update-skill'),
    # path('skill/delete/<pk>', views.deleteSkill, name='delete-skill'),
    #
    path('login/',views.loginUser,name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/',views.registerUser,name='register'),
    #
    #
    # path('account/inbox',views.inbox,name='inbox'),
    # path('account/inbox/<pk>',views.viewMessage,name='message'),
    # path('message/create/<pk>', views.createMessage, name='message-create'), #pk u ovom slucaju sluzi da se zna kojem akauntu se poruka prosljedjuje
]

