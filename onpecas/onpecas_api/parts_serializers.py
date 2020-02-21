from rest_framework import serializers

from .models import Parts

class PartsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Parts
		fields = ('name','price')
