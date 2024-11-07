from abc import ABC, abstractmethod

class ViewCountCommunityService(ABC):

    @abstractmethod
    def increment_community_view_count(self, communityId):
        pass

    @abstractmethod
    def get_all_community_view_counts(self):
        pass