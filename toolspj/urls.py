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

from django.urls import include, path, re_path
from django.contrib import admin
from central.views import mapping, stats, god_view
from central.views import beginAdd, updateOnReq, query, queryById, fetchpage

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # sightings
    path('sightings', query, name='Show all sightings'),
    # add
    path('sightings/add', beginAdd, name='Add'),
    # render to update.html
    path('update', updateOnReq, name='Render to update.html'),
    # query by specific id
    path('query', queryById, name='Query by specific id'),
    # return jsonresponse for ajax on submitting the update form
    path('sightings/updatetemp', fetchpage),
    # delete and update logics
    path('sightings/<slug:uniqueID>/', god_view),
    # map
    path('map', mapping, name='mapping'),
    # stats
    path('sightings/stats', stats, name='stats'),
]
