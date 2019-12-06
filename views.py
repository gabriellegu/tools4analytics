# -*- coding: UTF-8 -*-

# import builtins
import json

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.context import RequestContext
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models import Count

from django.views.decorators.csrf import csrf_exempt

import random
from central.models import Squirrel


# Create your views here.
def mapping(request):
    Squirrels = Squirrel.objects.order_by('?')[:50]
    return render_to_response('map.html', {'sightings': Squirrels})


def stats(request):
    all_squirrels = Squirrel.objects.all().count()
    per_adult = (Squirrel.objects.filter(age='Adult').count())/
    (Squirrel.objects.all().count()) * 100
    per_gray = (Squirrel.objects.filter(primaryColor='Gray').count())/
    (Squirrel.objects.all().count()) * 100
    per_running = (Squirrel.objects.filter(running='true').count())/
    (Squirrel.objects.all().count()) * 100
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
    if request.method == "POST":
        print(request.POST)
        print('进入添加界面')
        loc_X = float(request.POST['loc_X'])
        loc_Y = float(request.POST['loc_Y'])
        hectare = request.POST['hectare']
        shift = request.POST['shift']
        date = request.POST['date']
        hectareNum = int(request.POST['hectareNum'])
        uniqueID = hectare + "-" + shift + "-" + date[:4] + "-" + (
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
        print('进入修改界面的GET')

        uniqueID = request.GET.get('uniqueID')
        print('obj', uniqueID)
        # 有可能查询到多个值
        obj = Squirrel.objects.filter(uniqueID=uniqueID)
        if obj:
            # 不管多少个值，只拿去第一个去做修改
            obj=obj[0]
            print(obj)
            return render(request, 'update.html', {'data': obj})
        else:
            return HttpResponse('为检测你输入的uniqueID')
    elif request.method == 'POST':
        print('进入修改界面的POST')
        loc_X = request.POST['loc_X']
        loc_Y = request.POST['loc_Y']
        hectare = request.POST['hectare']
        shift = request.POST['shift']
        date = request.POST['date']
        hectareNum = request.POST['hectareNum']
        uniqueID = request.POST['uniqueID']
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

        # 查询要修改的uniqueID
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
        return HttpResponseRedirect("/sightings")

def query(request):
    limit = 20
    Squirrels = Squirrel.objects.all()
    paginator = Paginator(Squirrels, limit)
    page = request.GET.get('page')
    try:
        Squirrels = paginator.page(page)
    except PageNotAnInteger:
        Squirrels = paginator.page(1)
    except EmptyPage:
        Squirrels = paginator.page(paginator.num_pages)
    return render_to_response('curd.html', {'data': Squirrels})


def queryById(request):
    uniqueID = request.GET['uniqueID'];
    if uniqueID == "":
        return HttpResponseRedirect("/sightings")
    bb = Squirrel.objects.filter(uniqueID=uniqueID)
    return render_to_response('curd.html', {'data': bb})


def showUid(request, uniqueID):
    bb = Squirrel.objects.get(uniqueID=uniqueID)
    return render_to_response('update1.html', {'data': bb})


def delByID(request, uniqueID):
    bb = Squirrel.objects.get(uniqueID=uniqueID)
    bb.delete()
    return HttpResponseRedirect("/sightings")


def delByCode(request, d):
    # if request.method == 'DELETE':
    #     bb=Squirrel.objects.get(uniqueID=uniqueID)
    #     bb.delete()
    #     return HttpResponseRedirect("/sightings")
    # else:
    #     bb=Squirrel.objects.get(uniqueID=uniqueID)
    #     return render_to_response('update1.html',{'data':bb})

    if request.method == "GET":
        pass

    elif request.method == 'POST':
        d = int(d)
        uniqueID = request.body.decode().split('=')
        if uniqueID:
            uniqueID = uniqueID[1]

        print('uniqueID-----', uniqueID)


        # if id==1,代表进行删除动作
        if d == 1:
            # 因为uniqueID不唯一，所以要同时删除多个
            bb = Squirrel.objects.filter(uniqueID=uniqueID)
            print('bb---',bb)
            if bb:
                bb.delete()
                return JsonResponse({'code': 1})
            else:
                print('未查询到')
                # return HttpResponseRedirect("/sightings")
                return JsonResponse({'code': 3})
        elif d == 2:
            return JsonResponse({'code': 2})

data = Squirrel.objects.values()
