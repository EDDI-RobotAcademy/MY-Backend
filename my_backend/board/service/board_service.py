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
    def get_all_categories(self):
        pass