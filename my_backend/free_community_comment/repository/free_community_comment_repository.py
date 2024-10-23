from abc import ABC, abstractmethod

class FreeCommunityCommentRepository(ABC):
    @abstractmethod
    def list(self, free_community_id):
        pass

    @abstractmethod
    def list_replies(self, parent_id):
        pass

    @abstractmethod
    def create(self, content, free_community_id, account_id, parent_id=None):
        pass

    @abstractmethod
    def findByCommentId(self, comment_id):
        pass

    @abstractmethod
    def deleteByCommentId(self, comment_id):
        pass

    @abstractmethod
    def update(self, comment, commentData):
        pass
