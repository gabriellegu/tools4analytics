import csv
from django.core.management.base import BaseCommand, CommandError
from central.models import Squirrel


class Command(BaseCommand):
    help = 'Load a csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt', encoding='UTF-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                new_squirrel = Squirrel(loc_X=row['X'], loc_Y=row['Y'], uniqueID=row['Unique Squirrel ID'],
                                        hectare=row['Hectare'], shift=row['Shift'], date=row['Date'],
                                        hectareNum=row['Hectare Squirrel Number'], age=row['Age'],
                                        primaryColor=row['Primary Fur Color'],
                                        highlightColor=row['Highlight Fur Color'],
                                        combiColor=row['Combination of Primary and Highlight Color'],
                                        colorNotes=row['Color notes'], location=row['Location'],
                                        measurement=row['Above Ground Sighter Measurement'],
                                        specificLocation=row['Specific Location'], running=row['Running'],
                                        chasing=row['Chasing'], climbing=row['Climbing'], eating=row['Eating'],
                                        foraging=row['Foraging'], otherActivities=row['Other Activities'],
                                        kuks=row['Kuks'], quaas=row['Quaas'], moans=row['Moans'],
                                        tailFlags=row['Tail flags'], tailTwitches=row['Tail twitches'],
                                        approaches=row['Approaches'], indifferent=row['Indifferent'],
                                        runsFrom=row['Runs from'], otherInteractions=row['Other Interactions'],
                                        latLong=row['Lat/Long'], zipcodes=row['Zip Codes'],
                                        communityDistricts=row['Community Districts'],
                                        boroughBoundaries=row['Borough Boundaries'],
                                        cityCouncilDistricts=row['City Council Districts'],
                                        policePrecincts=row['Police Precincts'])
                new_squirrel.save()
