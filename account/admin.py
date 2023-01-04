from django.contrib import admin
from account.models import User
from account.models import MenuGroup, MenuMaster, TaskMaster, UserTaskAccess, FieldMaster, TaskFieldMaster

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'username', 'name', 'tc','usr','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('name', 'tc','usr')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'name', 'tc', 'usr','password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = ()


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)
admin.site.register(MenuGroup)
admin.site.register(MenuMaster)
admin.site.register(TaskMaster)
admin.site.register(UserTaskAccess)
admin.site.register(FieldMaster)
admin.site.register(TaskFieldMaster)