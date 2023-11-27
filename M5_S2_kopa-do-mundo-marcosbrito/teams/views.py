from rest_framework.views import APIView, Request, Response, status
from .models import Team
from django.forms import model_to_dict
from utils import data_processing
from exceptions import ImpossibleTitlesError
from exceptions import InvalidYearCupError
from exceptions import NegativeTitlesError


class TeamView(APIView):
    def post(self, req: Request) -> Response:
        team = Team(**req.data)

        try:
            data_processing(model_to_dict(team))
        except NegativeTitlesError as err:
            return Response({"error": f"{err.message}"},
                            status=status.HTTP_400_BAD_REQUEST)
        except InvalidYearCupError as err:
            return Response({"error": f"{err.message}"},
                            status=status.HTTP_400_BAD_REQUEST)
        except ImpossibleTitlesError as err:
            return Response({"error": f"{err.message}"},
                            status=status.HTTP_400_BAD_REQUEST)

        team.save()

        converted = model_to_dict(team)
        return Response(converted, status=status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        teams = Team.objects.all()
        converted_teams = []
        for team in teams:
            converted_team = model_to_dict(team)
            converted_teams.append(converted_team)

        return Response(converted_teams, status.HTTP_200_OK)


class TeamDetailsView(APIView):
    def get(self, req: Request, team_id: int) -> Response:
        try:
            found_team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status.HTTP_404_NOT_FOUND
            )
        converted_account = model_to_dict(found_team)
        return Response(converted_account)

    def delete(self, req: Request, team_id: int) -> Response:
        try:
            found_team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status.HTTP_404_NOT_FOUND
            )
        found_team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, req: Request, team_id: int) -> Response:
        try:
            found_team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status.HTTP_404_NOT_FOUND
            )

        for key, value in req.data.items():
            setattr(found_team, key, value)

        found_team.save()
        converted_team = model_to_dict(found_team)

        return Response(converted_team)
