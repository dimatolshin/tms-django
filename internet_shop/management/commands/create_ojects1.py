from django.core.management import BaseCommand
from internet_shop .models import Product,Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category1=Category.objects.create(name="vejetables")
        products1=Product.objects.create(name='Finiki',description="testy",\
                 price=5,category=category1)
