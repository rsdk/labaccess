from django.contrib import admin
from labaccess.models import Verantwortlicher, Labor, Zugang

# Register your models here


class ZugangAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,                  {'fields': ['zugang_v', 'zugang_l']}),
    ('Studentendaten',      {'fields': ['zugang_vname', 'zugang_nname', 'zugang_matnr', 'zugang_email', 'zugang_begruendung']}),
    ('Datumsinformationen', {'fields': ['zugang_anfrage_date', 'zugang_genehmigt_date']}),
    ]


admin.site.register(Verantwortlicher)
admin.site.register(Labor)
admin.site.register(Zugang, ZugangAdmin)