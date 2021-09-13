from math import asin, cos, radians, sin, sqrt
from django.shortcuts import render_to_response

from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (Level, MovementReason, Rule, Setting, UserDailyStat,
                     UserIsolationLocation, UserLevelScore,
                     UserLocationHistory, UserMovement, BonusPointLink, UserVisitBonusPoint, Instruction, UserProfile)
from .serializers import (LevelSerializer, MovementReasonSerializer,
                          RuleSerializer, SettingSerializer,
                          UserDailyStatSerializer,
                          UserIsolationLocationSerializer,
                          UserLevelScoreSerializer,
                          UserLocationHistorySerializer,
                          UserMovementSerializer, UserSerializer, BonusPointLinkSerializer, UserVisitBonusPointSerializer, InstructionSerializer, UserProfileSerializer)
from users.models import CustomUser
import datetime
from django.db import transaction

class LevelAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Level.objects.get(pk=id)
            serializer = LevelSerializer(item)
            return Response(serializer.data)
        except Level.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Level.objects.get(pk=id)
        except Level.DoesNotExist:
            return Response(status=404)
        serializer = LevelSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Level.objects.get(pk=id)
        except Level.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class LevelAPIListView(APIView):

    def get(self, request, format=None):
        items = Level.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = LevelSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = LevelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RuleAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Rule.objects.get(pk=id)
            serializer = RuleSerializer(item)
            return Response(serializer.data)
        except Rule.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Rule.objects.get(pk=id)
        except Rule.DoesNotExist:
            return Response(status=404)
        serializer = RuleSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Rule.objects.get(pk=id)
        except Rule.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class RuleAPIListView(APIView):

    def get(self, request, format=None):
        items = Rule.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = RuleSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = RuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserIsolationLocationAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = UserIsolationLocation.objects.get(user=id)[0]
            serializer = UserIsolationLocationSerializer(item)
            return Response(serializer.data)
        except UserIsolationLocation.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = UserIsolationLocation.objects.get(pk=id)
        except UserIsolationLocation.DoesNotExist:
            return Response(status=404)
        serializer = UserIsolationLocationSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = UserIsolationLocation.objects.get(pk=id)
        except UserIsolationLocation.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserIsolationLocationAPIListView(APIView):

    def get(self, request, format=None):
        items = UserIsolationLocation.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = UserIsolationLocationSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = UserIsolationLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserLocationHistoryAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = UserLocationHistory.objects.get(pk=id)
            serializer = UserLocationHistorySerializer(item)
            return Response(serializer.data)
        except UserLocationHistory.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = UserLocationHistory.objects.get(pk=id)
        except UserLocationHistory.DoesNotExist:
            return Response(status=404)
        serializer = UserLocationHistorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = UserLocationHistory.objects.get(pk=id)
        except UserLocationHistory.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserLocationHistoryAPIListView(APIView):

    def get(self, request, format=None):
        items = UserLocationHistory.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = UserLocationHistorySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = UserLocationHistorySerializer(data=request.data)
        if serializer.is_valid():
            lat1 = serializer.validated_data.get("lattitude")
            long1 = serializer.validated_data.get("longitude")
            user = serializer.validated_data.get("user")
            user_isolation_location = UserIsolationLocation.objects.get(
                user=user.id)
            distance = self.distance(float(user_isolation_location.lattitude), float(
                lat1), float(user_isolation_location.longitude), float(long1))
            user_level_score = None
            try:
                user_level_score = UserLevelScore.objects.get(
                                user=user.id, is_active=1)                
            except UserLevelScore.DoesNotExist:
                user_level_score = UserLevelScore()
                serializer = UserLevelScoreSerializer(user_level_score, data=self.get_user_level_score_data(user.id))
            new_points = 0
            distance_within_limit = 0
            distance_beyond_limit = 0            
            if distance <= 100:
                new_points = user_level_score.points * 1.013
                distance_within_limit = 1
            else:
                new_points = user_level_score.points * 0.9
                distance_beyond_limit = 1
            serializer.validated_data['points'] = new_points
            serializer.validated_data['dist_from_deafult'] = distance
            serializer.validated_data['user_isolation_location_id'] = user_isolation_location.id
            #serializer.save()
            serializer = UserLevelScoreSerializer(user_level_score, data=self.get_user_level_score_data(
                user_level_score, new_points, 1))

            if(serializer.is_valid()):
                # Saving user level score
                serializer.save()
                try:
                    user_daily_stat = UserDailyStat.objects.get(user=user.id, day=datetime.datetime.today().day, month = datetime.datetime.today().month, year = datetime.datetime.today().year)
                    if user_daily_stat is not None:
                        if distance_within_limit == 1:
                            distance_within_limit = user_daily_stat.distance_within_limit + 1
                        else:
                            distance_within_limit = user_daily_stat.distance_within_limit
                        if distance_beyond_limit == 1:
                            distance_beyond_limit = user_daily_stat.distance_beyond_limit + 1
                        else:
                            distance_beyond_limit = user_daily_stat.distance_beyond_limit
                        serializer = UserDailyStatSerializer(user_daily_stat, data=self.get_user_daily_stat_data(user.id, distance_within_limit, distance_beyond_limit))
                        if(serializer.is_valid()):
                            serializer.save()
                except UserDailyStat.DoesNotExist:
                    user_daily_stat = UserDailyStat()
                    serializer = UserDailyStatSerializer(user_daily_stat, data=self.get_user_daily_stat_data(user.id, distance_within_limit, distance_beyond_limit))
                    if(serializer.is_valid()):
                        serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def get_user_level_score_data(self, user_level_score, new_points, level):
        return {
            "id": user_level_score.id,
            "points": new_points,
            "is_active": 1,
            "user": user_level_score.user.id,
            "level": level
        }

    def get_user_daily_stat_data(self, user_id, distance_within_limit, distance_beyond_limit):
        return {
            "distance_within_limit": distance_within_limit,
            "distance_beyond_limit": distance_beyond_limit,
            "percentage_score" : (distance_within_limit /(distance_within_limit + distance_beyond_limit)) * 100,
            "user": user_id,
            "day" : datetime.datetime.today().day, 
            "month" : datetime.datetime.today().month,
            "year" : datetime.datetime.today().year
        }

    def distance(self, lat1, lat2, lon1, lon2):
        # The math module contains a function named
        # radians which converts from degrees to radians.
        lon1 = radians(lon1)
        lon2 = radians(lon2)
        lat1 = radians(lat1)
        lat2 = radians(lat2)

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

        c = 2 * asin(sqrt(a))

        # Radius of earth in kilometers. Use 3956 for miles
        r = 6371

        # calculate the result
        return (c * r) * 1000


class UserLevelScoreAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = UserLevelScore.objects.get(pk=id)
            serializer = UserLevelScoreSerializer(item)
            return Response(serializer.data)
        except UserLevelScore.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = UserLevelScore.objects.get(pk=id)
        except UserLevelScore.DoesNotExist:
            return Response(status=404)
        serializer = UserLevelScoreSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = UserLevelScore.objects.get(pk=id)
        except UserLevelScore.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserLevelScoreAPIListView(APIView):

    def get(self, request, format=None):
        items = UserLevelScore.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = UserLevelScoreSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        request.data
        serializer = UserLevelScoreSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            try:            
                user_level_score = UserLevelScore.objects.get(user=user.id, is_active=1)
            except UserLevelScore.DoesNotExist:
                serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SettingAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Setting.objects.get(pk=id)
            serializer = SettingSerializer(item)
            return Response(serializer.data)
        except Setting.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Setting.objects.get(pk=id)
        except Setting.DoesNotExist:
            return Response(status=404)
        serializer = SettingSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Setting.objects.get(pk=id)
        except Setting.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SettingAPIListView(APIView):

    def get(self, request, format=None):
        items = Setting.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = SettingSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SettingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class MovementReasonAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = MovementReason.objects.get(pk=id)
            serializer = MovementReasonSerializer(item)
            return Response(serializer.data)
        except MovementReason.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = MovementReason.objects.get(pk=id)
        except MovementReason.DoesNotExist:
            return Response(status=404)
        serializer = MovementReasonSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = MovementReason.objects.get(pk=id)
        except MovementReason.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class MovementReasonAPIListView(APIView):

    def get(self, request, format=None):
        items = MovementReason.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = MovementReasonSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = MovementReasonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserMovementAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = UserMovement.objects.get(pk=id)
            serializer = UserMovementSerializer(item)
            return Response(serializer.data)
        except UserMovement.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = UserMovement.objects.get(pk=id)
        except UserMovement.DoesNotExist:
            return Response(status=404)
        serializer = UserMovementSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = UserMovement.objects.get(pk=id)
        except UserMovement.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserMovementAPIListView(APIView):

    def get(self, request, format=None):
        items = UserMovement.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = UserMovementSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = UserMovementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserDailyStatAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = UserDailyStat.objects.get(pk=id)
            serializer = UserDailyStatSerializer(item)
            return Response(serializer.data)
        except Level.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = UserDailyStat.objects.get(pk=id)
        except Level.DoesNotExist:
            return Response(status=404)
        serializer = UserDailyStatSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = UserDailyStat.objects.get(pk=id)
        except UserDailyStat.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserDailyStatAPIListView(APIView):

    def get(self, request, id, format=None):
        paginator = PageNumberPagination()
        items = UserDailyStat.objects.filter(user_id=id).order_by('-created_at')
        result_page = paginator.paginate_queryset(items, request)
        serializer = UserDailyStatSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, id, format=None):
        serializer = UserDailyStatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserExistsOrNotAPIView(APIView):

    def get(self, request, email_id, format=None):
        try:
            item = CustomUser.objects.filter(
                email=email_id).filter(is_active=1)
            if item != None and len(item) >= 1:
                return Response({"user_exists": 1})
            return Response({"user_exists": 0})
        except CustomUser.DoesNotExist:
            return Response({"user_exists": 0})


class UserScoreAPIListView(APIView):

    def get(self, request, id, format=None):
        try:
            item = UserLevelScore.objects.filter(user=id, is_active=1).first()
            if item != None:
                serializer = UserLevelScoreSerializer(item)
                return Response(serializer.data)
        except UserLevelScore.DoesNotExist:
            return Response(status=404)


class UserwiseIsolcationLocationAPIListView(APIView):

    def get(self, request, id, format=None):
        try:
            items = UserIsolationLocation.objects.filter(user=id)
            if items != None and len(items) >= 1:
                item = items.first()
                if item != None:
                    serializer = UserIsolationLocationSerializer(item)
                    return Response(serializer.data)
            return Response(status=404)
        except UserIsolationLocation.DoesNotExist:
            return Response(status=404)


class LeaderboardView(APIView):

    def get(self, request, id, format=None):
        paginator = PageNumberPagination()
        items = UserLevelScore.objects.select_related().filter(
            is_active=1, level=id).order_by('-points')
        result_page = paginator.paginate_queryset(items, request)
        serializer = UserLevelScoreSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class BonusPointLinkAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = BonusPointLink.objects.get(pk=id)
            serializer = BonusPointLinkSerializer(item)
            return Response(serializer.data)
        except Level.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = BonusPointLink.objects.get(pk=id)
        except Level.DoesNotExist:
            return Response(status=404)
        serializer = BonusPointLinkSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = BonusPointLink.objects.get(pk=id)
        except BonusPointLink.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class BonusPointLinkListView(APIView):

    def get(self, request, format=None):
        items = BonusPointLink.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = BonusPointLinkSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = BonusPointLinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserClickedBonusLinkOrNotAPIView(APIView):

    def get(self, request, user_id, bonus_point_link_id, format=None):
        try:
            item = UserVisitBonusPoint.objects.filter(
                user=user_id, bonus_point_link=bonus_point_link_id)
            if item != None and len(item) >= 1:
                return Response({"bonus_link_read": 1})
            return Response({"bonus_link_read": 0})
        except UserVisitBonusPoint.DoesNotExist:
            return Response({"bonus_link_read": 0})


class UserVisitBonusPointAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = UserVisitBonusPoint.objects.get(pk=id)
            serializer = UserVisitBonusPointSerializer(item)
            return Response(serializer.data)
        except Level.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = UserVisitBonusPoint.objects.get(pk=id)
        except Level.DoesNotExist:
            return Response(status=404)
        serializer = UserVisitBonusPointSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = UserVisitBonusPoint.objects.get(pk=id)
        except UserVisitBonusPoint.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserVisitBonusPointListView(APIView):

    def get(self, request, format=None):
        items = UserVisitBonusPoint.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = UserVisitBonusPointSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = UserVisitBonusPointSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            bonus_point_link_id = serializer.validated_data.get('bonus_point_link')

            user_level_score = UserLevelScore.objects.get(
                user=user.id, is_active=1)
            bonus_point_link = BonusPointLink.objects.get(pk=bonus_point_link_id.id)

            with transaction.atomic():
                serializer.save()
                serializer = UserLevelScoreSerializer(user_level_score, data=self.get_user_level_score_data(
                    user_level_score, user_level_score.points + bonus_point_link.points, 1))

                if serializer.is_valid():
                    serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def get_user_level_score_data(self, user_level_score, new_points, level):
        return {
            "id": user_level_score.id,
            "points": new_points,
            "is_active": 1,
            "user": user_level_score.user.id,
            "level": level
        }


class ActiveBonusLinksAPIView(APIView):

    def get(self, request, user_id, format=None):
        try:
            result = []
            items = BonusPointLink.objects.filter(
                valid_till__gte=datetime.datetime.now())
            for bonus_point_link in items:
                print(bonus_point_link)
                item = UserVisitBonusPoint.objects.filter(
                    user=user_id, bonus_point_link=bonus_point_link.id)
                if item is not None and len(item) == 0:
                    serializer = BonusPointLinkSerializer(bonus_point_link)
                    result.append(serializer.data)
            if len(result) >= 1:
                return Response(result)
            return Response(status=404)
        except BonusPointLink.DoesNotExist:
            return Response(status=404)


class InstructionAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Instruction.objects.get(pk=id)
            serializer = InstructionSerializer(item)
            return Response(serializer.data)
        except Instruction.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Instruction.objects.get(pk=id)
        except Instruction.DoesNotExist:
            return Response(status=404)
        serializer = InstructionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Instruction.objects.get(pk=id)
        except Instruction.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class InstructionAPIListView(APIView):

    def get(self, request, format=None):
        items = Instruction.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = InstructionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = InstructionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserProfileAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = UserProfile.objects.get(pk=id)
            serializer = UserProfileSerializer(item)
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = UserProfile.objects.get(pk=id)
        except UserProfile.DoesNotExist:
            return Response(status=404)
        serializer = UserProfileSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = UserProfile.objects.get(pk=id)
        except UserProfile.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserProfileAPIListView(APIView):

    def get(self, request, format=None):
        items = UserProfile.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = UserProfileSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
