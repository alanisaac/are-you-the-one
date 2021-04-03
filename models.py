from collections import defaultdict
from dataclasses import dataclass, field
from pydantic import BaseModel
from typing import Dict, List, Mapping, Sequence, Tuple

class BoothData(BaseModel):
    pairing: Tuple[str, str]
    outcome: bool

class WeekData(BaseModel):
    beams: int
    pairings: List[Tuple[str, str]]
    booths: List[BoothData]

class SeasonData(BaseModel):
    teams: List[List[str]]
    weeks: List[WeekData]

@dataclass(frozen=True)
class Week:
    id: int
    beams: int
    pairings: Sequence[Tuple[int, int]]
    booths: Mapping[Tuple[int, int], bool]

    @property
    def name(self) -> str:
        return f'Week {self.id + 1}'

@dataclass(frozen=True)
class Season:
    contestants: List[str]
    teams: List[Sequence[int]]
    weeks: List[Week]

@dataclass()
class Outcome:
    total_counts: int
    counts: Dict[Tuple[int, int], int]

    @property
    def probabilities(self) -> Dict[Tuple[int, int], float]:
        result = defaultdict(float)
        result.update({k: v / self.total_counts for k, v in self.counts.items()})
        return result

@dataclass()
class Simulation:
    season: Season
    weeks: List[Outcome]
