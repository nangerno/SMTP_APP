# views.py
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from rest_framework.decorators import action
from .utils import encode_uid, decode_uid


class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes=[permissions.AllowAny]
    # serializer_class = UserRegistrationSerializer

    @action(detail=False, methods=['POST','PUT'])
    def create_user(self, request):
        encoded_uid = request.query_params.get('uid')
        if not encoded_uid:
            return Response({'error': 'Invalid link'}, status=status.HTTP_400_BAD_REQUEST)
        
        uid_data = decode_uid(encoded_uid)
        if not uid_data:
            return Response({'error': 'Invalid or expired link'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Other actions (list, retrieve, update, partial_update, destroy) can be added here as needed.
    
    @action(detail=False,methods=['GET'])
    def list_users(self,request):
        users=User.objects.all()
        serializer=UserRegistrationSerializer(users)
        return Response({'users':serializer.data})

    @action(detail=False, methods=['POST'])
    def send_email(self,request):
        data=request.data
        user_email=data['email']
        user_first_name=data["first_name"]
        user_last_name=data["last_name"]
        encoded_uid=encode_uid(request.data)
        url_with_uid=f'http://127.0.0.1:8000/register/create_user/?uid={encoded_uid}'
        send_mail(
            'Welcome to the emailAPP',
            f'Hi {user_first_name} {user_last_name},\n\n'
            f'Thank you for registering with us. Please click on the link below to complete the registration process:\n\n'
            f'{url_with_uid}\n\n'
            'Best regards,\n'
            'The emailAPP Team',
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=False,
        )
        print(f'encoded uid {encoded_uid}')
        return Response({'message': 'Welcome to login page',
                          'users': request.data})
       
       
    

        

