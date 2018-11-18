from django.test import TestCase
from model_mommy import mommy
from core.models import FeatureRequest


class ClientTest(TestCase):
    
    def setUp(self):
        self.client = mommy.make('core.Client', name='Arthur')

    def test_str(self):
        self.assertEquals('Arthur', str(self.client))

class ProductAreaTests(TestCase):
    def setUp(self):
        self.finance = mommy.make('core.ProductArea', area='Finance')
        self.goods = mommy.make('core.ProductArea', area='Goods')
        self.food = mommy.make('core.ProductArea', area='Food')

    def test_str(self):
        self.assertEquals('Finance', str(self.finance))

class FeatureRequestTests(TestCase):

    def setUp(self):
        self.client = mommy.make('core.Client', name='Coca Cola')
        self.product_area = mommy.make('core.ProductArea', area='Finance')
        self.feature_request = mommy.make('core.FeatureRequest', 
                                         title='Feature',
                                         description='description',
                                         client=self.client, 
                                         product_area=self.product_area,
                                         priority=1)

    def test_str(self):
        expected = '[Finance] :: [Feature] by Coca Cola'
        self.assertEquals(expected, str(self.feature_request))