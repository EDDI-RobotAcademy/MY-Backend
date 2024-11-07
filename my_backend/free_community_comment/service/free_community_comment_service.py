from abc import ABC, abstractmethod

class FreeCommunityCommentService(ABC):
    @abstractmethod
    def listComments(self, freeCommmunityId):
        pass

    @abstractmethod
    def listReplies(self, parentId):
        pass

    @abstractmethod
    def createComment(self, content, nickname, freeCommmunityId, accountId, parentId):
        pass

    @abstractmethod
    def readComment(self, commentId):
        pass

    @abstractmethod
    def removeComment(self, commentId):
        pass

    @abstractmethod
    def updateComment(self, commentId, commentData):
        pass
