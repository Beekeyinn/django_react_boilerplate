from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'

    def get_paginated_response(self, data):
        print("next", self.get_next_link())
        return Response({
            'success': True,
            'message': 'Success',
            'data': data,
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
        })
