from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import get_contact_interactions
from .views import CreateContact
from .views import CreateInteraction
from .views import DetailsContact
from .views import DetailsInteraction

urlpatterns = {
    url(r'^contacts/$', CreateContact.as_view(), name="create"),
    url(r'^contacts/(?P<pk>[0-9]+)/$', DetailsContact.as_view(), name="details"),
    url(r'^interactions/$', CreateInteraction.as_view(), name="create"),
    url(r'^interactions/(?P<pk>[0-9]+)/$', DetailsInteraction.as_view(), name="details"),
    url(r'^contact_interactions/(?P<pk>[0-9]+)/$', get_contact_interactions)
}

urlpatterns = format_suffix_patterns(urlpatterns)
