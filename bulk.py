import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from brand.models import Brand

path = 'C:/slownique/brand1.csv'
print(path)
f = open(path, 'r', encoding='utf-8')
data = []

rdr = csv.reader(f)

for row in rdr:
    name, category, desc, info, image, link = row
    tuple = (name, category, desc, info, image, link)
    data.append(tuple)
f.close()

instances = []
for (name, category, desc, info, image, link) in data:
    instances.append(Brand(name=name, category=category, desc=desc, info=info, image=image, link=link))

Brand.objects.bulk_create(instances)