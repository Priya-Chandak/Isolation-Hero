from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . models import User, Setting, Level, Rule, UserIsolationLocation, UserLocationHistory, UserLevelScore, MovementReason, UserMovement, UserDailyStat, BonusPointLink, UserVisitBonusPoint, Instruction, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'


class LevelSerializer(ModelSerializer):

    class Meta:
        model = Level
        fields = '__all__'


class RuleSerializer(ModelSerializer):

    class Meta:
        model = Rule
        fields = '__all__'


class UserIsolationLocationSerializer(ModelSerializer):

    class Meta:
        model = UserIsolationLocation
        fields = '__all__'


class UserLocationHistorySerializer(ModelSerializer):

    class Meta:
        model = UserLocationHistory
        fields = '__all__'


class UserLevelScoreSerializer(ModelSerializer):
    user_email = serializers.CharField(source='user.email', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = UserLevelScore
        fields = ('id', 'points', 'is_active', 'created_at',
                  'updated_at', 'user', 'level', 'user_email', 'username')


class MovementReasonSerializer(ModelSerializer):

    class Meta:
        model = MovementReason
        fields = '__all__'


class UserMovementSerializer(ModelSerializer):

    class Meta:
        model = UserMovement
        fields = '__all__'


class UserDailyStatSerializer(ModelSerializer):

    class Meta:
        model = UserDailyStat
        fields = '__all__'


class BonusPointLinkSerializer(ModelSerializer):

    class Meta:
        model = BonusPointLink
        fields = '__all__'


class UserVisitBonusPointSerializer(ModelSerializer):

    class Meta:
        model = UserVisitBonusPoint
        fields = '__all__'


class InstructionSerializer(ModelSerializer):

    class Meta:
        model = Instruction
        fields = '__all__'


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'
