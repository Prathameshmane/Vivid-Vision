from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from accounts.models import User

from excel.models import Table
@admin.register(Table)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id',)

    seacrch_fields = ['id']

    def __str__(self):
        return self.pname

# Register your models here.
admin.site.register(User)
