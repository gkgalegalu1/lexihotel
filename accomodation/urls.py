from django.urls import path
from accomodation import views


urlpatterns = [
    path('lexihotel/home1',views.home1, name='home1'),
    path('lexihotel/', views.home, name='home'),
    path('lexihotel/about', views.about, name='about'),
    path('lexihotel/makereservation', views.makereservation, name='makereservation'),
    path('lexihotel/submit_reservation', views.submit_reservation, name='submit_reservation'),
    path('lexihotel/confirm', views.record_payment, name='record_payment'),
    path('lexihotel/rooms', views.rooms, name='rooms'),
    path('lexihotel/login', views.login, name='login'),
    path('lexihotel/signin', views.signin, name='signin'),
    path('lexihotel/logout', views.logout, name='logout'),
    path('lexihotel/register', views.register, name='register'),
    path('lexihotel/register_employee', views.register_employee, name='register_employee'),
    path('lexihotel/check_reservation', views.check_reservation, name='check_reservation'),
    path('lexihotel/pictures', views.pictures, name='pictures'),
]