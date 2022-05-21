from django.shortcuts import redirect, render
from django.views import View
from django.core.paginator import Paginator

from .models import Gallery


class GalleryViews(View):

    def get(self, request):
        queryset = Gallery.objects.all()
        pagination = Paginator(queryset, 30)
        page_number = request.GET.get('page')
        get_page = pagination.get_page(page_number)

        if get_page.has_next():
            next_url = f"?page={get_page.next_page_number()}"
        else:
            next_url = ''

        if get_page.has_previous():
            prev_url = f"?page={get_page.previous_page_number()}"
        else:
            prev_url = ''

        try:
            p = int(page_number)
        except TypeError:
            p = 0

        is_pager = True
        if p > get_page.number:
            is_pager = False

        context = {
            'next_url': next_url,
            'prev_url': prev_url,
            'pagination': get_page,
            'is_pager': is_pager
        }
        return render(request, "gallery/gallery.html", context)