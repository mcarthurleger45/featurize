# -*- coding: utf-8 -*-

from rest_framework import serializers
from core.models import Client, FeatureRequest, ProductArea
from django.shortcuts import get_object_or_404
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User

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

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)

class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')