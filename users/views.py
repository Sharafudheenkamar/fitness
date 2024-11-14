from django.contrib.auth.hashers import make_password
from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib import messages
# from .views import *
import json
from .forms import Clientregistrationform
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.http import HttpResponse

from .serializers import *

# Create your views here.
class Login(View):
    templates_name = 'newlogin.html'
    def get(self,request):
        return render(request,self.templates_name)

    def post(self, request):
        user_type = ""
        response_dict = {"success": False}
        landing_page_url = {
        "ADMIN":"admin_homepage",
        "TRAINER":"trainer_homepage",
         "CLIENT":"client_homepage"

        }
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember = request.POST.get("remember")
        print(username)
        print(password)

        authenticated = authenticate(username=username,password=password)
        try:
            user = Userprofile.objects.get(username=username)
            # print("hello")
        except Userprofile.DoesNotExist:
            response_dict[
                           "reason"
                         ] = "No account found for this username. Please signup."
            messages.error(request, response_dict["reason"])
        if not authenticated:
            # print("notauthenticated")
            response_dict["reason"] = "invalid credentials."
            messages.error(request, response_dict["reason"])
            return redirect(request.GET.get("from") or "login")

        else:
            # print("hello")
            session_dict = {"real_user": authenticated.id}
            token, c = Token.objects.get_or_create(
                       user=user, defaults={"session_dict": json.dumps(session_dict)}
            )
        user_type = authenticated.user_type

        request.session["data"] = {
                        "user_id": user.id,
                        "user_type": user.user_type,
                        "token":token.key,
                        "username": user.username,
                        "status": user.is_active,

                      }
        print("hai")
        print("user")
        print("user_type")
        request.session["user_id"]=user.id,
        request.session["user"] = authenticated.username
        request.session["token"] = token.key
        request.session["status"] = user.is_active
        print(request.session["data"])
        # return redirect(landing_page_url[user_type])
        print(request.session["data"])
        # return redirect(request.GET.get("from") or contractor)
        if remember:
            response = redirect(landing_page_url[user_type])
            response.set_cookie('remembered_username', username)
            response.set_cookie('remembered_password', password)
            return response

            # Clear the remembered username and password if "Remember Me" is not checked
        else:
            response = redirect(landing_page_url[user_type])
            response.delete_cookie('remembered_username')
            response.delete_cookie('remembered_password')
            return response

class UserLoginapi(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = tuple()

    def get(self, request):
        response_dict = {"status": False}
        response_dict["logged_in"] = bool(request.user.is_authenticated)
        response_dict["status"] = True
        return Response(response_dict, HTTP_200_OK)

    def post(self, request):
        response_dict = {"status": False, "token": None, "redirect": False}
        password = request.data.get("password")
        username = request.data.get("username")
        print(username)
        print(password)
        try:
            t_user = Userprofile.objects.get(username=username)
        except Userprofile.DoesNotExist:
            response_dict["reason"] = "No account found for this username. Please signup."
            return Response(response_dict, HTTP_200_OK)

        # blocked_msg = "This account has been blocked. Please contact admin."
        # today = utc_today()
        authenticated = authenticate(username=t_user.username, password=password)
        print(authenticated)
        if not authenticated:
            response_dict["reason"] = "Invalid credentials."
            return Response(response_dict, HTTP_200_OK)
        print("hello")

        user = t_user
        print(user)
        if not user.is_active:
            response_dict["reason"] = "Your login is inactive! Please contact admin"
            return Response(response_dict, HTTP_200_OK)

        session_dict = {"real_user": authenticated.id}
        token, c = Token.objects.get_or_create(
            user=user, defaults={"session_dict": json.dumps(session_dict)}
        )
        login(request, user, "django.contrib.auth.backends.ModelBackend")
        response_dict["session_data"] = {
            "user_id": user.id,
            "user_type": user.user_type,
            "token": token.key,
            "username": user.username,
            "subscriptionplan":user.subscriptionplan,
            "name": user.first_name,
            "status": user.status,
        }
        response_dict["token"] = token.key
        response_dict["status"] = True
        return Response(response_dict, HTTP_200_OK)


class Adminhome(View):
    def get(self,request):
        return render(request,'admin/home_index.html')


class Trainerhome(View):
    def get(self, request):
        return render(request, 'trainer/trainerhome_index.html')
class Clienthome(View):
    def get(self, request):
        return render(request, 'user/userhome_index.html')



class Logout(View):
    def get(self,request):
        request.session["token"]=None
        request.session.flush()
        # print(request.session["token"])
        return redirect("login")


class Clientregistration(View):
    def get(self,request):
        return render(request,'user/signup_index.html')
    def post(self,request):
        form=Clientregistrationform(request.POST,request.FILES)
        if form.is_valid():
            teach = form.save(commit=False)
            us=Userprofile.objects.create_user(user_type='CLIENT',username=request.POST['email'],password=request.POST['password'],email=request.POST['email'],first_name=request.POST['first_name'],gender=request.POST['gender'],dob=request.POST['dob'],photo=request.FILES['photo'],phoneno=request.POST['phoneno'])
            teach.user=us
            teach.save()
            return redirect('login')


class ForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            # username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            print(email)
            try:
                user = Userprofile.objects.get(email=email)
            except Userprofile.DoesNotExist:
                return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

            # Generate OTP
            otp = get_random_string(length=4, allowed_chars='0123456789')

            # Save OTP to user model (you may need to add a field for this)
            user.otp = otp
            user.save()

            # Send OTP through email
            send_mail(
                'Forgot Password OTP',
                f'Canteen Management System Your OTP is: {otp}',
                'from@example.com',
                [email],
                fail_silently=False,
            )

            return Response({'detail': 'OTP sent successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordChangeAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            new_password = serializer.validated_data['new_password']

            # Check if the user exists and OTP is valid
            try:
                user = Userprofile.objects.get(email=email, otp=otp)
            except Userprofile.DoesNotExist:
                return Response({'error': 'Invalid user ID or OTP'}, status=status.HTTP_400_BAD_REQUEST)

            # Change the password
            user.set_password(new_password)
            user.save()

            return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ForgotPassword(View):
    def get(self,request):
        return render(request,'forgot password.html')
    def post(self, request):
        email = request.POST.get('email')

        try:
            user = Userprofile.objects.get(email=email)
        except Userprofile.DoesNotExist:
            messages.error(request, 'User not found.')
            return HttpResponse('User not found.', status=404)

        # Generate OTP
        otp = get_random_string(length=6, allowed_chars='0123456789')
        hashedpass=make_password(otp)
        print(otp)
        # Save OTP to user model (you may need to add a field for this)
        user.password = hashedpass
        user.save()

        # Send OTP through email
        send_mail(
            'Forgot Password OTP',
            f'Canteen Management System Your OTP is: {otp}',
            'from@example.com',
            [email],
            fail_silently=False,
        )

        # messages.success(request, 'OTP sent successfully.')
        return HttpResponse('''<script>alert('otp send successfully to your email');window.location='/'</script>''')
class PasswordChange(View):
    def post(self, request):
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        new_password = request.POST.get('new_password')

        # Check if the user exists and OTP is valid
        try:
            user = Userprofile.objects.get(email=email, otp=otp)
        except Userprofile.DoesNotExist:
            messages.error(request, 'Invalid user ID or OTP')
            return HttpResponse('Invalid user ID or OTP', status=400)

        # Change the password
        user.set_password(new_password)
        user.save()

        messages.success(request, 'Password changed successfully')
        return HttpResponse('Password changed successfully', status=200)

class ProfilePasswordChange(APIView):
        def post(self, request):
            # Get the user making the request
        
            user=Userprofile.objects.get(id=request.data.get('id'))
            # Retrieve old password, new password, and confirm password from request data
            old_password = request.data.get('old_password')
            new_password = request.data.get('new_password')


            # Check if old password matches the current password
            if not user.check_password(old_password):
                return Response({"error": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)

            # Check if new password and confirm password match


            # Set the new password and save the user
            user.set_password(new_password)
            user.save()

            return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)

        class ProfilePasswordChange(APIView):
            def post(self, request):
                # Get the user making the request

                user = Userprofile.objects.get(id=request.data.get('id'))
                # Retrieve old password, new password, and confirm password from request data
                old_password = request.data.get('old_password')
                new_password = request.data.get('new_password')

                # Check if old password matches the current password
                if not user.check_password(old_password):
                    return Response({"error": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)

                # Check if new password and confirm password match

                # Set the new password and save the user
                user.set_password(new_password)
                user.save()

                return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)


class ProfilePlanChange(APIView):
    def post(self, request):
        # Get the user making the request
        user_id = request.data.get('id')
        new_plan = request.data.get('new_plan')

        if user_id is None or new_plan is None:
            return Response({"error": "Missing required data"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Userprofile.objects.get(id=user_id)
        except Userprofile.DoesNotExist:
            return Response({"error": "User doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)

        # Update the user's subscription plan
        user.subscriptionplan = new_plan
        print(new_plan)
        print(user.subscriptionplan)
        user.save()

        return Response({"message": "Plan updated successfully"}, status=status.HTTP_200_OK)