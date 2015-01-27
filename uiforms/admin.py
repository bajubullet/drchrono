from django.contrib import admin

from django_object_actions import DjangoObjectActions

from models import UiForm, FormFields
from views import show_form


class FormFieldsInline(admin.StackedInline):
    model = FormFields
    extra = 3


class UiFormAdmin(DjangoObjectActions, admin.ModelAdmin):
    def preview_this(self, request, obj):
        return show_form(request, obj)

    preview_this.label = 'Preview'
    preview_this.short_description = 'Preview this'
    inlines = (FormFieldsInline,)
    exclude = ('author',)
    objectactions = ('preview_this',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(UiForm, UiFormAdmin)
# admin.site.register(FormFields)
