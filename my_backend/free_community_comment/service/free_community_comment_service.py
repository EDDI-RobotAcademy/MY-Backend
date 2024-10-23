from abc import ABC, abstractmethod

class FreeCommunityCommentService(ABC):
    @abstractmethod
    def listComments(self, freeCommmunityId):
        pass

