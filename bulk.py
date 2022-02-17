import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from brand.models import Brand

path = 'C:/slownique/brand7.csv'
print(path)
f = open(path, 'r', encoding='cp949')
data = []

rdr = csv.reader(f)

for row in rdr:
    name, category_id, desc, info, image, link = row
    tuple = (name, category_id, desc, info, image, link)
    data.append(tuple)
f.close()

instances = []
for (name, category_id, desc, info, image, link) in data:
    instances.append(Brand(name=name, category_id=category_id, desc=desc, info=info, image=image, link=link))

Brand.objects.bulk_create(instances)


