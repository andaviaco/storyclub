
from rest_framework import serializers

from club.models import Story, Segment, User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = (
            'id_user',
            'username',
            'email',
            'role',
            'registered_date',
            'updated_at',
            'password',
            'confirm_password',
        )
        read_only_fields = ('registered_date', 'updated_at',)

        def create(self, validated_data):
            return User.objects.create(**validated_data)


class SegmentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True, required=False)

    class Meta:
        model = Segment
        fields = (
            'id_segment',
            'text',
            'date',
            'is_last',
            'proposed_end',
            'author',
            'users_votes',
            'id_story',
        )

        read_only_fields = (
            'id_segment',
            'date',
            'is_last',
            'proposed_end',
            'users_votes',
        )

    def get_validation_exclusions(self, *arg, **kwargs):
        exclusions = super(SegmentSerializer, self).get_validation_exclusions()

        return exclusions + ['author']


class StorySerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True, required=False)
    segments = SegmentSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Story
        fields = (
            'id_story',
            'title',
            'image_url',
            'first_text',
            'creator',
            'publish_date',
            'closed',
            'public',
            'users',
            'segments',
        )

        read_only_fields = (
            'id_story',
            'creator',
            'publish_date',
        )

    def get_validation_exclusions(self, *arg, **kwargs):
        exclusions = super(StorySerializer, self).get_validation_exclusions()

        return exclusions + ['creator']
