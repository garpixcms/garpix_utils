from django.http import FileResponse, Http404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404


class SecretFileViewMixin(viewsets.GenericViewSet):

    @action(methods=['get'], detail=False, url_path='(get_file_path/?P<share_hash>[^/.]+)')
    def get_file_path(self, request, share_hash, *args, **kwargs):

        instance = get_object_or_404(self.get_queryset(), share_hash=share_hash)

        try:
            return FileResponse(open(instance.file.path, 'rb'))

        except IOError:
            raise Http404
