from django.test import TestCase
from django.urls import reverse
from .models import Product


def create_product(name, description):
    return Product(name=name, description=description)


class InternetTest(TestCase):
    def test_empty_list(self):
        product = self.client.get(reverse('internet_shop:main'))
        self.assertEquals(product.status_code, 200)
        self.assertContains(product, 'There not have objects!')

    # def test_new_list(self):
    #     product = create_product('dima', 'dima')
    #     response = self.client.get(reverse('internet_shop:main'))
    #     self.assertEquals(response.status_code,200)
    #     self.assertContains(response, product.name)

