from dataclasses import replace
from models import Contestant, Pairing, Season, Week
from typing import Iterable

def replay_season(season: Season) -> Iterable[Season]:
    current_weeks = []

    for week in season.weeks:
        current_weeks.append(week)
        copy_weeks = current_weeks.copy()
        yield replace(season, weeks=copy_weeks)

def get_season1() -> Season:
    adam = Contestant("Adam")
    chris_t = Contestant("Chris T")
    dillan = Contestant("Dillan")
    dre = Contestant("Dre")
    ethan = Contestant("Ethan")
    j_j = Contestant("JJ")
    joey = Contestant("Joey")
    ryan = Contestant("Ryan")
    chris_s = Contestant("Chris S")
    wes = Contestant("Wes")

    men = [
        adam,
        chris_t,
        dillan,
        dre,
        ethan,
        j_j,
        joey,
        ryan,
        chris_s,
        wes
    ]

    amber = Contestant("Amber")
    ashleigh = Contestant("Ashleigh")
    brittany = Contestant("Brittany")
    coleysia = Contestant("Coleysia")
    jacy = Contestant("Jacy")
    jessica = Contestant("Jessica")
    kayla = Contestant("Kayla")
    paige = Contestant("Paige")
    shanley = Contestant("Shanley")
    simone = Contestant("Simone")

    women = [
        amber,
        ashleigh,
        brittany,
        coleysia,
        jacy,
        jessica,
        kayla,
        paige,
        shanley,
        simone
    ]

    contestants = [*women, *men]
    teams = {
        "men": men,
        "women": women
    }
    week1 = Week(
        1,
        beams=2,
        pairings=[
            Pairing(wes, kayla),
            Pairing(ethan, shanley),
            Pairing(adam, brittany),
            Pairing(dre, jacy),
            Pairing(j_j, simone),
            Pairing(chris_t, jessica),
            Pairing(joey, paige),
            Pairing(chris_s, ashleigh),
            Pairing(ryan, amber),
            Pairing(dillan, coleysia)
        ],
        truth_booths={
            Pairing(chris_t, shanley): False
        }
    )

    week2 = Week(
        2,
        beams=4,
        pairings=[
            Pairing(j_j, jacy),
            Pairing(dillan, jessica),
            Pairing(chris_t, paige),
            Pairing(chris_s, simone),
            Pairing(wes, coleysia),
            Pairing(ethan, amber),
            Pairing(joey, brittany),
            Pairing(ryan, kayla),
            Pairing(dre, ashleigh),
            Pairing(adam, shanley)
        ],
        truth_booths={
            Pairing(ethan, jessica): False
        }
    )

    week3 = Week(
        3,
        beams=2,
        pairings=[
            Pairing(dillan, coleysia),
            Pairing(j_j, jessica),
            Pairing(chris_t, simone),
            Pairing(chris_s, paige),
            Pairing(wes, jacy),
            Pairing(ethan, amber),
            Pairing(joey, shanley),
            Pairing(ryan, kayla),
            Pairing(dre, ashleigh),
            Pairing(adam, brittany)
        ],
        truth_booths={
            Pairing(j_j, simone): False
        }
    )

    week4 = Week(
        4,
        beams=2,
        pairings=[
            Pairing(dillan, coleysia),
            Pairing(j_j, shanley),
            Pairing(chris_t, ashleigh),
            Pairing(chris_s, paige),
            Pairing(wes, jessica),
            Pairing(ethan, kayla),
            Pairing(joey, jacy),
            Pairing(ryan, brittany),
            Pairing(dre, simone),
            Pairing(adam, amber)
        ],
        truth_booths={
            Pairing(dillan, jessica): False
        }
    )

    week5 = Week(
        5,
        beams=5,
        pairings=[
            Pairing(dillan, coleysia),
            Pairing(j_j, jacy),
            Pairing(chris_t, paige),
            Pairing(chris_s, simone),
            Pairing(wes, kayla),
            Pairing(ethan, amber),
            Pairing(joey, jessica),
            Pairing(ryan, ashleigh),
            Pairing(dre, brittany),
            Pairing(adam, shanley)
        ],
        truth_booths={
            Pairing(dre, ashleigh): False,
            Pairing(dillan, coleysia): True
        }
    )

    week6 = Week(
        6,
        beams=5,
        pairings=[
            Pairing(dillan, coleysia),
            Pairing(j_j, jacy),
            Pairing(chris_t, paige),
            Pairing(chris_s, brittany),
            Pairing(wes, kayla),
            Pairing(ethan, amber),
            Pairing(joey, simone),
            Pairing(ryan, jessica),
            Pairing(dre, shanley),
            Pairing(adam, ashleigh)
        ],
        truth_booths={
            Pairing(chris_t, paige): True
        }
    )

    week7 = Week(
        7,
        beams=7,
        pairings=[
            Pairing(dillan, coleysia),
            Pairing(j_j, brittany),
            Pairing(chris_t, paige),
            Pairing(chris_s, jacy),
            Pairing(wes, kayla),
            Pairing(ethan, amber),
            Pairing(joey, jessica),
            Pairing(ryan, ashleigh),
            Pairing(dre, simone),
            Pairing(adam, shanley)
        ],
        truth_booths={
            Pairing(ryan, kayla): False
        }
    )

    weeks = [
        week1,
        week2,
        week3,
        week4,
        week5,
        week6,
        week7
    ]

    season = Season(
        contestants,
        teams,
        weeks
    )

    return season

def get_season4() -> Season:
    stephen = Contestant("Stephen")
    prosper = Contestant("Prosper")
    tyler = Contestant("Tyler")
    cameron = Contestant("Cameron")
    morgan = Contestant("Morgan")
    asaf = Contestant("Asaf")
    john = Contestant("John")
    sam = Contestant("Sam")
    cam = Contestant("Cam")
    giovanni = Contestant("Giovanni")

    men = [
        stephen,
        prosper,
        tyler,
        cameron,
        morgan,
        asaf,
        john,
        sam,
        cam,
        giovanni
    ]

    victoria = Contestant("Victoria")
    alyssa = Contestant("Alyssa")
    camille = Contestant("Camille")
    mikala = Contestant("Mikala")
    tori = Contestant("Tori")
    julia = Contestant("Julia")
    emma = Contestant("Emma")
    nicole = Contestant("Nicole")
    kaylen = Contestant("Kayleen")
    francesca = Contestant("Francesca")

    women = [
        victoria,
        alyssa,
        camille,
        mikala,
        tori,
        julia,
        emma,
        nicole,
        kaylen,
        francesca
    ]

    contestants = [*women, *men]
    teams = {
        "men": men,
        "women": women
    }
    week1 = Week(
        1,
        beams=3,
        pairings=[
            Pairing(giovanni, kaylen),
            Pairing(cam, victoria),
            Pairing(asaf, francesca),
            Pairing(john, emma),
            Pairing(prosper, camille),
            Pairing(sam, alyssa),
            Pairing(cameron, mikala),
            Pairing(morgan, julia),
            Pairing(stephen, nicole),
            Pairing(tyler, tori)
        ],
        truth_booths={
            Pairing(prosper, tori): False
        }
    )

    weeks = [
        week1,
    ]

    season = Season(
        contestants,
        teams,
        weeks
    )

    return season