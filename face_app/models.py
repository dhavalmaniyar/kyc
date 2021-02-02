from django.db import models
# from webcam.fields import DBCameraField, FSCameraField
# from webcam.storage import CameraFileSystemStorage

# Create your models here.
class Person(models.Model):
    # picture1 = DBCameraField() # store in the database
    # picture2 = FSCameraField(format='gif') # by default storen on settings.MEDIA_ROOT
    # picture3 = FSCameraField(format='png',
    #                          storage=CameraFileSystemStorage('/absolute/path/to/'),
    #                          null=True, blank=True) # store on filesystem   
    pass