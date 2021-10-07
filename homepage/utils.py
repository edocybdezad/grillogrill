import csv
from .models import *

def import_csv(request):
    category=""
    footer=""
    with open('datas/carta.csv',encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['category']} - {row['name']} - {row['description']} - {row['price']}")
            ct = Category(name=c['category'], footer=c['footer'])
            ct.save()
            it = Item(name=i['name'], description=i['description'], price=i['price'], category=ct)
            it.save()            

def import_text(request)
    cates =[]
    items =[]
    with open('datas/vinos.txt',encoding="utf8") as f:
        line = f.readline()
        while line:
            if line[0] == "#":
                if footer:
                    ca['footer']=footer
                    footer=""
                c = line[1:].rstrip('\n')
                ca = {'category': c, 'footer':footer}
                cates.append(ca)             
            elif line[0] == "*":
                footer += line[1:]
            else:
                n = line.rstrip('\n')
                d = f.readline().rstrip('\n')
                p = f.readline().rstrip('\n')
                item = {'name':n, 'description': d, 'price':p, 'category': ca['category']}
                items.append(item)
            line = f.readline()
    for c in cates:
        ct = Category(name=c['category'], footer=c['footer'])
        ct.save()
    for i in items:
        ct = Category.objects.filter(name=i['category']).first()
        it = Item(name=i['name'], description=i['description'], price=i['price'], category=ct)
        it.save()