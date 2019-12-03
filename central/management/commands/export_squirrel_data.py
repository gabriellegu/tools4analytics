import csv
from django.core.management.base import BaseCommand, CommandError
from central.models import Squirrel


class Command(BaseCommand):
    help = 'Load a csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        csvFile = open(path, "w")

        #get all the attributes in the model
        fileheader = ['X','Y','Unique Squirrel ID','Hectare','Shift','Date','Hectare Squirrel Number','Age','Primary Fur Color',
                    'Highlight Fur Color','Combination of Primary and Highlight Color','Color notes','Location',
                    'Above Ground Sighter Measurement','Specific Location','Running','Chasing','Climbing','Eating','Foraging',
                    'Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent',
                    'Runs from','Other Interactions','Lat/Long','Zip Codes','Community Districts','Borough Boundaries',
                    'City Council Districts','Police Precincts']
        dict_writer = csv.DictWriter(csvFile, fileheader)
        dict_writer.writeheader()
        #get data
        squirrels_list = Squirrel.objects.distinct()

        for obj in squirrels_list:
            row_list = [obj.loc_X, obj.loc_Y, obj.uniqueID, obj.hectare, obj.shift, obj.date, obj.hectareNum, obj.age,
                        obj.primaryColor, obj.highlightColor, obj.combiColor, obj.colorNotes,obj.location,obj.measurement,
                        obj.specificLocation,obj.running,obj.chasing,obj.climbing,obj.eating,obj.foraging,obj.otherActivities,
                        obj.kuks,obj.quaas,obj.moans,obj.tailFlags,obj.tailTwitches,obj.approaches,obj.indifferent,obj.runsFrom,
                        obj.otherInteractions,obj.latLong,obj.zipcodes,obj.communityDistricts,obj.boroughBoundaries,obj.cityCouncilDistricts,
                        obj.policePrecincts]
            row_file=dict(zip(fileheader,row_list))
            #write data
            dict_writer.writerow(row_file)

        csvFile.close()
