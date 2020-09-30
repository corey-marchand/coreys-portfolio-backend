# from rest_framework.viewsets import ReadOnlyModelViewSet

from rest_framework.generics import ListAPIView, CreateAPIView

from .models import Form
from .serializers import FormSerializer

class ContactCreate(CreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
