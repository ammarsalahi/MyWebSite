from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
class ContentPagination(PageNumberPagination):
    page_size=8
    max_page_size=32
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'next_page_number': self.page.next_page_number() if self.page.has_next() else None,
            'count': self.page.paginator.count,
            'results': data

        })

class CategoryPagination(PageNumberPagination):
    page_size=4
    max_page_size=32
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'next_page_number': self.page.next_page_number() if self.page.has_next() else None,
            'prev_page_number': self.page.previous_page_number() if self.page.has_previous() else None,
            'count': self.page.paginator.count,
            'results': data

        })