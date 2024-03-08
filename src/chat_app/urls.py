
from chat.views import Main

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # main view where user lands
    path('', Main.as_view(), name = 'main-view'),

    # chat app views
    path('chat/', include('chat.urls')),

    #account views
    path('account/', include('accounts.urls'))

]
