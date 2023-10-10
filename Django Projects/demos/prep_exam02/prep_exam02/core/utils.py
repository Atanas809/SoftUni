from prep_exam02.games.models import Game
from prep_exam02.profiles.models import Profile


def get_user_profile():
    try:
        return Profile.objects.first()
    except Profile.DoesNotExist:
        return None


def get_avg_rating():
    games = Game.objects.all()

    all_ratings = sum(game.rating for game in games)

    avg_rating = all_ratings / games.count()

    return f"{avg_rating:.1f}"

