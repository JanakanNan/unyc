from django.contrib.auth.models import User, Group
from rest_framework import serializers, status
from unycAPI.models import Biere, Comptoir, Stock, Ranking

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Group
            fields = ['url', 'name']

class BieresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biere
        fields = ['ref', 'name', 'description']

class ReferenceSerializer(serializers.Serializer):
    ref = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    def create(self, validated_data):
        return Biere.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ref = validated_data.get('ref', instance.ref)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)

        return instance

class BarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comptoir
        fields = ['pks', 'name']

class ComptoirSerializer(serializers.Serializer):
    pks = serializers.CharField(required=False)
    name = serializers.CharField(required=False)

    def create(self, validated_data):
        return Comptoir.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.pk = validated_data.get('pk', instance.pk)
        instance.name = validated_data.get('name', instance.name)

        return instance

class StockSerializer(serializers.ModelSerializer):
    ref = serializers.CharField(source='biid.ref')
    name = serializers.CharField(source='biid.name')
    description = serializers.CharField(source='biid.description')

    class Meta:
        model = Stock
        fields = ['ref', 'name','description','stock','coid','biid']

class RankingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ranking
        fields = ['name','description','stid']

class RankingSerializerTest(serializers.ModelSerializer):
    rankings = serializers.StringRelatedField(many=True)

    class Meta:
        model = Ranking
        fields = ['name', 'description', 'rankings']




