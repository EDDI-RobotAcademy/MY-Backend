from account.entity.account import Account
from board.entity.BoardCategory import BoardCategory
from board.entity.models import Board
from board.repository.board_repository import BoardRepository


class BoardRepositoryImpl(BoardRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        return Board.objects.all().order_by('regDate')

    def create_category(self, name):
        category = BoardCategory(**name)
        category.save()
        return category

    def create(self, categoryId, title, accountId, content, contentImage):
        if accountId:
            account = Account.objects.get(id=accountId)
        else:
            account = None
        category = BoardCategory.objects.get(categoryId=categoryId)

        board = Board(
            category = category,
            title = title,
            account = account,
            content = content,
            contentImage = contentImage
        )
        board.save()
        return board

    def findByBoardId(self, boardId):
        return Board.objects.get(boardId=boardId)

    def deleteByBoardId(self, boardId):
        board = Board.objects.get(boardId=boardId)
        board.delete()

    def update(self, board, boardData):
        for key, value in boardData.items():
            print(f"key: {key}, value: {value}")
            setattr(board, key, value)
        board.save()
        return board

    def get_all_categories(self):
        return BoardCategory.objects.all().order_by('categoryId').values('categoryId', 'name')

    def listBoardByCategoryId(self, categoryId):
        return Board.objects.filter(category=categoryId)

    def listBoardByTitle(self, title):
        return Board.objects.filter(title__icontains=title)

    def listBoardByContent(self, content):
        return Board.objects.filter(content__icontains=content)

    def listBoardByAccount(self, account):
        return Board.objects.filter(account=account)