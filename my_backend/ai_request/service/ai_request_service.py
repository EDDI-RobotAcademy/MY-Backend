from abc import ABC, abstractmethod


class AiRequestService(ABC):
    @abstractmethod
    def aiRequestToFastAPI(self, command, data):
        pass