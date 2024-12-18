from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Log
from .serializers import LogSerializer


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all().order_by("-created_at")
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
