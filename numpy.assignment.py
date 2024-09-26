import numpy as np

file_path = '/Users/connerstarkey/Downloads/players_stats_by_season_full_details.csv'

data = np.genfromtxt(file_path, delimiter=',', skip_header=1, dtype=None)


def calculate_accuracies(data):
    results = []
    for player in data:
        FG_made, FG_attempts, TP_made, TP_attempts, FT_made, FT_attempts = player[2], player[3], player[4], player[5], player[6], player[7]
        FG_accuracy = FG_made / FG_attempts if FG_attempts > 0 else 0
        TP_accuracy = TP_made / TP_attempts if TP_attempts > 0 else 0
        FT_accuracy = FT_made / FT_attempts if FT_attempts > 0 else 0
        results.append((player[0], player[1], FG_accuracy, TP_accuracy, FT_accuracy))
    return results

def calculate_points_per_minute(data):
    results = []
    for player in data:
        Points, Minutes_played = player[8], player[9]
        points_per_minute = Points / Minutes_played if Minutes_played > 0 else 0
        results.append((player[0], player[1], points_per_minute))
    return results

def calculate_overall_accuracy(data):
    results = []
    for player in data:
        FG_made, TP_made, FT_made = player[2], player[4], player[6]
        FG_attempts, TP_attempts, FT_attempts = player[3], player[5], player[7]
        total_made = FG_made + TP_made + FT_made
        total_attempts = FG_attempts + TP_attempts + FT_attempts
        overall_accuracy = total_made / total_attempts if total_attempts > 0 else 0
        results.append((player[0], player[1], overall_accuracy))
    return results


def calculate_blocks_steals_per_game(data):
    results = []
    for player in data:
        Blocks, Steals, Games_played = player[10], player[11], player[12]
        blocks_per_game = Blocks / Games_played if Games_played > 0 else 0
        steals_per_game = Steals / Games_played if Games_played > 0 else 0
        results.append((player[0], player[1], blocks_per_game, steals_per_game))
    return results


def sort_by_metric(results, metric_index):
  
    def sort_key(item):
        return item[metric_index]
    

    sorted_results = sorted(results, key=sort_key, reverse=True)
    return sorted_results[:100]


accuracies = calculate_accuracies(data)
points_per_minute = calculate_points_per_minute(data)
overall_accuracy = calculate_overall_accuracy(data)
blocks_steals = calculate_blocks_steals_per_game(data)

top_100_FG_accuracy = sort_by_metric([(x[0], x[1], x[2]) for x in accuracies], 2)
top_100_TP_accuracy = sort_by_metric([(x[0], x[1], x[3]) for x in accuracies], 2)
top_100_FT_accuracy = sort_by_metric([(x[0], x[1], x[4]) for x in accuracies], 2)
top_100_points_per_minute = sort_by_metric(points_per_minute, 2)
top_100_overall_accuracy = sort_by_metric(overall_accuracy, 2)
top_100_blocks_per_game = sort_by_metric([(x[0], x[1], x[2]) for x in blocks_steals], 2)
top_100_steals_per_game = sort_by_metric([(x[0], x[1], x[3]) for x in blocks_steals], 2)

print("Top 100 Field Goal Accuracy:", top_100_FG_accuracy)
print("Top 100 Three Point Accuracy:", top_100_TP_accuracy)
print("Top 100 Free Throw Accuracy:", top_100_FT_accuracy)
print("Top 100 Points Per Minute:", top_100_points_per_minute)
print("Top 100 Overall Shooting Accuracy:", top_100_overall_accuracy)
print("Top 100 Blocks Per Game:", top_100_blocks_per_game)
print("Top 100 Steals Per Game:", top_100_steals_per_game)
