import json
import os
import random
import string
from os.path import basename

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.pos.models import *
from core.security.models import *


def insert_data():
    numbers = list(string.digits)

    company = Company()
    company.business_name = 'VELEZ AGUIRRE SIMON EDUARDO'
    company.tradename = 'PUNTOHELP'
    company.ruc = '0921637781001'
    company.establishment_code = '003'
    company.issuing_point_code = '003'
    company.special_taxpayer = '000'
    company.main_address = '5 DE OCTUBRE Y 10 DE AGOSTO NARANJITO,GUAYAS'
    company.establishment_address = '5 DE OCTUBRE Y 10 DE AGOSTO NARANJITO,GUAYAS'
    company.mobile = '0996555528'
    company.phone = '2977557'
    company.email = 'puntohelpsa@gmail.com'
    company.website = 'https://puntohelp.com'
    company.description = 'VENTA AL POR MAYOR DE COMPUTADORAS Y EQUIPO PERIFÉRICO.'
    company.iva = 12.00
    company.electronic_signature_key = '224426rajansn'
    company.email_host_user = 'factorapos19@gmail.com'
    company.email_host_password = 'nbkqthnfkysfuudn'
    image_path = f'{settings.BASE_DIR}{settings.STATIC_URL}img/default/logo.png'
    company.image.save(basename(image_path), content=File(open(image_path, 'rb')), save=False)
    electronic_signature_path = f'{settings.BASE_DIR}{settings.STATIC_URL}files/firma.p12'
    company.electronic_signature.save(basename(electronic_signature_path), content=File(open(electronic_signature_path, 'rb')), save=False)
    company.save()

    for item in VOUCHER_TYPE:
        current_number = f"{int(''.join(random.choices(numbers, k=7))):09d}"
        if item[0] == VOUCHER_TYPE[-1][0]:
            current_number = '000000001'
        Receipt.objects.create(name=item[1], code=item[0], start_number='000000000', end_number='999999999', current_number=current_number)

    with open(f'{settings.BASE_DIR}/deploy/json/products.json', encoding='utf8') as json_file:
        for item in json.load(json_file):
            product = Product()
            product.name = item['name']
            product.code = item['code']
            product.category = Category.objects.get_or_create(name=item['category'])[0]
            product.price = float(item['price'])
            product.pvp = float(item['pvp'])
            product.save()
            print(f'record inserted product {product.id}')

    category = Category.objects.create(name='SERVICIOS')
    Product.objects.create(name='FORMATEO DE COMPUTADORAS', category=category, inventoried=False, with_tax=False, pvp=15.00, code='FORMATEO85451')

    with open(f'{settings.BASE_DIR}/deploy/json/customers.json', encoding='utf8') as json_file:
        data = json.load(json_file)
        for item in data[0:20]:
            provider = Provider()
            provider.name = item['company'].upper()
            provider.ruc = ''.join(random.choices(numbers, k=13))
            provider.mobile = ''.join(random.choices(numbers, k=10))
            provider.address = item['country']
            provider.email = item['email']
            provider.save()
            print(f'record inserted provider {provider.id}')

    provider_id = list(Provider.objects.all().values_list('id', flat=True))
    product_id = list(Product.objects.filter(inventoried=True).values_list('id', flat=True))
    for i in range(1, 10):
        purchase = Purchase()
        purchase.number = ''.join(random.choices(numbers, k=8))
        purchase.provider_id = random.choice(provider_id)
        purchase.save()
        print(f'record inserted purchase {purchase.id}')

        for d in range(1, 5):
            detail = PurchaseDetail()
            detail.purchase_id = purchase.id
            detail.product_id = random.choice(product_id)
            while purchase.purchasedetail_set.filter(product_id=detail.product_id).exists():
                detail.product_id = random.choice(product_id)
            detail.cant = random.randint(1, 50)
            detail.price = detail.product.pvp
            detail.subtotal = float(detail.price) * detail.cant
            detail.save()
            detail.product.stock += detail.cant
            detail.product.save()
        purchase.calculate_invoice()

    user = User(names='Consumidor Final', email='davilawilliam94@gmail.com', username='9999999999999')
    user.set_password(user.username)
    user.save()
    user.groups.add(Group.objects.get(pk=settings.GROUPS.get('client')))
    client = Client()
    client.user = user
    client.dni = user.username
    client.birthdate = date(1994, 10, 19)
    client.mobile = '9999999999'
    client.address = 'Milagro, cdla. Paquisha'
    client.identification_type = IDENTIFICATION_TYPE[3][0]
    client.send_email_invoice = False
    client.save()

    user = User(names='William Jair Dávila Vargas', email='wdavilav1994@gmail.com', username='0928363993')
    user.set_password(user.username)
    user.save()
    user.groups.add(Group.objects.get(pk=settings.GROUPS.get('client')))
    client = Client()
    client.user = user
    client.dni = user.username
    client.birthdate = date(1994, 10, 19)
    client.mobile = '0979014551'
    client.address = 'Milagro, cdla. Paquisha'
    client.save()

    user = User(names='LIBRIMUNDI LIBRERÍA INTERNACIONAL S.A.', email='williamjairdavilavargas@gmail.com', username='1791411293001')
    user.set_password(user.username)
    user.save()
    user.groups.add(Group.objects.get(pk=settings.GROUPS.get('client')))
    client = Client()
    client.user = user
    client.dni = user.username
    client.birthdate = date(1994, 10, 19)
    client.mobile = '0979014552'
    client.address = 'Milagro, cdla. Paquisha'
    client.identification_type = IDENTIFICATION_TYPE[1][0]
    client.save()


insert_data()
