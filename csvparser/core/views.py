from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import csv
from core.models import MyModel
from core.serializers import MyModelSerializer

class MyModelUploadView(APIView):
    def post(self, request, format=None):
        csv_file = request.FILES['file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        serializer = MyModelSerializer(data=reader)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class MyModelSortView(APIView):
    def get(self, request, column, sort_order, format=None):
        # Check if column is valid
        if not hasattr(MyModel, column):
            return Response({'error': f'Invalid column name: {column}'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if sort order is valid
        if sort_order not in ['asc', 'desc']:
            return Response({'error': f'Invalid sort order: {sort_order}'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Perform sorting and return top 50 rows
        if sort_order == 'asc':
            queryset = MyModel.objects.order_by(column)[:50]
        else:
            queryset = MyModel.objects.order_by(f'-{column}')[:50]
            
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)

            
       
