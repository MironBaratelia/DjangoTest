from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as DefUser
from django.utils.translation import gettext_lazy as _

@admin.register(User)
class UserAdmin(DefUser):
    list_display = ('username', 'is_superuser', 'first_name', 'last_name', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'avatar')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

class ConversationInline(admin.TabularInline):
    model = Conversation
    extra = 0
    readonly_fields = ('text', 'user', )

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title',)
    inlines = (ConversationInline, )

class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    readonly_fields = ('text', 'user')

@admin.register(Conversation)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'user', 'created_at', 'modified_at')
    list_filer = ('section', 'user',)
    search_fields = ('text', 'section__title')
    #readonly_fields = ('user',)
    inlines = (MessageInline, )

@admin.register(Message)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',  'created_at', 'modified_at',)
    list_filter = ('conversation', 'conversation__section', 'user',)
    search_fields = ('text', 'conversation__text', 'conversation__section__title',)