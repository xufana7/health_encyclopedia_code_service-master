from rest_framework import serializers
from health_service.models import *


class InfoHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoHealth
        fields = ['health_info_id', 'person_id', 'height', 'weight',
                  'blood_pressure', 'blood_routines', 'urine_routines', 'diet',
                  'sleep_info']
