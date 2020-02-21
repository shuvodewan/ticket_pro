"""ticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#login
from django.contrib.auth.views import LoginView,LogoutView

#view
from ticketapp import views

#load media file
from django.conf import settings
from django.conf.urls.static import static



class LoginTestView(LoginView):
  
    
    def get_context_data(self, **kwargs):
        con=super(LoginTestView,self).get_context_data(**kwargs)
        #context = super(LoginTestView, self).context
        #setting.LOGIN_REDIRECT_URL=con
        
        for d in con:
            if d=="next":
                if len(con[d])==0:
                    pass
                else:
                    settings.LOGIN_REDIRECT_URL=con[d] 
        return con

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('account/',include('account.urls'),name='account'),
    path('ticket/',include("ticketapp.urls"),name="ticket"),
    path('login/',LoginTestView.as_view(),name="login"),
    path('logout',LogoutView.as_view(),name="logout"),


]
urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
