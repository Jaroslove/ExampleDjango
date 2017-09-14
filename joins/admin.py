from django.contrib import admin
from .models import Join


class JoinAdmin(admin.ModelAdmin):
    list_display = ['email', 'friend', 'timestamp', 'update', 'ip_address']

    class Meta:
        model = Join


admin.site.register(Join, JoinAdmin)
# admin.site.register(JoinFriends)
# Register your models here.
