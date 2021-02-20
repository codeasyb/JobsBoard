from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from joboffer.models import JobOffer
from joboffer.api.serializers import JobOfferSerializer

# FIRST ENDPOINT
class JobsListCreateAPIView(APIView):
   
    def get(self, request):
        jobs  = JobOffer.objects.filter(availabe=True)
        serializer = JobOfferSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

# SECOND ENDPOINT
class JobsDetailsCreateAPIView(APIView):
    
    def get_object(self, pk):
        jobs = get_object_or_404(JobOffer, pk=pk)
        return jobs
    
    def get(self, request, pk):
        jobs = self.get_object(pk)
        serializer = JobOfferSerializer(jobs)
        return Response(serializer.data)
    
    def put(self, request, pk):
        job = self.get_object(pk)
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        job = self.get_object(pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        