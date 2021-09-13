from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import isolation_hero_api.settings as settings
import datetime
from users.models import CustomUser

class Setting(models.Model):
    setting_id = models.IntegerField()
    key = models.CharField(max_length=20)
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.setting_id

    def save(self, *args, **kwargs):
        self.slug = slugify(self.setting_id)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Setting'


class Level(models.Model):
    name = models.CharField(max_length=100)
    min_no_of_minutes = models.IntegerField(null=False, default=0)
    max_no_of_minutes = models.IntegerField(null=False, default=0)
    min_points = models.IntegerField(null=False, default=0)
    max_points = models.IntegerField(null=False, default=0)
    sequence = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Levels'


class Rule(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()
    min_distance_from_isolation_location = models.FloatField(default=0.0)
    max_distance_from_isolation_location = models.FloatField(default=0.0)
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Rules'


class UserIsolationLocation(models.Model):
    lattitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    city_name = models.CharField(max_length=255)
    state_name = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    is_default = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.city_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.city_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'UserIsolationLocations'


class UserLocationHistory(models.Model):
    lattitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    dist_from_deafult = models.FloatField(null=True)
    points = models.FloatField(null=True)
    status = models.IntegerField(null= False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING, null=False)
    user_isolation_location = models.ForeignKey(
        UserIsolationLocation, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.user_id

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user_id)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'UserLocationHistories'


class UserLevelScore(models.Model):
    points = models.FloatField(blank=False)
    is_active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, related_name='custom_user',
                             on_delete=models.DO_NOTHING, null=True)
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(self.user_id)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.user_id))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'UserLevelScores'


class MovementReason(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'MovementReasons'


class UserMovement(models.Model):
    movement_reason_id = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.user_id

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user_id)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'UserMovements'


class UserDailyStat(models.Model):
    day = models.IntegerField(default= datetime.datetime.today().day)
    month = models.IntegerField(default= datetime.datetime.today().month)
    year = models.IntegerField(default= datetime.datetime.today().year)
    percentage_score = models.FloatField(default= 0.0)
    distance_within_limit = models.IntegerField(default= 0)
    distance_beyond_limit = models.IntegerField(default= 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.day

    def save(self, *args, **kwargs):
        self.slug = slugify(self.day)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'UserDailyStats'


class BonusPointLink(models.Model):
    link = models.CharField(max_length=1024, null = False)
    name = models.CharField(max_length=100, null = False, default="")
    description = models.CharField(max_length=1024, null = False, default="")
    valid_till = models.DateTimeField(blank=False, null = False)
    points = models.FloatField(blank=False, null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'BonusPointLinks'


class UserVisitBonusPoint(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING, null=False)
    bonus_point_link = models.ForeignKey(BonusPointLink,
                             on_delete=models.DO_NOTHING, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bonus_point_link.link

    def save(self, *args, **kwargs):
        self.slug = slugify(self.bonus_point_link.link)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'UserVisitBonusPoints'


class Instruction(models.Model):
    image_url = models.CharField(null = False, max_length= 1024)
    description = models.CharField(null = False, max_length= 2048)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_url

    def save(self, *args, **kwargs):
        self.slug = slugify(self.image_url)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Instructions'


class UserProfile(models.Model):
    age = models.IntegerField(null = True)
    gender = models.IntegerField(null = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'UserProfiles'

