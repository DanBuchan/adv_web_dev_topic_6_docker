from rest_framework import generics
from rest_framework import mixins
from .models import *
from .serializers import *
from django.http import HttpResponseRedirect
from .tasks import *

class ImageDetail(mixins.CreateModelMixin,  generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        response = super(ImageDetail, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='/test')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        record = serializer.save()
        make_thumbnail.delay(record.pk)


class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['name', 'image', 'thumbnail']


class ImageList(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageListSerializer
