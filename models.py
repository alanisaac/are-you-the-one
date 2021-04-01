from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

@dataclass(frozen=True)
class Contestant:
    name: str

@dataclass(frozen=True)
class Pairing:
    first: Contestant
    second: Contestant

@dataclass(frozen=True, eq=True)
class Week:
    id: int
    beams: int = field(compare=False)
    pairings: List[Pairing] = field(compare=False)
    truth_booths: Dict[Pairing, bool] = field(compare=False)

@dataclass(frozen=True)
class Season:
    contestants: List[Contestant]
    teams: Dict[str, List[Contestant]]
    weeks: List[Week]

@dataclass()
class Outcome:
    total_counts: int
    counts: Dict[Pairing, float]

    @property
    def probabilities(self) -> Dict[Pairing, float]:
        result = defaultdict(int)
        result.update({k: v / self.total_counts for k, v in self.counts.items()})
        return result

@dataclass()
class Simulation:
    season: Season
    weeks: Dict[Week, Outcome]
