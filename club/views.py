from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from club.models import Story
from club.serializers import StorySerializer


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


class StoryViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = StorySerializer
    queryset = Story.objects.order_by('-publish_date')
