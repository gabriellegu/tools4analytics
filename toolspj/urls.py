"""toolspj path Configuration

The `pathpatterns` list routes paths to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a path to pathpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a path to pathpatterns:  path('', Home.as_view(), name='home')
Including another pathconf
    1. Import the include() function: from django.paths import include, path
    2. Add a path to pathpatterns:  path('blog/', include('blog.paths'))
"""
# from django.contrib import admin
# from django.paths import include, path

# pathpatterns = [
#    path('map/',include('central.paths')),
#    path('admin/', admin.site.paths),
# ]
from django.urls import include, path, re_path
from django.contrib import admin
from central.views import beginAdd, updateOnReq, mapping, stats, query, queryById, showUid, delByID, delByCode

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # sightings
    path('sightings', query, name='query'),
    # add
    path('sightings/add', beginAdd, name='beginAdd'),
    path('add', updateOnReq, name='updateOnReq'),
    # query
    path('query', queryById, name='query'),
    # map
    path('map', mapping, name='mapping'),
    # stats
    path('sightings/stats', stats, name='stats'),
    # path('yanzheng',yanzheng),
    # 删除用户根据id
    # path('^sightings/(.+)/<slug:uniqueID>/$',god_view),
    re_path('sightings/d(\d+)', delByCode),
    # 更新的方法，根据id
]
