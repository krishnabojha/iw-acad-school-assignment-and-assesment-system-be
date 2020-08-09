from rest_framework.pagination import LimitOffsetPagination

class MypaginationOffset(LimitOffsetPagination):
    default_limit = 5