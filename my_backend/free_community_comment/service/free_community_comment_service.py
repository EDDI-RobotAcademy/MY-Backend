from abc import ABC, abstractmethod

class FreeCommunityCommentService(ABC):
    @abstractmethod
    def listComments(self, freeCommmunityId):
        pass

    @abstractmethod
    def listReplies(self, parentId):
        pass

    @abstractmethod
    def createComment(self, content, freeCommmunityId, accountId, parentId):
        pass

    @abstractmethod
    def readComments(self, commentId):
        pass
