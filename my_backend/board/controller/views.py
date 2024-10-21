from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import IntegrityError
from board.entity.models import Board
from board.serializers import BoardSerializer, BoardCategorySerializer
from board.service.board_service import BoardService
from board.service.board_service_impl import BoardServiceImpl


class BoardView(viewsets.ViewSet):
    queryset = Board.objects.all()

    boardService = BoardServiceImpl.getInstance()

    def list(self, request):
        boardList = self.boardService.list()
        serializer = BoardSerializer(boardList, many=True)
        return Response(serializer.data)

    def create(self, request):
        print("Received data:", request.data)
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            try:
                board = self.boardService.createBoard(serializer.validated_data)
                return Response(BoardSerializer(board).data, status=status.HTTP_201_CREATED)
            except Exception as e:
                print("Error in createBoard:", str(e))
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("Serializer errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def createCategory(self, request):
        serializer = BoardCategorySerializer(data=request.data)
        if serializer.is_valid():
            try:
                category = self.boardService.createCategory(serializer.validated_data)
                return Response({"message": "카테고리 생성 완료"}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"message": "이미 존재하는 카테고리입니다."}, status=status.HTTP_400_BAD_REQUEST)
            except Exception:
                return Response({"message": "카테고리 추가 중 오류가 발생했습니다."}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def getCategories(self, request):
        service = BoardServiceImpl()
        categories = service.get_all_categories()
        return Response(categories)
