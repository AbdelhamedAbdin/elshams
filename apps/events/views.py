from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator



class PastEvents(View):
    queryset = ""
    pagination = Paginator(queryset, 4)

    def get(self, request):
        page_number = request.GET.get("page")
        get_page = self.pagination.get_page(page_number)

        if get_page.has_next():
            next_url = f"?page={get_page.next_page_number()}"
        else:
            next_url = ''

        if get_page.has_previous():
            prev_url = f"?page={get_page.previous_page_number()}"
        else:
            prev_url = ''

        context = {
            'next_url': next_url,
            'prev_url': prev_url,
            'pagination': get_page
        }
        return render(request, "events/past_events.html", context)
