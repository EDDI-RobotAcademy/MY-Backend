from abc import ABC, abstractmethod
class BoardService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createCategory(self, name):
        pass

    @abstractmethod
    def createBoard(self, categoryId, title, accountId, content, contentImage):
        pass

    @abstractmethod
    def readBoard(self, boardId):
        pass

    @abstractmethod
    def removeBoard(self, boardId):
        pass

    @abstractmethod
    def updateBoard(self, boardId, boardData):
        pass

    @abstractmethod
    def get_all_categories(self):
        pass

    @abstractmethod
    def listByCategoryId(self, categoryId):
        pass

    @abstractmethod
    def listByTitle(self, title):
        pass

    @abstractmethod
    def listByContent(self, content):
        pass