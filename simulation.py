import collections
import itertools
from models import Season, Simulation, Week, WeekOutcome
from typing import Iterable, List, Set, Tuple, TypeVar

_T = TypeVar("_T")
_U = TypeVar("_U")

def feasible_week(week: Week, pairings_set: Set[Tuple[int, int]]) -> bool:
    for booth in week.booths:
        is_in_parings = booth.pairing in pairings_set

        if booth.outcome != is_in_parings:
            return False

    correct = 0
    for pairing in week.pairings:
        if pairing in pairings_set:
            correct += 1

    return correct == week.beams

def feasible_season(season: Season, pairings_set: Set[Tuple[int, int]]) -> Iterable[Tuple[Week, bool]]:
    is_feasible = True

    for week in season.weeks:
        if not is_feasible or not feasible_week(week, pairings_set):
            is_feasible = False
        yield (week, is_feasible)

def all_combinations(list1: List[_T], list2: List[_U]) -> Iterable[Iterable[Tuple[_T, _U]]]:
    return (zip(x, list2) for x in itertools.permutations(list1, len(list2)))

def all_combinations_single(list_: List[_T]) -> Iterable[Iterable[Tuple[_T, _T]]]:
    if not list_:
        yield []
    else:
        for group in (((list_[0],) + xs) for xs in itertools.combinations(list_[1:], 1)):
            for groups in all_combinations_single([x for x in list_ if x not in group]):
                yield [group] + groups

def simulate(season: Season) -> Simulation:
    week_outcomes = [WeekOutcome(0, collections.defaultdict(int)) for week in season.weeks]

    if season.teams[0] == season.teams[1]:
        combinations = all_combinations_single(season.teams[0])
    else:
        combinations = all_combinations(season.teams[0], season.teams[1])

    counter = 0
    for combination in combinations:
        counter += 1
        pairing_set = set(combination)
    
        for week, is_feasible in feasible_season(season, pairing_set):
            week_outcome = week_outcomes[week.id]
            if is_feasible:
                week_outcome.total_counts += 1
                for pairing in pairing_set:
                    week_outcome.counts[pairing] += 1

    return Simulation(season, week_outcomes)
