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
