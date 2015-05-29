from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.decorators import detail_route

from club.models import Story, Segment, Comment, UsersRelStories
from club.serializers import StorySerializer, SegmentSerializer, CommentSerializer
from club.serializers import UserSerializer


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


class StoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = StorySerializer
    queryset = Story.objects.order_by('-publish_date')

    def get_queryset(self):
        return self.queryset

    def perform_create(self, serializer):
        instance = serializer.save(creator=self.request.user)

        return super(StoryViewSet, self).perform_create(serializer)

    @detail_route(methods=['post', 'get'])
    def fav(self, request, **kwargs):
        if request.method == 'POST':
            story = self.get_object()
            user = request.user

            try:
                rel = UsersRelStories.objects.get(
                    id_story=story.id_story, id_user=user.id_user)
                rel.favorite = not rel.favorite;
                rel.save()

            except UsersRelStories.DoesNotExist:
                rel = UsersRelStories(
                    id_story=story,
                    id_user=user,
                    favorite=True)
                rel.save()

            return Response({
                'message': 'HOLIS! :D',
            }, status=status.HTTP_204_NO_CONTENT)

        return Response({
                'message': 'HOLIS? D:',
            }, status=status.HTTP_404_NOT_FOUND)

    @detail_route(methods=['post', 'get'])
    def follow(self, request, **kwargs):
        if request.method == 'POST':
            story = self.get_object()
            user = request.user

            try:
                rel = UsersRelStories.objects.get(
                    id_story=story.id_story, id_user=user.id_user)
                rel.following = not rel.following;
                rel.save()

            except UsersRelStories.DoesNotExist:
                rel = UsersRelStories(
                    id_story=story,
                    id_user=user,
                    following=True)
                rel.save()

            return Response({
                'message': 'HOLIS! :D',
            }, status=status.HTTP_204_NO_CONTENT)

        return Response({
                'message': 'HOLIS? D:',
            }, status=status.HTTP_404_NOT_FOUND)


class SegmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = SegmentSerializer
    queryset = Segment.objects.order_by('-id_story')

    def perform_create(self, serializer):
        story = Story.objects.get(id_story=self.request.data['id_story'])
        user = self.request.user

        try:
            rel = UsersRelStories.objects.get(
                id_story=story.id_story, id_user=user.id_user)

            if not rel.contribution:
                rel.contribution = True;
                rel.save()

        except UsersRelStories.DoesNotExist:
            rel = UsersRelStories(
                id_story=story,
                id_user=user,
                contribution=True)
            rel.save()

        instance = serializer.save(author=self.request.user)

        return super(SegmentViewSet, self).perform_create(serializer)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CommentSerializer
    queryset = Comment.objects.order_by('id_comment')

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)

        return super(CommentViewSet, self).perform_create(serializer)


class CurrentUserView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        if request.user.is_authenticated():
            serializer = UserSerializer(request.user)

            return Response(serializer.data)

        return Response({
            'message': 'You are not authenticated',
        }, status=status.HTTP_401_UNAUTHORIZED)