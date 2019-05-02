from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/ques/', include("quest.urls")),
    re_path(r'^.*', include("start.urls"))
]

#urlpatterns = [re_path(r'^.*', include("start.urls"))]
