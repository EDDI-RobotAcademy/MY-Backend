from abc import ABC, abstractmethod


class AiRequestRepository(ABC):
    @abstractmethod
    def aiRequest(self, userToken, command, request_id, data):
        pass