import django
from os import path
import sys
mBaseDir = path.dirname(path.abspath(__file__))
sys.path.append(mBaseDir)

from django.contrib.auth.models import User
from blog.models import BlogArticles
import manage

user = User.objects.get()
