from rest_framework.pagination import LimitOffsetPagination


class LimitOffsetPaginationWithUpperBound(LimitOffsetPagination):
    """Limit offset pagination with upper bound."""
    # Set the maximum limit value to 8
    max_limit = 8
