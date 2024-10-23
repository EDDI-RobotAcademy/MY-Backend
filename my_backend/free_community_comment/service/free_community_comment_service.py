from abc import ABC, abstractmethod

class FreeCommunityCommentService(ABC):
    @abstractmethod
    def listComment(self, freeCommmunityId):
        pass

