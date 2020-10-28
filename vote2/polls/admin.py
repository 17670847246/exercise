from django.contrib import admin

# Register your models here.
from polls.models import Subject, Teachers


class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'intro', 'is_hot')
    search_fields = ('name', )
    ordering = ('no', )


admin.site.register(Subject, SubjectModelAdmin)


class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'sex', 'birth', 'good_count', 'bad_count', 'subject')
    search_fields = ('name', )
    ordering = ('no', )

admin.site.register(Teachers, TeacherModelAdmin)