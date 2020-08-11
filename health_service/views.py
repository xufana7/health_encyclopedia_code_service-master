from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from health_service.models import *
from health_service.serializers import InfoHealthSerializer


@api_view(['GET', 'POST'])
def api_root(request, format=None):
    return Response({
        'health': reverse('health-info', request=request, format=format),
    })


class HealthInfoViewSet(viewsets.ModelViewSet):
    """
    info_health表的数据接口
    """
    queryset = InfoHealth.objects.all()
    serializer_class = InfoHealthSerializer

    def get(self, request, format=None):
        health_infos = InfoHealth.objects.all()
        # 过滤条件
        health_infos = health_infos.filter(weight="456")
        serializer = InfoHealthSerializer(health_infos, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InfoHealthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
