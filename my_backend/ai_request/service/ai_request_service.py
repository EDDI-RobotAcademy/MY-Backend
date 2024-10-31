from abc import ABC, abstractmethod


class AiRequestService(ABC):
    @abstractmethod
    def aiRequestToFastAPI(self, userToken, command, request_id, data):
        pass