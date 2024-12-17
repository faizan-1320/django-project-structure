from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .searializers import ToDoCreateSerializer
from .models import TOdo

# Create your views here.
class TodoCreate(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        serializer = ToDoCreateSerializer(data=request.data,context={'request':request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':serializer.data},status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class TodoList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        todo = TOdo.objects.filter(user=request.user)
        serializer = ToDoCreateSerializer(todo,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class TodoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            todo = TOdo.objects.get(id=id, user=request.user)
            serializer = ToDoCreateSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TOdo.DoesNotExist:
            return Response({'error': 'Todo item not found or access denied.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class TodoEdit(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self,request,id):
        todo = TOdo.objects.get(id=id,user=request.user)
        serializer = ToDoCreateSerializer(todo,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Todo Updated Sueccsfully!'},status=status.HTTP_200_OK)
    
class TodoDelete(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,id):
        todo = TOdo.objects.get(id=id,user=request.user)
        todo.delete()
        return Response({'message':'Todo Deleted Sueccsfully!'},status=status.HTTP_200_OK)
    
class TodoComplete(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self,request,id):
        todo = TOdo.objects.get(id=id,user=request.user)
        serializer = ToDoCreateSerializer(todo,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Todo Completed Successfully!'},status=status.HTTP_200_OK)
    
class TodoFilterByStatus(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        status_param = request.query_params.get('is_completed')
        if status_param is not None:
            if status_param.lower() == 'yes':
                is_completed=True
            elif status_param.lower() == 'no':
                is_completed=False
            else:
                return Response({'error':'Invalid value for completed.Use "yer" or "no"'},status=status.HTTP_400_BAD_REQUEST)
            
            todo = TOdo.objects.filter(user=request.user,is_completed=is_completed)
        else:
            todo = TOdo.objects.filter(user=request.user)

        serializer = ToDoCreateSerializer(todo,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
