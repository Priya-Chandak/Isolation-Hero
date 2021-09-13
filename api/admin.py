from django.contrib import admin
from . models import User, Setting, Level, Rule, UserIsolationLocation, UserLocationHistory, UserLevelScore, MovementReason, UserMovement, UserDailyStat, BonusPointLink, UserVisitBonusPoint, Instruction

# Register your models here.
admin.site.register(User)
admin.site.register(Setting)
admin.site.register(Level)
admin.site.register(Rule)
admin.site.register(UserIsolationLocation)
admin.site.register(UserLocationHistory)
admin.site.register(UserLevelScore)
admin.site.register(MovementReason)
admin.site.register(UserMovement)
admin.site.register(UserDailyStat)
admin.site.register(BonusPointLink)
admin.site.register(UserVisitBonusPoint)
admin.site.register(Instruction)
