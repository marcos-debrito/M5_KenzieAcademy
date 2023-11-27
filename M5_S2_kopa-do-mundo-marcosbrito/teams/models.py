from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30)
    titles = models.IntegerField(null=True, default=0)
    top_scorer = models.CharField(max_length=50)
    fifa_code = models.CharField(max_length=3, unique=True)
    first_cup = models.DateField(null=True)

    def __repr__(self) -> str:
        abreviation = self.fifa_code.upper()
        return f"<[{self.pk}] {self.name} - {abreviation}>"
