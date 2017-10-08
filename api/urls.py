from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns
from .views import check_logged_in
from .views import create_new_user
from .views import get_contact_interactions
from .views import get_tag_interactions
from .views import get_top_contacts
from .views import CreateContact
from .views import CreateInteraction
from .views import DetailsContact
from .views import DetailsInteraction
from .views import CreateTag

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^check_logged_in', check_logged_in),
    url(r'^create_new_user', create_new_user),
    url(r'^contacts/$', CreateContact.as_view(), name="create"),
    url(r'^contacts/(?P<pk>[0-9]+)/$', DetailsContact.as_view(), name="details"),
    url(r'^interactions/$', CreateInteraction.as_view(), name="create"),
    url(r'^interactions_frequent/$', get_top_contacts),
    url(r'^interactions/(?P<pk>[0-9]+)/$', DetailsInteraction.as_view(), name="details"),
    url(r'^tag/$', CreateTag.as_view(), name="create"),
    url(r'^contact_interactions/(?P<pk>[0-9]+)/$', get_contact_interactions),
    url(r'^tag_interactions/(?P<pk>[0-9]+)/$', get_tag_interactions),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
