from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

    def perform_create(self, serializer):
        """Save the post data when creating a new contact"""
        serializer.save()


class DetailsContact(generics.RetrieveUpdateDestroyAPIView):
    """Class handles GET, PUT, and DELETE"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


@api_view(['GET'])
def get_contact_interactions(request, pk):
    """gets all interactions for single person"""
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
    #TODO: Put in tags
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Interaction"""
        serializer.save()


class DetailsInteraction(generics.RetrieveUpdateDestroyAPIView):
    """Handles GET, PUT, and DELETE"""
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer


# Tag Stuff
class CreateTag(generics.ListCreateAPIView):
    queryset = InteractionTag.objects.all()
    serializer_class = InteractionTagSerializer

    def perform_create(self, serializer):
        serializer.save()


@api_view(['GET'])
def get_tag_interactions(request, pk):
    """gets all interactions for single person"""
    try:
        tag = InteractionTag.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ans = []
    interactions = tag.interaction_set.all()
    for interaction in interactions:
        ans.append(InteractionSerializer(interaction).data)
    return Response(ans)

