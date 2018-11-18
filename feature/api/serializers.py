# -*- coding: utf-8 -*-

from rest_framework import serializers
from core.models import Client, FeatureRequest, ProductArea
from django.shortcuts import get_object_or_404

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'

class ProductAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductArea
        fields = '__all__'

class FeatureRequestSerializer(serializers.ModelSerializer):
    product_area = ProductAreaSerializer()
    client = ClientSerializer()

    class Meta:
        model = FeatureRequest
        fields = ('id', 'title', 'description', 'target_date', 'priority', 'client', 'product_area' )

    def create(self, validated_data):
        client = validated_data.pop('client')
        product = validated_data.pop('product_area')
        obj_client = get_object_or_404(Client, name=client['name'])
        obj_product = get_object_or_404(ProductArea, area=product['area'] )
        validated_data['client'] = obj_client
        validated_data['product_area'] = obj_product
        instance = FeatureRequest.objects.create(**validated_data)
        return instance
        