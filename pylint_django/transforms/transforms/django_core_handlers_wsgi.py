from django.core.handlers.wsgi import WSGIRequest as WSGIRequestOriginal


class WSGIRequest(WSGIRequestOriginal):
    status_code = None
    content = ''

    # hacks for tests, where astroid always parses response as WSGIRequest
    # even though it may actually be a different class (HttpResponseRedirect, etc)
    context = {}
    url = ''

    def get(header):
        pass
