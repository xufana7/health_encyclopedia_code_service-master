# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Diagnosis(models.Model):
    diagnosis_id = models.BigAutoField(primary_key=True)
    disease_basic = models.CharField(max_length=1024, blank=True, null=True)
    disease_history = models.CharField(max_length=1024, blank=True, null=True)
    allergy_history = models.CharField(max_length=1024, blank=True, null=True)
    immunization = models.CharField(max_length=2048, blank=True, null=True)
    diagnosis_history = models.CharField(max_length=2048, blank=True, null=True)
    drag_usage = models.CharField(max_length=2048, blank=True, null=True)
    surgery = models.CharField(max_length=2048, blank=True, null=True)
    radiation = models.CharField(max_length=2048, blank=True, null=True)
    inspection_result = models.CharField(max_length=2048, blank=True, null=True)
    diagnostic_result = models.CharField(max_length=2048, blank=True, null=True)
    data_create = models.DateTimeField(blank=True, null=True)
    data_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'diagnosis'


class DiseaseRisk(models.Model):
    disease_risk_id = models.BigAutoField(primary_key=True)
    person_id = models.BigIntegerField(blank=True, null=True)
    disease_risk = models.CharField(max_length=256, blank=True, null=True)
    data_create = models.DateTimeField(blank=True, null=True)
    data_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'disease_risk'


class InfoHealth(models.Model):
    health_info_id = models.BigAutoField(primary_key=True)
    person_id = models.BigIntegerField(blank=True, null=True)
    height = models.CharField(max_length=32, blank=True, null=True)
    weight = models.CharField(max_length=32, blank=True, null=True)
    blood_pressure = models.CharField(max_length=32, blank=True, null=True)
    blood_routines = models.CharField(max_length=128, blank=True, null=True)
    urine_routines = models.CharField(max_length=128, blank=True, null=True)
    diet = models.CharField(max_length=128, blank=True, null=True)
    sleep_info = models.BigIntegerField(blank=True, null=True)
    data_create = models.DateTimeField(blank=True, null=True)
    data_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'info_health'


class InfoSleep(models.Model):
    sleep_info_id = models.BigAutoField(primary_key=True)
    person_id = models.BigIntegerField(blank=True, null=True)
    sleep_start = models.DateTimeField(blank=True, null=True)
    duration = models.BigIntegerField(blank=True, null=True)
    quality = models.CharField(max_length=128, blank=True, null=True)
    deep_quality = models.CharField(max_length=128, blank=True, null=True)
    advise = models.CharField(max_length=1024, blank=True, null=True)
    data_create = models.DateTimeField(blank=True, null=True)
    data_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'info_sleep'


class InfoTrack(models.Model):
    track_id = models.BigAutoField(primary_key=True)
    person_id = models.BigIntegerField(blank=True, null=True)
    from_field = models.CharField(db_column='from', max_length=256, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    destination = models.CharField(max_length=256, blank=True, null=True)
    track_date_start = models.DateTimeField(blank=True, null=True)
    track_date_end = models.DateTimeField(blank=True, null=True)
    data_create = models.DateTimeField(blank=True, null=True)
    data_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'info_track'


class PersonInformation(models.Model):
    person_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    sex = models.CharField(max_length=32, blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)
    certificate_type = models.CharField(max_length=32, blank=True, null=True)
    certificate_number = models.CharField(max_length=128, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    contact_phone = models.CharField(max_length=256, blank=True, null=True)
    emergency_contact = models.CharField(max_length=256, blank=True, null=True)
    emergency_phone = models.CharField(max_length=256, blank=True, null=True)
    data_create = models.DateTimeField(blank=True, null=True)
    data_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'person_information'


class RawData(models.Model):
    raw_data_id = models.BigAutoField(primary_key=True)
    image_type = models.CharField(max_length=128, blank=True, null=True)
    person_id = models.BigIntegerField(blank=True, null=True)
    diagnosis_id = models.BigIntegerField(blank=True, null=True)
    raw_data_path = models.CharField(max_length=1024, blank=True, null=True)
    data_create = models.DateTimeField(blank=True, null=True)
    data_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'raw_data'
