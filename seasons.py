import json
from models import Season, SeasonData, TruthBooth, Week
from pathlib import Path

def read_season(name: str) -> SeasonData:
    path = Path('seasons') / f'{name}.json'
    with path.open('r') as f:
        data = json.load(f)

    result = SeasonData(**data)
    return result

def convert_season(data: SeasonData) -> Season:
    contestants = dict()
    teams = []
    
    next_contestant_number = 0
    for team_data in data.teams:
        team = []
        for contestant in sorted(team_data):
            contestant_number = contestants.setdefault(contestant, next_contestant_number)
            if contestant_number == next_contestant_number:
                next_contestant_number += 1

            team.append(contestant_number)
        teams.append(team)

    weeks = []
    week_number = 0
    for week_data in data.weeks:
        booths = []
        for booth_data in week_data.booths:
            first = contestants[booth_data.pairing[0]]
            second = contestants[booth_data.pairing[1]]
            booth = TruthBooth(
                pairing=(first, second),
                outcome=booth_data.outcome
            )
            booths.append(booth)

        pairings = set()
        # each contestant may only be in one pairing
        contestants_copy = dict(contestants)
        for pairing_data in week_data.pairings:
            first = contestants_copy.pop(pairing_data[0])
            second = contestants_copy.pop(pairing_data[1])
            pairings.add((first, second))
        
        week = Week(
            id = week_number,
            pairings = pairings,
            beams = week_data.beams,
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
