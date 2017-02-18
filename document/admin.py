from django.contrib import admin

from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'data', )


admin.site.register(Document, DocumentAdmin)
