from django.urls import path
from . import views

urlpatterns = [
    # user
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('user', views.UserView.as_view()),
    path('user/update/<int:user_id>', views.UserUpdateView.as_view()),
    path('users', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    # entry
    path('entry/create', views.EntryCreateView.as_view()),
    path('entry/update/<int:entry_id>', views.EntryUpdateView.as_view()),
    path('entry/delete/<int:entry_id>', views.EntryDeleteView.as_view()),
    path('entries', views.EntryList.as_view()),
    path('entries/<int:pk>', views.EntryDetail.as_view()),
    # water
    path('water/create', views.WaterCreateView.as_view()),
    path('water/update/<int:water_id>', views.WaterUpdateView.as_view()),
    path('water/delete/<int:water_id>', views.WaterDeleteView.as_view()),
    path('waters', views.WaterList.as_view()),
    path('waters/<int:pk>', views.WaterDetail.as_view()),
    # food
    path('food/create', views.FoodCreateView.as_view()),
    path('food/update/<int:food_id>', views.FoodUpdateView.as_view()),
    path('food/delete/<int:food_id>', views.FoodDeleteView.as_view()),
    path('foods', views.FoodList.as_view()),
    path('foods/<int:pk>', views.FoodDetail.as_view()),
    # exercise
    path('exercise/create', views.ExerciseCreateView.as_view()),
    path('exercise/update/<int:exercise_id>', views.ExerciseUpdateView.as_view()),
    path('exercise/delete/<int:exercise_id>', views.ExerciseDeleteView.as_view()),
    path('exercises', views.ExerciseList.as_view()),
    path('exercises/<int:pk>', views.ExerciseDetail.as_view()),
]