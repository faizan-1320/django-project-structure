from django.db import models
from project.utils import base_model
from django.conf import settings

# Create your models here.
class TOdo(base_model.BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField()
    is_completed = models.BooleanField(default=0)
    due_date = models.DateTimeField()