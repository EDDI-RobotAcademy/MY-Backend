from viewCount.repository.viewcount_repository_impl import ViewCountCommunityRepositoryImpl
from viewCount.service.viewcount_service import ViewCountCommunityService


class ViewCountCommunityServiceImpl(ViewCountCommunityService):
    def __init__(self):
        self.repository = ViewCountCommunityRepositoryImpl()

    def increment_community_view_count(self, communityId):
        return self.repository.increment_community_view_count(communityId)

    def get_all_community_view_counts(self):
        return self.repository.get_all_community_view_counts()
