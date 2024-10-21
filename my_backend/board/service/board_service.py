from abc import ABC, abstractmethod
class BoardService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createCategory(self, name):
        pass

    @abstractmethod
    def createBoard(self, boardData):
        pass

    @abstractmethod
    def get_all_categories(self):
        pass