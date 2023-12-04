from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.schemas import DefaultSchema

reviews = []

class AppDevClubReviewsView(APIView):
    def post(self, request):
        user_review = request.get('user_review', '')
        #review to the array
        reviews.append(user_review)
        print(user_review)
        return JsonResponse({'status': 'success'})
    
    def get(self, request):
        return Response({'user_reviews': reviews})