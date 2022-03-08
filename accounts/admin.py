# from django.contrib import admin

# # Register your models here.
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#   list_display =(
#     'username', 'email','first_name', 'last_name','user_image','user_bio'
#   )

#   fieldsets = (
#         (None, {
#             'fields': ('username', 'password')
#         }),
#         ('Personal info', {
#             'fields': ('first_name', 'last_name', 'email')
#         }),
#         ('Permissions', {
#             'fields': (
#                 'is_active', 'is_staff', 'is_superuser',
#                 'groups', 'user_permissions'
#                 )
#         }),
#         ('Important dates', {
#             'fields': ('last_login', 'date_joined')
#         }),
#         ('Additional info', {
#             'fields': ('user_image','user_bio')
#         })
#     )

#   add_fieldsets = (
#         (None, {
#             'fields': ('username', 'password1', 'password2')
#         }),
#         ('Personal info', {
#             'fields': ('first_name', 'last_name', 'email')
#         }),
#         ('Permissions', {
#             'fields': (
#                 'is_active', 'is_staff', 'is_superuser',
#                 'groups', 'user_permissions'
#                 )
#         }),
#         ('Important dates', {
#             'fields': ('last_login', 'date_joined')
#         }),
#         ('Additional info', {
#             'fields': ('user_image', 'user_bio')
#         })
#     )

  

# # Register your models here.

# admin.site.register(CustomUser,CustomUserAdmin)
