from rest_framework import serializers
from .models import sexOptions
from groups.serializer import GroupSerializer
from traits.serializer import TraitSerializer


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=sexOptions.choices, default=sexOptions.NOT_INFORMED
    )
    # group -> precisamos fazer esse serializer primeiro
    group = GroupSerializer()
    # traits -> tambem precisamos fazer esse serializer!
    traits = TraitSerializer(many=True)
