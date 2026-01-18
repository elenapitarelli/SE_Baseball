from dataclasses import dataclass

@dataclass
class Salario:
    team_id: int
    total: int

    def __str__(self):
        return f"{self.team_id} , {self.total}"

