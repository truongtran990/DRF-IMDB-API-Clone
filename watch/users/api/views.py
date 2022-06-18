from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from rest_framework.response import Response


@api_view(["POST", ])
def register_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)