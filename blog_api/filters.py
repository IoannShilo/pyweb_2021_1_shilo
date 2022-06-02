from django.db.models.query import QuerySet


def filter_notes_by_author_id(queryset, author_id):
    return queryset.filter(author_id=author_id)


def important_filter(queryset: QuerySet, important: bool):
    """
    """
    if important is not None:
        return queryset.filter(important=important)
    else:
        return queryset


def public_filter(queryset: QuerySet, public: bool):
    """
    """
    if public is not None:
        return queryset.filter(public=public)
    else:
        return queryset
