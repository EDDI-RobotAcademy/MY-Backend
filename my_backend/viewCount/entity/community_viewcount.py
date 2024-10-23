from django.db import models
from free_community.entity.models import FreeCommunity

class CommunityViewCount(models.Model):
    community = models.OneToOneField(FreeCommunity, on_delete=models.CASCADE, related_name='view_count')
    count = models.PositiveIntegerField(default=0)

    def increment(self):
        self.count += 1
        self.save()

    class Meta:
        db_table = 'free_community_viewcount'
        app_label = 'viewCount'