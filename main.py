import argparse
import seasons
import simulation
import plot
import timer

def main():
    parser = argparse.ArgumentParser(
        description='Calculate and render probabilities of matchups for the show "Are You The One?".'
    )
    parser.add_argument(
        'season',
        type=str,
        help='the name of a season available in the "seasons" folder, like "s1"')
    
    parser.add_argument(
        '--profile',
        dest='profile', 
        action='store_true',
        help='if provided, profiles the code')

    args = parser.parse_args()
    print(f'Reading season {args.season}')
    season_data = seasons.read_season(args.season)
    
    print(f'Preparing season')
    season = seasons.convert_season(season_data)
    
    print(f'Simulating season')
    with timer.start(args.profile) as t:
        output = simulation.simulate(season)
    print(f'Simulation completed in {t.elapsed} seconds')

    print(f'Plotting season')
    fig = plot.create_plot(season, output)
    fig.show()

if __name__ == "__main__":
    main()
