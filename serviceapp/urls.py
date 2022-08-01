from django.urls import path
from .import views


urlpatterns = [
   
    path('', views.home , name ='home'),
    path('SignIn', views.login , name='signin'),
    path('SignUp', views.log , name='sign'),
    path('Contactus', views.cont , name='contact'),
    path('Resturant', views.rest , name='re'),
    path('Homeservice', views.hom , name='ho'),
    path('Plumber', views.plumb , name='pl'),
    path('Otp', views.ot , name='otp'),
    path('Registration', views.reg , name='registration'),
    path('Logout', views.logt , name='logout'),
    path('Quickview<int:myid>', views.quick , name='quickview')
   #path('Addcart', views.cart , name='add')


]