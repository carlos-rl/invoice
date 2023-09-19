import os
import string
from os.path import basename

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.security.models import *
from django.contrib.auth.models import Permission
from core.pos.models import *

numbers = list(string.digits)

dashboard = Dashboard()
dashboard.name = 'FACTORA POS'
dashboard.author = 'William Jair Dávila Vargas'
dashboard.icon = 'fas fa-shopping-cart'
dashboard.layout = 1
dashboard.navbar = 'navbar-dark navbar-navy'
dashboard.sidebar = 'sidebar-dark-navy'
image_path = f'{settings.BASE_DIR}{settings.STATIC_URL}img/default/logo.png'
dashboard.image.save(basename(image_path), content=File(open(image_path, 'rb')), save=False)
dashboard.save()

moduletype = ModuleType()
moduletype.name = 'Seguridad'
moduletype.icon = 'fas fa-lock'
moduletype.save()
print(f'insertado {moduletype.name}')

module = Module()
module.module_type_id = 1
module.name = 'Tipos de Módulos'
module.url = '/security/module/type/'
module.icon = 'fas fa-door-open'
module.description = 'Permite administrar los tipos de módulos del sistema'
module.save()
for i in Permission.objects.filter(content_type__model=ModuleType._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 1
module.name = 'Módulos'
module.url = '/security/module/'
module.icon = 'fas fa-th-large'
module.description = 'Permite administrar los módulos del sistema'
module.save()
for i in Permission.objects.filter(content_type__model=Module._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 1
module.name = 'Grupos'
module.url = '/security/group/'
module.icon = 'fas fa-users'
module.description = 'Permite administrar los grupos de usuarios del sistema'
module.save()
for i in Permission.objects.filter(content_type__model=Group._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 1
module.name = 'Respaldos'
module.url = '/security/database/backups/'
module.icon = 'fas fa-database'
module.description = 'Permite administrar los respaldos de base de datos'
module.save()
for i in Permission.objects.filter(content_type__model=DatabaseBackups._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 1
module.name = 'Conf. Dashboard'
module.url = '/security/dashboard/update/'
module.icon = 'fas fa-tools'
module.description = 'Permite configurar los datos de la plantilla'
module.save()
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 1
module.name = 'Accesos'
module.url = '/security/user/access/'
module.icon = 'fas fa-user-secret'
module.description = 'Permite administrar los accesos de los usuarios'
module.save()
for i in Permission.objects.filter(content_type__model=UserAccess._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 1
module.name = 'Usuarios'
module.url = '/user/'
module.icon = 'fas fa-user'
module.description = 'Permite administrar a los administradores del sistema'
module.save()
for i in Permission.objects.filter(content_type__model=User._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

moduletype = ModuleType()
moduletype.name = 'Bodega'
moduletype.icon = 'fas fa-boxes'
moduletype.save()
print(f'insertado {moduletype.name}')

module = Module()
module.module_type_id = 2
module.name = 'Proveedores'
module.url = '/pos/provider/'
module.icon = 'fas fa-truck'
module.description = 'Permite administrar a los proveedores de las compras'
module.save()
for i in Permission.objects.filter(content_type__model=Provider._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 2
module.name = 'Categorías'
module.url = '/pos/category/'
module.icon = 'fas fa-truck-loading'
module.description = 'Permite administrar las categorías de los productos'
module.save()
for i in Permission.objects.filter(content_type__model=Category._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 2
module.name = 'Productos'
module.url = '/pos/product/'
module.icon = 'fas fa-box'
module.description = 'Permite administrar los productos del sistema'
module.save()
for i in Permission.objects.filter(content_type__model=Product._meta.label.split('.')[1].lower()).exclude(codename='adjust_product_stock'):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 2
module.name = 'Compras'
module.url = '/pos/purchase/'
module.icon = 'fas fa-dolly-flatbed'
module.description = 'Permite administrar las compras de los productos'
module.save()
for i in Permission.objects.filter(content_type__model=Purchase._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 2
module.name = 'Ajuste de Stock'
module.url = '/pos/product/stock/adjustment/'
module.icon = 'fas fa-sliders-h'
module.description = 'Permite administrar los ajustes de stock de productos'
module.save()
module.permissions.add(Permission.objects.get(codename='adjust_product_stock'))
print(f'insertado {module.name}')

moduletype = ModuleType()
moduletype.name = 'Administrativo'
moduletype.icon = 'fas fa-hand-holding-usd'
moduletype.save()
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 3
module.name = 'Tipos de Gastos'
module.url = '/pos/type/expense/'
module.icon = 'fas fa-comments-dollar'
module.description = 'Permite administrar los tipos de gastos'
module.save()
for i in Permission.objects.filter(content_type__model=TypeExpense._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 3
module.name = 'Gastos'
module.url = '/pos/expenses/'
module.icon = 'fas fa-file-invoice-dollar'
module.description = 'Permite administrar los gastos de la compañia'
module.save()
for i in Permission.objects.filter(content_type__model=Expenses._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 3
module.name = 'Cuentas por cobrar'
module.url = '/pos/ctas/collect/'
module.icon = 'fas fa-funnel-dollar'
module.description = 'Permite administrar las cuentas por cobrar de los clientes'
module.save()
for i in Permission.objects.filter(content_type__model=CtasCollect._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 3
module.name = 'Cuentas por pagar'
module.url = '/pos/debts/pay/'
module.icon = 'fas fa-money-check-alt'
module.description = 'Permite administrar las cuentas por pagar de los proveedores'
module.save()
for i in Permission.objects.filter(content_type__model=DebtsPay._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

moduletype = ModuleType()
moduletype.name = 'Facturación'
moduletype.icon = 'fas fa-calculator'
moduletype.save()
print(f'insertado {moduletype.name}')

module = Module()
module.module_type_id = 4
module.name = 'T. de Comprobantes'
module.url = '/pos/receipt/'
module.icon = 'fas fa-user-friends'
module.description = 'Permite administrar los tipos de comprobantes para la facturación'
module.save()
for i in Permission.objects.filter(content_type__model=Receipt._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 4
module.name = 'Clientes'
module.url = '/pos/client/'
module.icon = 'fas fa-user-friends'
module.description = 'Permite administrar los clientes del sistema'
module.save()
for i in Permission.objects.filter(content_type__model=Client._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 4
module.name = 'Ventas'
module.url = '/pos/sale/admin/'
module.icon = 'fas fa-shopping-cart'
module.description = 'Permite administrar las ventas de los productos'
module.save()
for i in Permission.objects.filter(content_type__model=Sale._meta.label.split('.')[1].lower()).exclude(codename='view_sale_client'):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 4
module.name = 'Notas de Credito'
module.url = '/pos/credit/note/admin/'
module.icon = 'fa-solid fa-boxes-packing'
module.description = 'Permite administrar las notas de creditos de las ventas'
module.save()
for i in Permission.objects.filter(content_type__model=CreditNote._meta.label.split('.')[1].lower()).exclude(codename='view_credit_note_client'):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.name = 'Ventas'
module.url = '/pos/sale/client/'
module.icon = 'fas fa-shopping-cart'
module.description = 'Permite administrar las ventas de los productos'
module.save()
module.permissions.add(Permission.objects.get(codename='view_sale_client'))
print(f'insertado {module.name}')

module = Module()
module.name = 'Notas de Credito'
module.url = '/pos/credit/note/client/'
module.icon = 'fa-solid fa-boxes-packing'
module.description = 'Permite administrar las notas de credito de las ventas'
module.save()
module.permissions.add(Permission.objects.get(codename='view_credit_note_client'))
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 4
module.name = 'Promociones'
module.url = '/pos/promotions/'
module.icon = 'far fa-calendar-check'
module.description = 'Permite administrar las promociones de los productos'
module.save()
for i in Permission.objects.filter(content_type__model=Promotions._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 4
module.name = 'Errores de Comprob.'
module.url = '/pos/voucher/errors/'
module.icon = 'fas fa-file-archive'
module.description = 'Permite administrar los errores de los comprobantes de las facturas'
module.save()
for i in Permission.objects.filter(content_type__model=VoucherErrors._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

moduletype = ModuleType()
moduletype.name = 'Reportes'
moduletype.icon = 'fas fa-chart-pie'
moduletype.save()
print(f'insertado {moduletype.name}')

module = Module()
module.module_type_id = 5
module.name = 'Ventas'
module.url = '/reports/sale/'
module.icon = 'fas fa-chart-bar'
module.description = 'Permite ver los reportes de las ventas'
module.save()
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 5
module.name = 'Compras'
module.url = '/reports/purchase/'
module.icon = 'fas fa-chart-bar'
module.description = 'Permite ver los reportes de las compras'
module.save()
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 5
module.name = 'Gastos'
module.url = '/reports/expenses/'
module.icon = 'fas fa-chart-bar'
module.description = 'Permite ver los reportes de los gastos'
module.save()
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 5
module.name = 'Cuentas por Pagar'
module.url = '/reports/debts/pay/'
module.icon = 'fas fa-chart-bar'
module.description = 'Permite ver los reportes de las cuentas por pagar'
module.save()
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 5
module.name = 'Cuentas por Cobrar'
module.url = '/reports/ctas/collect/'
module.icon = 'fas fa-chart-bar'
module.description = 'Permite ver los reportes de las cuentas por cobrar'
module.save()
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 5
module.name = 'Resultados'
module.url = '/reports/results/'
module.icon = 'fas fa-chart-bar'
module.description = 'Permite ver los reportes de perdidas y ganancias'
module.save()
print(f'insertado {module.name}')

module = Module()
module.module_type_id = 5
module.name = 'Ganancias'
module.url = '/reports/earnings/'
module.icon = 'fas fa-chart-bar'
module.description = 'Permite ver los reportes de las ganancias'
module.save()
print(f'insertado {module.name}')

module = Module()
module.name = 'Cambiar password'
module.url = '/user/update/password/'
module.icon = 'fas fa-key'
module.description = 'Permite cambiar tu password de tu cuenta'
module.save()
print(f'insertado {module.name}')

module = Module()
module.name = 'Editar perfil'
module.url = '/user/update/profile/'
module.icon = 'fas fa-user'
module.description = 'Permite cambiar la información de tu cuenta'
module.save()
print(f'insertado {module.name}')

module = Module()
module.name = 'Editar perfil'
module.url = '/pos/client/update/profile/'
module.icon = 'fas fa-user'
module.description = 'Permite cambiar la información de tu cuenta'
module.save()
print(f'insertado {module.name}')

module = Module()
module.name = 'Compañia'
module.url = '/pos/company/update/'
module.icon = 'fas fa-building'
module.description = 'Permite gestionar la información de la compañia'
module.save()
for i in Permission.objects.filter(content_type__model=Company._meta.label.split('.')[1].lower()):
    module.permissions.add(i)
print(f'insertado {module.name}')

group = Group()
group.name = 'Administrador'
group.save()
print(f'insertado {group.name}')
for module in Module.objects.filter().exclude(url__in=['/pos/client/update/profile/', '/pos/sale/client/', '/pos/credit/note/client/']):
    group_module = GroupModule()
    group_module.module_id = module.id
    group_module.group_id = group.id
    group_module.save()
    for permission in module.permissions.all():
        group.permissions.add(permission)

group = Group()
group.name = 'Cliente'
group.save()
print(f'insertado {group.name}')

for module in Module.objects.filter(url__in=['/pos/client/update/profile/', '/pos/sale/client/', '/pos/credit/note/client/', '/user/update/password/']):
    group_module = GroupModule()
    group_module.module_id = module.id
    group_module.group_id = group.id
    group_module.save()
    for permission in module.permissions.all():
        group.permissions.add(permission)

user = User()
user.names = 'William Jair Dávila Vargas'
user.username = 'admin'
user.email = 'davilawilliam93@gmail.com'
user.is_active = True
user.is_superuser = True
user.is_staff = True
user.set_password('hacker94')
user.save()
group = Group.objects.get(pk=1)
user.groups.add(group)
print(f'Bienvenido {user.names}')
