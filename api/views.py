from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .permissions import IsOwner
from .serializers import ContactSerializer
from .serializers import InteractionSerializer
from .serializers import InteractionTagSerializer
from .models import Contact
from .models import Interaction
from .models import InteractionTag


# Contacts stuff

class CreateContact(generics.ListCreateAPIView):
    """defines api create behavior of contact"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        """Only return items owned by the currently authenticated user."""
        user = self.request.user
        return Contact.objects.filter(owner=user)

    def perform_create(self, serializer):
        """Save the post data when creating a new contact"""
        serializer.save(owner=self.request.user)


class DetailsContact(generics.RetrieveUpdateDestroyAPIView):
    """Class handles GET, PUT, and DELETE"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


@api_view(['GET'])
def get_top_contacts(request):
    interactions = Interaction.objects.filter(owner=request.user)
    contact_interact_count = {}
    for interaction in interactions:
        for contact in interaction.contacts.all():
            if contact not in contact_interact_count:
                contact_interact_count[contact] = 1
            else:
                contact_interact_count[contact] += 1
    return Response([((str(k), contact_interact_count[k]) for k in sorted(contact_interact_count, key=contact_interact_count.get,
                                                         reverse=True))])



@api_view(['GET'])
def get_contact_interactions(request, pk):
    """gets all interactions for single contact"""
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ans = []
    interactions = contact.interaction_set.all()
    for interaction in interactions:
        ans.append(InteractionSerializer(interaction).data)
    return Response(ans)


# Interaction Stuff

class CreateInteraction(generics.ListCreateAPIView):
    """api create behavior of interaction"""
    # TODO: Put in tags
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        """Only return items owned by the currently authenticated user."""
        user = self.request.user
        return Interaction.objects.filter(owner=user)

    def perform_create(self, serializer):
        """Save the post data when creating a new Interaction"""
        serializer.save()


class DetailsInteraction(generics.RetrieveUpdateDestroyAPIView):
    """Handles GET, PUT, and DELETE"""
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


# Tag Stuff
class CreateTag(generics.ListCreateAPIView):
    queryset = InteractionTag.objects.all()
    serializer_class = InteractionTagSerializer

    def perform_create(self, serializer):
        serializer.save()


@api_view(['GET'])
def get_tag_interactions(request, pk):
    """gets all of a User's interactions for single tag"""
    try:
        tag = InteractionTag.objects.get(pk=pk)
    except InteractionTag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ans = []
    interactions = tag.interaction_set.all()
    for interaction in interactions:
        if request.user == interaction.owner:
            ans.append(InteractionSerializer(interaction).data)
    return Response(ans)


@api_view(['GET'])
def check_logged_in(request):
    if request.user:
        return Response(str(request.user))
    return Response()