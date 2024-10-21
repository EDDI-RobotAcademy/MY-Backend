from abc import ABC, abstractmethod
class BoardRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create_category(self, name):
        pass

    @abstractmethod
    def create(self, boardData):
        pass

    @abstractmethod
    def get_all_categories(self):
        pass