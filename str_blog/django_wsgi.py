#!/usr/bin/env python
# -*-coding:utf-8-*-
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE","vmaig_blog.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
