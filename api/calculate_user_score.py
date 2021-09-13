from users import CustomUser
from .models import UserLocationHistory, Rule, UserLevelScore, Level
import datetime

# Get user


def get_user(user_name):
    user = CustomUser.objects.get(username=user_name)
    print(user)

# Get rules and make list of tuples with min distance, max distance and points


def get_rules():
    result = []
    rules = Rule.objects.all()
    for rule in rules:
        result.append((rule.min_distance_from_isolation_location,
                       rule.max_distance_from_isolation_location,
                       rule.points))
    return result

# Get rules and make list of tuples with min points, max points and level id


def get_levels():
    result = []
    levels = Level.objects.all()
    for level in levels:
        result.append((level.min_points,
                       level.max_points,
                       level.id))
    return result


def calculate_points(user_id, year, month, day):
    total_points = 0
    level_id = 0

    # Get user location history from database
    user_location_histories = UserLocationHistory.objects.filter(
        user_id__exact=user_id).filter(created_at__startswith=datetime.date(year, month, day))
    # Get rules tuples list from above defined method
    rules = get_rules()

    # Get level tuples list from above defined method
    levels = get_levels()

    # Iterate location history
    for user_location_history in user_location_histories:
        # Iterate rules tuples list
        for rule in rules:
            # Match user location details with rules and increment points based on that
            if user_location_history.dist_from_deafult >= rule[0] and user_location_history.dist_from_deafult <= rule[1]:
                user_level_score = UserLevelScore()
                total_points = total_points + rule[2]
                break

    # Iterate levels to find out user level
    for level in levels:
        if total_points >= level[0] and total_points <= level[1]:
            # Set level id
            level_id = level[2]
            break

    # Create user level score object
    user_level_score = UserLevelScore()
    user_level_score.points = total_points
    user_level_score.user_id = user_id
    user_level_score.level_id = level_id

    # Save user level score object to the database
    user_level_score.save()
