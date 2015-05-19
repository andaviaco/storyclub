
from rest_framework import serializers

from club.models import Story


class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = (
            'id_story',
            'title',
            'first_text',
            'publish_date',
            'closed',
            'public',
        )
