from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Mail
from .serializers import MailSerializer


class MailViewSet(viewsets.ModelViewSet):
    queryset = Mail.objects.all()

    serializer_class = MailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)
