from django.conf import settings

def debug(request):
    "Returns context variables helpful for debugging."
    context_extras = {}
    if settings.DEBUG:
        context_extras['debug'] = True
        from django.db import connection
        context_extras['sql_queries'] = connection.queries
    return context_extras