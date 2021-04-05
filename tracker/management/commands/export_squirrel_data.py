import csv

from django.core.management.base import BaseCommand, CommandError
from tracker.models import squirrel

class Command(BaseCommand):
    help='A command that can be used to export the data in CSV format'

    def add_arguments(self,parser):
        parser.add_argument('args',type=str,nargs='*')

    def handle(self,*args,**kwargs):
        path = args[0]
        fields = squirrel._meta.fields
        with open(path,'w') as f:
            writer = csv.writer(f)
            for i in squirrel.objects.all():
                row = [getattr(i,field.name) for field in fields]
                writer.writerow(row)
            f.close()
