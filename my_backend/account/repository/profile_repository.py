from abc import ABC, abstractmethod


class ProfileRepository(ABC):

    @abstractmethod
    def create(self, nickname, email, account):
        pass

