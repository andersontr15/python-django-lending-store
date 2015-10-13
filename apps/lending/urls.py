from django.conf.urls import patterns, url
from apps.lending import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^lender_login$', views.lender_login, name='lender_login'),
	url(r'^borrower_login$', views.borrower_login, name='borrower_login'),
	url(r'^lender_register$', views.lender_register, name='lender_register'),
	url(r'^borrower_register$', views.borrower_register, name='borrower_register'),
	url(r'^borrower_home$', views.borrower_home, name='borrower_home'),
	url(r'^lender_home$', views.lender_home, name='lender_home'),
	url(r'^lender_logout$', views.lender_logout, name='lender_logout'),
	url(r'^borrower_logout$', views.borrower_logout, name='borrower_logout'),
	url(r'^borrower/(?P<borrower_id>\d+)/lend$', views.lend),
	url(r'^borrower/(?P<borrower_id>\d+)/delete$', views.delete),
	url(r'^borrower_login_page$', views.borrower_login_page, name='borrower_login_page'),
	url(r'^lender_login_page$', views.lender_login_page, name='lender_login_page'),

)