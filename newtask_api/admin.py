from django.contrib import admin
from newtask_api.models import Post, Like, DisLike

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(DisLike)
