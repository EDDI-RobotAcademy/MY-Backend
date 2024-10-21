from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import IntegrityError
from board.entity.models import Board
from board.serializers import BoardSerializer, BoardCategorySerializer
from board.service.board_service import BoardService
from board.service.board_service_impl import BoardServiceImpl
from redis_token.service.redis_service_impl import RedisServiceImpl


class BoardView(viewsets.ViewSet):
    queryset = Board.objects.all()

    boardService = BoardServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def list(self, request):
        boardList = self.boardService.list()
        serializer = BoardSerializer(boardList, many=True)
        return Response(serializer.data)

    def listByCategory(self, request):
        categoryId = request.data.get('categoryId')
        boardList = self.boardService.listByCategoryId(categoryId)
        serializer = BoardSerializer(boardList, many=True)
        return Response(serializer.data)

    def listByTitle(self, request):
        title = request.data.get('title')
        boardList = self.boardService.listByTitle(title)
        serializer = BoardSerializer(boardList, many=True)
        return Response(serializer.data)

    def listByContent(self, request):
        content = request.data.get('content')
        boardList = self.boardService.listByContent(content)
        serializer = BoardSerializer(boardList, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            data = request.data

            categoryId = data.get('categoryId')
            title = data.get('title')
            userToken = data.get('userToken')
            if userToken:
                accountId = self.redisService.getValueByKey(userToken)
            else:
                accountId = None
            content = data.get('content')
            contentImage = data.get('contentImage')

            print(f"categoryId: {categoryId}, title: {title}, accountId: {accountId}, content: {content}, contentImage: {contentImage}")

            self.boardService.createBoard(categoryId, title, accountId, content, contentImage)
            return Response(True, status.HTTP_200_OK)

        except Exception as e:
            return Response(False, status.HTTP_400_BAD_REQUEST)

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

    def readBoard(self, request, pk=None):
        board = self.boardService.readBoard(pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    def removeBoard(self, request, pk=None):
        self.boardService.removeBoard(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def modifyBoard(self, request, pk=None):
        board = self.boardService.readBoard(pk)
        serializer = BoardSerializer(board, data=request.data, partial=True)

        if serializer.is_valid():
            updatedBoard = self.boardService.updateBoard(pk, serializer.validated_data)
            return Response(BoardSerializer(updatedBoard).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)