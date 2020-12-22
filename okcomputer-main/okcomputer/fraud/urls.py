from django.urls import path
from . import views

app_name = 'fraud'

urlpatterns = [
    path('register/',views.register, name = 'register'),
    path('login/',views.user_login, name = 'login'),
    path('logout/',views.user_logout, name = 'logout'),
    path('landing/',views.landing, name = 'landing'),
    path('check/',views.Create_Transaction.as_view(),name = 'check'),
    path('result/',views.result,name = 'result'),
    path('transactionlist/',views.TransactionListView.as_view(),name='transaction_list'),
    #path(r'^transaction/(?P<pk>\d+)$',views.TransactionDetailView.as_view(),name='transaction_detail'),
]
