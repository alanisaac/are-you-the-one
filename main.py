from models import Pairing
import math
import seasons
import simulation
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def heatmap_for_week(season, outcome):
    rows = season.teams["men"]
    columns = season.teams["women"]
    probabilities = outcome.probabilities

    cells = []
    for row in rows:
        row_values = []
        cells.append(row_values)
        for column in columns:
            probability = probabilities[Pairing(row, column)]
            row_values.append(probability)

    heatmap = go.Heatmap(z=cells,
        x=[x.name for x in columns],
        y=[x.name for x in rows],
        zmin=0,
        zmax=1,
        colorscale=[[0, 'black'], [0.5, 'yellow'], [1.0, 'green']]
    )

    return heatmap

def main():
    counter = 0
    season = seasons.get_season1()
    limit = 10000000
    output = simulation.simulate(season, limit)

    columns = 2
    rows = len(season.weeks) // columns + 1
    fig = make_subplots(
        rows=rows, 
        cols=columns,
        subplot_titles=[
            f'Week {week.id}: {outcome.total_counts:,} possibilities' 
            for week, outcome in output.weeks.items()
        ]
    )

    for week, outcome in output.weeks.items():
        heatmap = heatmap_for_week(season, outcome)
        row = counter // columns + 1
        col = counter % columns + 1
        fig.add_trace(heatmap, row=row, col=col)
        counter += 1

    fig.show()

if __name__ == "__main__":
    main()
