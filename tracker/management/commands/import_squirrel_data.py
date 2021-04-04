from django.core.management.base import BaseCommand
from tracker.models import squirrel
import csv
import datetime
class Command(BaseCommand):
    help='This command is used for Import squirrel data from csv file'
    def add_arguments(self,parser):
        parser.add_argument('path',type=str)
    def handle(self,*args,**kwargs):
        path = kwargs['path']

        try:
            with open(path,encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for i in reader:
                    s = Squirrels(
                        X=i['X'],
                        Y=i['Y'],
                        Unique_squirrel_id=i['Unique Squirrel ID'],
                        Shift=i['Shift'],
                        Date=datetime.date(int(i['Date'][-4:]),int(i['Date'][:2]),int(i['Date'][2:4])),
                        Age=i['Age'],
                        Primary_Fur_Color=i['Primary Fur Color'].lower(),
                        Location = i['Location'],
                        Specific_location = i['Specific Location'],
                        Running=i['Running'].lower(),
                        Chasing=i['Chasing'].lower(),
                        Climbing=i['Climbing'].lower(),
                        Eating=i['Eating'].upper(),
                        Foraging=i['Foraging'].upper(),
                        Other_activities=i['Other Activities'].lower(),
                        Kuks=i['Kuks'].upper(),
                        Quaas=i['Quaas'].upper(),
                        Moans=i['Moans'].upper(),
                        Tail_flags=i['Tail flags'].upper(),
                        Tail_twitches=i['Tail twitches'].upper(),
                        Approaches=i['Approaches'].upper(),
                        Indifferent=i['Indifferent'].upper(),
                        Runs_from=i['Runs from'].upper(),
                        )
                    s.save()
        except csv.Error as e:
            print(f'there is something wrong with {reader.line_num}')
