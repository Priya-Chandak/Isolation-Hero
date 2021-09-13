from math import asin, cos, radians, sin, sqrt
from django.shortcuts import render_to_response

from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView


class GoogleAPI(APIView):

    def get(self, request, format=None):
        now = datetime.datetime.now()
        return HttpResponse(now)
        
    # def post(self, request, format=None):
    #     serializer = RuleSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)

