def get_avg_rating(games):
    all_ratings = [game.rating for game in games]

    avg_rating = sum(all_ratings) / len(all_ratings)

    return avg_rating
