from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

 
#get all users data
class UserViewset(APIView):
    def get(self, request):
        user_obj = User_profile.objects.all()
        user_serializer_obj = UserSerializer(user_obj, many=True)
        return Response(user_serializer_obj.data)

#for Post/create user
class UserApi(APIView):
    def post(self, request):
        response = {'message': "Something went's wrong"}

        print("in UserAPI")

        try:
            f_name = request.data['first_name'].lower()
            l_name = request.data['last_name'].lower()
            email_id = request.data['email']
            add = request.data['address']
            p_number = request.data['phone_number']
            sex = request.data['gender']
            img = request.data['image']
            uname = request.data['username']
            pword = request.data['password']
            exist_user = User_profile.objects.filter(vfirst_name=f_name, last_name=l_name, email=email_id, ph_number = p_number)
            print('=========>', exist_user)

            if not exist_user:
                print("not exist user")
                info = User_profile(first_name=f_name, last_name=l_name, username= uname,
                                email = email_id, gender = sex, address=add, ph_number=p_number)
                info.save()
                user_id = User_profile.objects.get(username= uname)
                print( "80")
                response = {'message': "Updated",'user_id': user_id.id, 'user_name' : uname}
                return Response(response)
            else:
                print("else part exist visitor")
                user_id = User_profile.objects.get(username=uname)
                
                response = {'message': "Updated",'visit_id': user_id.id, 'user_name': uname}
                return Response(response)

        except Exception as e:
            print(e)
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# get user data
class User_data(APIView):
    def get(self, request, username):
        pin = username
        try:
            user = User_profile.objects.get(username = pin)
        except User_profile.DoesNotExist:
            user = None
        if not user:
            response = {'message': "User does not exist !!!"}
            return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        user_id = user.id
        user_name = User_profile.username
        user_data = User_profile.objects.get(username=username)
        obj = serializers.Serializer("json", user_data)
        #serializer = UserSerializer(user_data)
        response = {'data': obj, 'username': user_name}
        return Response(response)
