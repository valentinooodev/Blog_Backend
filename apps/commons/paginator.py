from rest_framework import pagination
from rest_framework.response import Response

from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        response = Response(data)
        response['count'] = self.page.paginator.count
        response['current'] = self.page.number
        response['next'] = self.get_next_link()
        response['previous'] = self.get_previous_link()
        pagination = {
            'page': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'total_posts': self.page.paginator.count,
            'size': self.page.paginator.per_page
        }
        content = {'pagination': pagination, 'data': data}
        return Response(content)
