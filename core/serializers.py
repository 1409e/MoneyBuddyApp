# serializers.py
from rest_framework import serializers
from .models import Budget, Goal, Expense

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'total_income', 'total_expense', 'created_at']

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'goal_name', 'target_amount', 'saved_amount', 'created_at']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'category', 'amount', 'description', 'created_at']
