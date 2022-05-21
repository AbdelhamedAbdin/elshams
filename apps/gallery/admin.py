from django.contrib import admin

from .models import EduLevel, Gallery


class MultipleImageManaged(admin.ModelAdmin):
    list_display = ('id', 'image')

    def get_form(self, request, obj=None, **kwargs):
        form = super(MultipleImageManaged, self).get_form(request, obj=None, **kwargs)
        form.base_fields['image'].widget.attrs = {
            'multiple': 'multiple'
        }
        return form

    def save_model(self, request, obj, form, change):
        for data in request.FILES.getlist('image'):
            level = EduLevel.objects.get(level=obj)
            Gallery.objects.create(image=data, education_level=level)


admin.site.register(EduLevel)
admin.site.register(Gallery, MultipleImageManaged)
