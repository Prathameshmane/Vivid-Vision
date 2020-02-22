from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import User
# Create your models here.

User = get_user_model()
