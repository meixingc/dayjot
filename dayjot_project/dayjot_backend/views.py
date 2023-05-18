from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, logout

from .models import Entry, Water, Food, Exercise, Sleep, Weight
User = get_user_model()
from .serializers import UserSerializer, EntrySerializer, WaterSerializer, FoodSerializer, ExerciseSerializer, SleepSerializer, WeightSerializer

# User Views
class RegisterView(APIView):
    def post(self, req):
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed("User not found")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        return Response({'jwt': token, 'user': user.id}, status=200)

class LogoutView(APIView):
    def post(self, request):
        return Response({'message': 'Logged Out'}, status=200)

class UserView(APIView):
    def get_object(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise Http404   
    def get(self, request): 
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            raise AuthenticationFailed('Authentication header missing')
        try:
            token = auth_header.split(' ')[1]
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except IndexError:
            raise AuthenticationFailed('Token prefix missing')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)

class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, user_id):
        print('User ID:')
        user = User.objects.filter(id=user_id).first()
        if user is None:
            raise Http404
        auth_header = request.headers.get('Authorization')
        print('Authentication Header:')
        if not auth_header:
            raise AuthenticationFailed('Authentication header missing')
        try:
            token = auth_header.split(' ')[1]
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except IndexError:
            raise AuthenticationFailed('Token prefix missing')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        authenticated_user = User.objects.filter(id=payload['id']).first()
        if authenticated_user is None:
            raise AuthenticationFailed('User not found')
        if authenticated_user.id != user.id:
            raise PermissionDenied('You do not have permission to update this user')
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Entry Views
class EntryCreateView(APIView):
    def post(self, request):
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)

class EntryUpdateView(APIView):
    def patch(self, request, entry_id):
        entry = Entry.objects.filter(id=entry_id).first()
        if entry is None:
            raise Http404
        serializer = EntrySerializer(entry, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

class EntryDeleteView(APIView):
    def delete(self, request, entry_id):
        entry = Entry.objects.filter(id=entry_id).first()
        if entry is None:
            raise Http404
        entry.delete()
        return Response(status=204)

class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

# Water Views
class WaterCreateView(APIView):
    def post(self, request):
        serializer = WaterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)

class WaterUpdateView(APIView):
    def patch(self, request, water_id):
        water = Water.objects.filter(id=water_id).first()
        if water is None:
            raise Http404
        serializer = WaterSerializer(water, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

class WaterDeleteView(APIView):
    def delete(self, request, water_id):
        water = Water.objects.filter(id=water_id).first()
        if water is None:
            raise Http404
        water.delete()
        return Response(status=204)

class WaterList(generics.ListCreateAPIView):
    queryset = Water.objects.all()
    serializer_class = WaterSerializer

class WaterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Water.objects.all()
    serializer_class = WaterSerializer

# Food Views
class FoodCreateView(APIView):
    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)

class FoodUpdateView(APIView):
    def patch(self, request, food_id):
        food = Food.objects.filter(id=food_id).first()
        if food is None:
            raise Http404
        serializer = FoodSerializer(food, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

class FoodDeleteView(APIView):
    def delete(self, request, food_id):
        food = Food.objects.filter(id=food_id).first()
        if food is None:
            raise Http404
        food.delete()
        return Response(status=204)

class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

# Exercise Views
class ExerciseCreateView(APIView):
    def post(self, request):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)

class ExerciseUpdateView(APIView):
    def patch(self, request, exercise_id):
        exercise = Exercise.objects.filter(id=exercise_id).first()
        if exercise is None:
            raise Http404
        serializer = ExerciseSerializer(exercise, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

class ExerciseDeleteView(APIView):
    def delete(self, request, exercise_id):
        exercise = Exercise.objects.filter(id=exercise_id).first()
        if exercise is None:
            raise Http404
        exercise.delete()
        return Response(status=204)

class ExerciseList(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

# Sleep Views
class SleepCreateView(APIView):
    def post(self, request):
        serializer = SleepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)

class SleepUpdateView(APIView):
    def patch(self, request, sleep_id):
        sleep = Sleep.objects.filter(id=sleep_id).first()
        if sleep is None:
            raise Http404
        serializer = SleepSerializer(sleep, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

class SleepDeleteView(APIView):
    def delete(self, request, sleep_id):
        sleep = Sleep.objects.filter(id=sleep_id).first()
        if sleep is None:
            raise Http404
        sleep.delete()
        return Response(status=204)

class SleepList(generics.ListCreateAPIView):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer

class SleepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer

#  Weight Views
class WeightCreateView(APIView):
    def post(self, request):
        serializer = WeightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)

class WeightUpdateView(APIView):
    def patch(self, request, weight_id):
        weight = Weight.objects.filter(id=weight_id).first()
        if weight is None:
            raise Http404
        serializer = WeightSerializer(weight, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

class WeightDeleteView(APIView):
    def delete(self, request, weight_id):
        weight = Weight.objects.filter(id=weight_id).first()
        if weight is None:
            raise Http404
        weight.delete()
        return Response(status=204)

class WeightList(generics.ListCreateAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer

class WeightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer