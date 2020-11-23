import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load
from unesco.models import Site,Category,State,Region,Iso

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()


    for row in reader:
        print(row)
        try:
            y = int(row[3])
        except:
            y = None

        try:
            lon = float(row[4])
        except:
            lon = None

        try:
            lat = float(row[5])
        except:
            lat = None

        try:
            area = float(row[6])
        except:
            area = None

        c, created = Category.objects.get_or_create(name=row[7])
        st, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])
        s = Site.objects.get_or_create(
            name=row[0], description=row[1], justification=row[2],
            year=y, longitude=lon, latitude=lat, area_hectares=area,
            states = st, category = c, region = r, iso = i
        )
        # s.save()
