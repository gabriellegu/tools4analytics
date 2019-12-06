import json

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.context import RequestContext
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from django.views.decorators.csrf import csrf_exempt

import random
from .models import Squirrel


# Create your views here.
def beginAdd(request):
    if request.method == "POST":
        print(request.POST)
        print('Add')
        loc_X = float(request.POST['loc_X'])
        loc_Y = float(request.POST['loc_Y'])
        hectare = request.POST['hectare']
        shift = request.POST['shift']
        date = request.POST['date']
        hectareNum = int(request.POST['hectareNum'])
        uniqueID = (hectare[1:] if hectare[0]=='0' else hectare) + "-" + shift + "-" + date[:4] + "-" + (
            str(hectareNum) if len(str(hectareNum)) == 2 else "0" + str(hectareNum))
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
    if request.method == 'GET':
        print('Update GET')

        uniqueID = request.GET.get('uniqueID')
        print('obj', uniqueID)
        obj = Squirrel.objects.filter(uniqueID=uniqueID)
        if obj:
            obj=obj[0]
            print(obj)
            return render(request, 'update.html', {'data': obj})


def query(request):
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
    uniqueID = request.GET['uniqueID'];
    if uniqueID == "":
        return HttpResponseRedirect("/sightings")
    bb = Squirrel.objects.filter(uniqueID=uniqueID)
    return render_to_response('sightings.html', {'data': bb})

def fetchpage(request):
    if request.method == "GET":
        pass
    elif request.method == 'POST':
        uniqueID = request.body.decode().split('=')
        if uniqueID:
            uniqueID = uniqueID[1]
        print('uniqueID-----', uniqueID)
        return JsonResponse({'code': 2})

def god_view(request,uniqueID):
    if request.method == 'DELETE':
        bb=Squirrel.objects.get(uniqueID=uniqueID)
        if bb:
            bb.delete() 
            return JsonResponse({'code': 1})
        else:
            print('cannot find the squirrel')
            return JsonResponse({'code': 3})
            
    elif request.method == 'POST':
        loc_X = request.POST['loc_X']
        loc_Y = request.POST['loc_Y']
        hectare = request.POST['hectare']
        shift = request.POST['shift']
        date = request.POST['date']
        hectareNum = request.POST['hectareNum']
        uniqueID = (hectare[1:] if hectare[0]=='0' else hectare) + "-" + shift + "-" + date[:4] + "-" + (
            str(hectareNum) if len(str(hectareNum)) == 2 else "0" + str(hectareNum))
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
        print(st_list)
        for st in st_list:
            st.loc_X = loc_X
            st.loc_Y = loc_Y
            st.uniqueID = hectare + "-" + shift + "-" + date[:4] + "-" + (
            str(hectareNum) if len(str(hectareNum)) == 2 else "0" + str(hectareNum))
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
        return JsonResponse({'code': 2})

datas = Squirrel.objects.values()
