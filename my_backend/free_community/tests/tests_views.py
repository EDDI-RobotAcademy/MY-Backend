from unittest import TestCase
from unittest.mock import patch, MagicMock

from free_community.entity.models import FreeCommunity
from free_community.service.free_community_service_impl import FreeCommunityServiceImpl


class FreeCommunityViewTest(TestCase):
    @patch('free_community.service.free_community_service_impl.FreeCommunityRepositoryImpl')
    def testList(self, MockFreeCommunityRepositoryImpl):
        mockRepository = MockFreeCommunityRepositoryImpl.getInstance.return_value
        mockFreeCommunityList = [
            FreeCommunity(free_communityId=1, title="Test FreeCommunity 1", content="Content 1"),
            FreeCommunity(free_communityId=2, title="Test FreeCommunity 2", content="Content 2"),
        ]
        mockRepository.list.return_value = mockFreeCommunityList

        print(f"Mock Repository Instance: {mockRepository}")
        print(f"Mock FreeCommunity List: {mockFreeCommunityList}")

        FreeCommunityServiceImpl._FreeCommunityServiceImpl__instance = None
        free_communityService = FreeCommunityServiceImpl.getInstance()

        result = free_communityService.list()

        print(f"result: {result}")

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].title, "Test FreeCommunity 1")
        self.assertEqual(result[1].title, "Test FreeCommunity 2")

        mockRepository.list.assert_called_once()
