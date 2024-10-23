from abc import ABC, abstractmethod

class FreeCommunityCommentRepository(ABC):
    @abstractmethod
    def list(self, free_community_id):
        pass