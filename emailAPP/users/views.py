# from django.core.mail import send_mail
# from django.shortcuts import render
from cryptography.fernet import Fernet
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import CustomUser
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.contrib.auth.models import User
# # from .utils import send_email
from django.conf import settings

settings.SECRET_KEY = Fernet.generate_key()

fernet = Fernet(settings.SECRET_KEY)


# # Create your views here.
@api_view(['GET','POST'])

def login(request):
    
     if request.method == 'GET':

        users=CustomUser.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response({'message': 'Welcome to login page',
                          'users': serializer.data})
        
# @api_view(['POST'])
# def create_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status

@api_view(['POST'])
def send_email(request):
    user_email=request.data['email']
    # try:
    link="http://127.0.0.1:8000/update/2/update_user/"
    subject="This is test email"
    message=f"Click the following link to update your password: {link}"
    from_email=settings.EMAIL_HOST_USER
    recipient=['isalman.ahmad01@gmail.com',user_email]
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient,
        fail_silently=False
    )
    # send_mail(
    #     subject=subject,
    #     message= message,
    #     from_email=from_email,
    #     recipient_list=recipient,
    #     fail_silently=False
    # )
    # )
        #send_email()
    return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
#     # except Exception as error:
#     #     print(error)
        
#         # return Response({"Unsucessful"})
        
# """
# @api_view(['POST'])
# def sent_email(request):
#     if request.method == 'POST':
        

# """

class user_viewset(viewsets.ModelViewSet):
     queryset=CustomUser.objects.all()
     serializer_class=UserSerializer
     permission_classes=[AllowAny]

     

     @action(detail=True, methods=['PUT','PATCH',])
     def update_user(self, request, pk):
         users=CustomUser.objects.all()
         print(request.data)
         user = get_object_or_404(users, pk=pk)
         
         #project.update(project_name=request.data)
         serializer = UserSerializer(user, data=request.data, partial=True)
         
         if serializer.is_valid():
             password=request.data['password']
             print(password)
             print("valid")
             serializer.save() 
             
             
              # Save the updated data
             return Response(serializer.data)
         else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

    


