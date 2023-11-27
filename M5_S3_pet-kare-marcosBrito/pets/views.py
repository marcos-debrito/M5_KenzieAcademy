from rest_framework.views import Request, Response, APIView, status
from .models import Pet
from .serializer import PetSerializer
from groups.serializer import GroupSerializer
from groups.models import Group
from traits.models import Trait
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404


class PetView(APIView, PageNumberPagination):
    def post(self, req: Request) -> Response:
        serializer = PetSerializer(data=req.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        group_data = serializer.validated_data.pop("group")
        traits = serializer.validated_data.pop("traits")

        try:
            group = Group.objects.get(
                scientific_name__iexact=group_data["scientific_name"]
            )
        except Group.DoesNotExist:
            group = Group.objects.create(**group_data)

        pet = Pet.objects.create(**serializer.validated_data, group=group)

        for trait_data in traits:
            try:
                trait = Trait.objects.get(name__iexact=trait_data["name"])
            except Trait.DoesNotExist:
                trait = Trait.objects.create(**trait_data)

            pet.traits.add(trait)

        serializer = PetSerializer(pet)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        by_trait = req.query_params.get("trait", None)
        pets = Pet.objects.all()
        if by_trait:
            pets = Pet.objects.filter(traits__name__icontains=by_trait)
        else:
            pets = Pet.objects.all()

        result = self.paginate_queryset(pets, req)
        serializer = PetSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)


class PetDetailView(APIView):
    def get(self, req: Request, pet_id) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)

        serializer = PetSerializer(pet)

        return Response(serializer.data)

    def delete(self, req: Request, pet_id) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)

        pet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, req: Request, pet_id) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)

        group_data = serializer.validated_data.pop("group", None)
        traits_data = serializer.validated_data.pop("traits", [])

        pet.traits.clear()
        for trait in traits_data:
            trait, creatd = Trait.objects.update_or_create(
                name__iexact=trait["name"], defaults=trait
            )
            pet.traits.add(trait)

        # update_or_create(parametro de busca, defaults=None, **kwargs)

        if group_data:
            group, creatd = Group.objects.update_or_create(
                scientific_name__iexact=group_data["scientific_name"],
                defaults=group_data,
            )
            pet.group = group

        for key, value in serializer.validated_data.items():
            setattr(pet, key, value)
        pet.save()

        serializer = PetSerializer(pet)

        return Response(serializer.data)
