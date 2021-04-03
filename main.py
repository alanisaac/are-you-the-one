import argparse
import math
import seasons
import simulation
import plot

def main():
    parser = argparse.ArgumentParser(
        description='Calculate and render probabilities of matchups for the show "Are You The One?".'
    )
    parser.add_argument(
        'season',
        type=str,
        help='the name of a season available in the "seasons" folder, like "s1"')

    args = parser.parse_args()
    print(f'Reading season {args.season}')
    season_data = seasons.read_season(args.season)
    
    print(f'Preparing season')
    season = seasons.convert_season(season_data)
    
    print(f'Simulating season')
    output = simulation.simulate(season)

    print(f'Plotting season')
    fig = plot.create_plot(season, output)
    fig.show()

if __name__ == "__main__":
    main()
