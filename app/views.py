from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Student
from app.serializers import STSerializer



@api_view(['GET', 'POST'])
def students_list(request):
    """
    List all postss, or create a new posts.
    """
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = STSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = STSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def students_detail(request, pk):
    """
    Get, udpate, or delete a specific posts
    """
    try:
        students = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = STSerializer(students)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = STSerializer(students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

