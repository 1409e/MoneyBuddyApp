# urls.py
from django.urls import path
from .views import BudgetAPIView, GoalAPIView, ExpenseAPIView

urlpatterns = [
    path('api/budget/', BudgetAPIView.as_view(), name='api_budget'),
    path('api/goals/', GoalAPIView.as_view(), name='api_goals'),
    path('api/expenses/', ExpenseAPIView.as_view(), name='api_expenses'),
]