from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from club.models import Story, Segment, Comment
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

    def retrieve(self, request, pk=None):
        story = get_object_or_404(self.queryset, pk=pk)
        segments = Segment.objects.filter(id_story=story.id_story)
        serializer = StorySerializer(story)
        return Response(serializer.data)

    def perform_create(self, serializer):
        print self.request
        instance = serializer.save(creator=self.request.user)

        return super(StoryViewSet, self).perform_create(serializer)


class SegmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = SegmentSerializer
    queryset = Segment.objects.order_by('-id_story')

    def perform_create(self, serializer):
        print self.request
        instance = serializer.save(author=self.request.user)

        return super(SegmentViewSet, self).perform_create(serializer)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CommentSerializer
    queryset = Comment.objects.order_by('id_comment')

    def perform_create(self, serializer):
        print self.request
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