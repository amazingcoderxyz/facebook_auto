# -*- coding: utf-8 -*-

from rest_framework import viewsets

from utils.request_utils import AdminPermission, search
from vps.api.serializers import AgentSerializer
from vps.models import Agent


# Created by: guangda.lee
# Created on: 2019/3/27
# Function: 社交账户类型视图


# ViewSets define the view behavior.
class AgentViewSet(viewsets.ModelViewSet):

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [AdminPermission]

    def get_queryset(self):
        queryset = Agent.objects.all()
        from django.db.models import Q
        queryset = search(self.request, queryset,
                          lambda qs, keyword: qs.filter(Q(queue_name__icontains=keyword) | Q(area__icontains=keyword)))
        return queryset