from rest_framework import viewsets, permissions
from unycAPI.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from unycAPI.permissions import MyCustomPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ListStock(viewsets.ModelViewSet):

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated, MyCustomPermission]

class ListRanking(viewsets.ModelViewSet):

    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer
    permission_classes = [permissions.IsAuthenticated, MyCustomPermission]

class ListBieres(APIView):
    permission_classes = [MyCustomPermission, IsAuthenticated]
    """
    List all bieres, or create a new bieres.
    """
    def get(self, request, format=None):
        bieres = Biere.objects.all()
        serializer = BieresSerializer(bieres, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BieresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListComptoirs(APIView):
    permission_classes = [MyCustomPermission, IsAuthenticated]
    """
    List all comptoirs, or create a new comptoirs.
    """
    def get(self, request, format=None):
        comptoirs = Comptoir.objects.all()
        serializer = BarsSerializer(comptoirs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BiereDetail(APIView):
    permission_classes = [MyCustomPermission, IsAuthenticated]
    """
    Retrieve, update or delete a biere instance.
    """
    def get_object(self, pk):
        try:
            return Biere.objects.get(pk = pk)
        except Biere.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        biere = self.get_object(pk)
        serializer = BieresSerializer(biere)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        biere = self.get_object(pk)
        serializer = BieresSerializer(biere, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        biere = self.get_object(pk)
        biere.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ComptoirsDetail(APIView):
    permission_classes = [MyCustomPermission, IsAuthenticated]
    """
    Retrieve, update or delete a biere instance.
    """

    def get_object(self, pk):
        try:
            return Comptoir.objects.get(pk=pk)
        except Comptoir.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comptoir = self.get_object(pk)
        serializer = BarsSerializer(comptoir)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comptoir = self.get_object(pk)
        serializer = BarsSerializer(comptoir, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comptoir = self.get_object(pk)
        comptoir.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class StockDetail(APIView):
    permission_classes = [MyCustomPermission, IsAuthenticated]
    """
    Retrieve, update or delete a biere instance.
    """

    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comptoir = self.get_object(pk)
        serializer = BarsSerializer(comptoir)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comptoir = self.get_object(pk)
        serializer = BarsSerializer(comptoir, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comptoir = self.get_object(pk)
        comptoir.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StockDetailView(generics.ListAPIView):
    serializer_class = StockSerializer

    def get_queryset(self):
        coid = self.kwargs['coid']
        return Stock.objects.filter(coid=coid)

class RankingComptoir(APIView):
    permission_classes = [MyCustomPermission, IsAuthenticated]
    """
    List all comptoirs, or create a new comptoirs.
    """
    def get(self, request, format=None):
        ranking = Ranking.objects.all()
        serializer = RankingSerializerTest(ranking, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RankingSerializerTest(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


