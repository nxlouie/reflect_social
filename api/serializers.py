from rest_framework import serializers
from .models import Contact
from .models import Interaction
from .models import InteractionTag


class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'owner')


class InteractionSerializer(serializers.ModelSerializer):
    contacts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Contact.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True, queryset=InteractionTag.objects.all()
    )

    class Meta:
        model = Interaction
        fields = ('id', 'note', 'contacts', 'tags', 'owner')


class InteractionTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractionTag
        fields = ('tag_name',)
