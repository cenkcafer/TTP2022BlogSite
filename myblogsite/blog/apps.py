# A python file in django environment where database are registered for
# admin. This file makes possible for admin to login from the backend and
# work with the database.
from django.apps import AppConfig
class BlogConfig(AppConfig):
    default_auto_field = ‘django.db.models.BigAutoField’
    name = ‘blog’
