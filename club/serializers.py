
from rest_framework import serializers

from club.models import Story, Segment, User, Comment, UsersRelStories


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


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True, required=False)

    class Meta:
        model = Comment
        fields = (
            'id_comment',
            'text',
            'date',
            'author',
            'id_segment',
            'id_story',
        )

        read_only_fields = (
            'date',
        )

    def get_validation_exclusions(self, *arg, **kwargs):
        exclusions = super(CommentSerializer, self).get_validation_exclusions()

        return exclusions + ['author']


class SegmentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True, required=False)
    comments = CommentSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Segment
        fields = (
            'id_segment',
            'text',
            'date',
            'is_last',
            'proposed_end',
            'author',
            'comments',
            'users_votes',
            'id_story',
        )

        read_only_fields = (
            'id_segment',
            'date',
            'is_last',
            'proposed_end',
            'author',
            'users_votes',
        )

    def get_validation_exclusions(self, *arg, **kwargs):
        exclusions = super(SegmentSerializer, self).get_validation_exclusions()

        return exclusions + ['author']


class StorySerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True, required=False)
    segments = SegmentSerializer(many=True, read_only=True, required=False)
    favs = serializers.SerializerMethodField()
    follows = serializers.SerializerMethodField()
    is_faved = serializers.SerializerMethodField()
    is_followed = serializers.SerializerMethodField()


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
            'favs',
            'is_faved',
            'is_followed',
            'follows',
            'users',
            'segments',
        )

        read_only_fields = (
            'id_story',
            'creator',
            'closed',
            'publish_date',
        )

    def get_validation_exclusions(self, *arg, **kwargs):
        exclusions = super(StorySerializer, self).get_validation_exclusions()

        return exclusions + ['creator']

    def get_favs(self, story):
        favs = UsersRelStories.objects.filter(
            id_story=story.id_story, favorite=True).count();
        return favs

    def get_follows(self, story):
        favs = UsersRelStories.objects.filter(
            id_story=story.id_story, following=True).count();
        return favs

    def get_is_faved(self, story):
        try:
            user = self.context['request'].user
            rel = UsersRelStories.objects.get(
                id_story=story.id_story, id_user=user.id_user)

            return rel.favorite

        except UsersRelStories.DoesNotExist:
            return False

    def get_is_followed(self, story):
        try:
            user = self.context['request'].user
            rel = UsersRelStories.objects.get(
                id_story=story.id_story, id_user=user.id_user)

            return rel.following

        except UsersRelStories.DoesNotExist:
            return False
