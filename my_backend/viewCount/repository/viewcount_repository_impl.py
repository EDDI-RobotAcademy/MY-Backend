from free_community.entity.models import FreeCommunity
from viewCount.entity.community_viewcount import CommunityViewCount
from viewCount.repository.viewcount_repository import ViewCountCommunityRepository


class ViewCountCommunityRepositoryImpl(ViewCountCommunityRepository):

    def increment_community_view_count(self, communityId):
        try:
            community = FreeCommunity.objects.get(pk=communityId)
            view_count, created = CommunityViewCount.objects.get_or_create(community=community)
            view_count.increment()
            return view_count.count
        except FreeCommunity.DoesNotExist:
            return None

    def get_all_community_view_counts(self):
        view_counts = CommunityViewCount.objects.select_related('community').values(
            'community_id',
            'count'
        )
        return view_counts