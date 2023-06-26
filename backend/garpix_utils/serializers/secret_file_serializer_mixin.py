from django.urls import reverse
from rest_framework import serializers


class SecretFileSerializerMixin(serializers.Serializer):
    file_url = serializers.SerializerMethodField(read_only=True)

    def get_file_url(self, obj):
        return self.context['request'].build_absolute_uri(
            reverse(f'{self.view_basename}-get-file-path', kwargs={'share_hash': obj.share_hash}))
