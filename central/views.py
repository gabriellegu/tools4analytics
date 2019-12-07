import json

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.context import RequestContext
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count

import random
from central.models import Squirrel


# Create your views here.
def mapping(request):
    """Using this function,
    user can get 50 random squirrel spots from the Squirrel database.
    method: GET
    format: 'map.html'
    """
    Squirrels = Squirrel.objects.order_by('?')[:50]
    return render_to_response('map.html', {'sightings': Squirrels})


def stats(request):
    """Using this function,
    user can get stats on 5 features of squirrels near Central Park
    from the Squirrel database.
    method: GET
    """
    all_squirrels = Squirrel.objects.all().count()
    per_adult = (Squirrel.objects.filter(age='Adult').count()) / (Squirrel.objects.all().count()) * 100
    per_gray = (Squirrel.objects.filter(primaryColor='Gray').count()) / (Squirrel.objects.all().count()) * 100
    per_running = (Squirrel.objects.filter(running='true').count()) / (Squirrel.objects.all().count()) * 100
    num_moans = Squirrel.objects.filter(moans='true').count()
    num_approaches = Squirrel.objects.filter(approaches='true').count()
    bb = {'all_squirrels': all_squirrels,
          'per_adult': per_adult,
          'per_gray': per_gray,
          'per_running': per_running,
          'num_moans': num_moans,
          'num_approaches': num_approaches}
    return render_to_response('stats.html', {'bb': bb})


def beginAdd(request):
    """Function for adding a new sighting

    Args:
        request: request

    Returns:
        HttpResponseRedirect("/sightings") for POST,
        render(request, 'add.html') otherwise

    """
    if request.method == "POST":
        print(request.POST)
        print('Add')
        loc_X = float(request.POST['loc_X'])
        loc_Y = float(request.POST['loc_Y'])
        hectare = request.POST['hectare']
        shift = request.POST['shift']
        date = request.POST['date']
        hectareNum = int(request.POST['hectareNum'])
        uniqueID = (hectare[1:] if hectare[0] == '0' else hectare) \
            + "-" + shift + "-" + date[:4] + "-" \
            + (str(hectareNum) if len(str(hectareNum)) == 2
                else "0" + str(hectareNum))
        age = request.POST['age']
        primaryColor = request.POST['primaryColor']
        highlightColor = request.POST['highlightColor']
        combiColor = request.POST['combiColor']
        colorNotes = request.POST['colorNotes']
        location = request.POST['location']
        measurement = request.POST['measurement']
        specificLocation = request.POST['specificLocation']
        running = request.POST['running']
        chasing = request.POST['chasing']
        climbing = request.POST['climbing']
        eating = request.POST['eating']
        foraging = request.POST['foraging']
        otherActivities = request.POST['otherActivities']
        kuks = request.POST['kuks']
        quaas = request.POST['quaas']
        moans = request.POST['moans']
        tailFlags = request.POST['tailFlags']
        tailTwitches = request.POST['tailTwitches']
        approaches = request.POST['approaches']
        indifferent = request.POST['indifferent']
        runsFrom = request.POST['runsFrom']
        otherInteractions = ''
        latLong = 'POINT ('+request.POST['loc_X']+' '+request.POST['loc_Y']+')'
        zipcodes = ''
        communityDistricts = 19
        boroughBoundaries = 4
        cityCouncilDistricts = 19
        policePrecincts = 13
        print(uniqueID)
        st = Squirrel()
        st.loc_X = loc_X
        st.loc_Y = loc_Y
        st.uniqueID = uniqueID
        st.hectare = hectare
        st.shift = shift
        st.date = date
        st.hectareNum = hectareNum
        st.age = age
        st.primaryColor = primaryColor
        st.highlightColor = highlightColor
        st.combiColor = combiColor
        st.colorNotes = colorNotes
        st.location = location
        st.measurement = measurement
        st.specificLocation = specificLocation
        st.running = running
        st.chasing = chasing
        st.climbing = climbing
        st.eating = eating
        st.foraging = foraging
        st.otherActivities = otherActivities
        st.kuks = kuks
        st.quaas = quaas
        st.moans = moans
        st.tailFlags = tailFlags
        st.tailTwitches = tailTwitches
        st.approaches = approaches
        st.indifferent = indifferent
        st.runsFrom = runsFrom
        st.otherInteractions = otherInteractions
        st.latLong = latLong
        st.zipcodes = zipcodes
        st.communityDistricts = communityDistricts
        st.boroughBoundaries = boroughBoundaries
        st.cityCouncilDistricts = cityCouncilDistricts
        st.policePrecincts = policePrecincts
        st.save()
        return HttpResponseRedirect("/sightings")
    else:
        return render(request, 'add.html')


# @csrf_exempt
def updateOnReq(request):
    """Function for updating a sighting

    Args:
        request: request

    Returns:
        render(request, 'update.html', {'data': obj})

    """
    if request.method == 'GET':
        print('Update GET')

        uniqueID = request.GET.get('uniqueID')
        print('obj', uniqueID)
        obj = Squirrel.objects.filter(uniqueID=uniqueID)
        if obj:
            obj = obj[0]
            print(obj)
            return render(request, 'update.html', {'data': obj})


def query(request):
    """Function for showing all sightings

    Args:
        request: request

    Returns:
        render_to_response('sightings.html', {'data': Squirrels})

    """
    limit = 100
    Squirrels = Squirrel.objects.all()
    paginator = Paginator(Squirrels, limit)
    page = request.GET.get('page')
    try:
        Squirrels = paginator.page(page)
    except PageNotAnInteger:
        Squirrels = paginator.page(1)
    except EmptyPage:
        Squirrels = paginator.page(paginator.num_pages)
    return render_to_response('sightings.html', {'data': Squirrels})


def queryById(request):
    """Function for searching a sighting with unique ID

    Args:
        request: request

    Returns:
        render_to_response('sightings.html', {'data': bb})

    """
    uniqueID = request.GET['uniqueID']
    if uniqueID == "":
        return HttpResponseRedirect("/sightings")
    bb = Squirrel.objects.filter(uniqueID=uniqueID)
    return render_to_response('sightings.html', {'data': bb})


def fetchpage(request):
    """Function for getting the page for updating

    Args:
        request: request

    Returns:
        JsonResponse({'code': 2})

    """
    if request.method == "GET":
        pass
    elif request.method == 'POST':
        uniqueID = request.body.decode().split('=')
        if uniqueID:
            uniqueID = uniqueID[1]
        print('uniqueID-----', uniqueID)
        return JsonResponse({'code': 2})


def god_view(request, uniqueID):
    """Function for directing to update/delete

    Args:
        request: request,uniqueID

    Returns:
        JsonResponse({'code': 2}) if POST
        JsonResponse({'code': 1}) if DELETE
        JsonResponse({'code': 3}) if can't find squirrel

    """
    if request.method == 'DELETE':
        bb = Squirrel.objects.get(uniqueID=uniqueID)
        if bb:
            bb.delete()
            return JsonResponse({'code': 1})
        else:
            print('cannot find Squirrel')
            return JsonResponse({'code': 3})
    elif request.method == 'POST':
        tempID = request.POST['tempID']
        loc_X = request.POST['loc_X']
        loc_Y = request.POST['loc_Y']
        hectare = request.POST['hectare']
        shift = request.POST['shift']
        date = request.POST['date']
        hectareNum = request.POST['hectareNum']
        age = request.POST['age']
        primaryColor = request.POST['primaryColor']
        highlightColor = request.POST['highlightColor']
        combiColor = request.POST['combiColor']
        colorNotes = request.POST['colorNotes']
        location = request.POST['location']
        measurement = request.POST['measurement']
        specificLocation = request.POST['specificLocation']
        running = request.POST['running']
        chasing = request.POST['chasing']
        climbing = request.POST['climbing']
        eating = request.POST['eating']
        foraging = request.POST['foraging']
        otherActivities = request.POST['otherActivities']
        kuks = request.POST['kuks']
        quaas = request.POST['quaas']
        moans = request.POST['moans']
        tailFlags = request.POST['tailFlags']
        tailTwitches = request.POST['tailTwitches']
        approaches = request.POST['approaches']
        indifferent = request.POST['indifferent']
        runsFrom = request.POST['runsFrom']
        otherInteractions = request.POST['otherInteractions']
        latLong = 'POINT ('+request.POST['loc_X']+' '+request.POST['loc_Y']+')'
        zipcodes = ''
        communityDistricts = 19
        boroughBoundaries = 4
        cityCouncilDistricts = 19
        policePrecincts = 13

        st_list = Squirrel.objects.filter(uniqueID=uniqueID)
        if st_list:
            for st in st_list:
                st.loc_X = loc_X
                st.loc_Y = loc_Y
                st.uniqueID = uniqueID
                st.hectare = hectare
                st.shift = shift
                st.date = date
                st.hectareNum = hectareNum
                st.age = age
                st.primaryColor = primaryColor
                st.highlightColor = highlightColor
                st.combiColor = combiColor
                st.colorNotes = colorNotes
                st.location = location
                st.measurement = measurement
                st.specificLocation = specificLocation
                st.running = running
                st.chasing = chasing
                st.climbing = climbing
                st.eating = eating
                st.foraging = foraging
                st.otherActivities = otherActivities
                st.kuks = kuks
                st.quaas = quaas
                st.moans = moans
                st.tailFlags = tailFlags
                st.tailTwitches = tailTwitches
                st.approaches = approaches
                st.indifferent = indifferent
                st.runsFrom = runsFrom
                st.otherInteractions = otherInteractions
                st.latLong = latLong
                st.zipcodes = zipcodes
                st.communityDistricts = communityDistricts
                st.boroughBoundaries = boroughBoundaries
                st.cityCouncilDistricts = cityCouncilDistricts
                st.policePrecincts = policePrecincts
                st.save()
        else:
            st = Squirrel()
            st.loc_X = loc_X
            st.loc_Y = loc_Y
            st.uniqueID = uniqueID
            st.hectare = hectare
            st.shift = shift
            st.date = date
            st.hectareNum = hectareNum
            st.age = age
            st.primaryColor = primaryColor
            st.highlightColor = highlightColor
            st.combiColor = combiColor
            st.colorNotes = colorNotes
            st.location = location
            st.measurement = measurement
            st.specificLocation = specificLocation
            st.running = running
            st.chasing = chasing
            st.climbing = climbing
            st.eating = eating
            st.foraging = foraging
            st.otherActivities = otherActivities
            st.kuks = kuks
            st.quaas = quaas
            st.moans = moans
            st.tailFlags = tailFlags
            st.tailTwitches = tailTwitches
            st.approaches = approaches
            st.indifferent = indifferent
            st.runsFrom = runsFrom
            st.otherInteractions = otherInteractions
            st.latLong = latLong
            st.zipcodes = zipcodes
            st.communityDistricts = communityDistricts
            st.boroughBoundaries = boroughBoundaries
            st.cityCouncilDistricts = cityCouncilDistricts
            st.policePrecincts = policePrecincts
            st.save()
            bb = Squirrel.objects.get(uniqueID=tempID)
            if bb:
                bb.delete()
        return JsonResponse({'code': 2})

datas = Squirrel.objects.values()
