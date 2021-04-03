from dataclasses import replace
import json
from models import Season, SeasonData, Week
from pathlib import Path
from typing import Iterable

def replay_season(season: Season) -> Iterable[Season]:
    current_weeks = []

    for week in season.weeks:
        current_weeks.append(week)
        copy_weeks = current_weeks.copy()
        yield replace(season, weeks=copy_weeks)

def read_season(name: str) -> SeasonData:
    path = Path('seasons') / f'{name}.json'
    with path.open('r') as f:
        data = json.load(f)

    result = SeasonData(**data)
    return result

def convert_season(data: SeasonData) -> Season:
    contestants = dict()
    teams = []
    
    contestant_number = 0
    for team_data in data.teams:
        team = []
        for contestant in sorted(team_data):
            contestants[contestant] = contestant_number
            team.append(contestant_number)
            contestant_number += 1
        teams.append(team)

    weeks = []
    week_number = 1
    for week_data in data.weeks:
        pairings = set()
        for pairing_data in week_data.pairings:
            first = contestants[pairing_data[0]]
            second = contestants[pairing_data[1]]
            pairings.add((first, second))

        booths = dict()
        for booth_data in week_data.booths:
            first = contestants[booth_data.pairing[0]]
            second = contestants[booth_data.pairing[1]]
            booths[(first, second)] = booth_data.outcome
        
        week = Week(
            week_number,
            beams = week_data.beams,
            pairings = pairings,
            booths = booths
        )

        weeks.append(week)
        week_number += 1

    sorted_contestants = sorted(contestants.items(), key=lambda x: x[1])
    season = Season(
        contestants = [k for k, v in sorted_contestants],
        teams = teams,
        weeks = weeks
    )

    return season
