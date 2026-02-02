import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Workout

# Create test users
def create_users():
    users = []
    for i in range(5):
        user = User.objects.create(
            username=f'user{i+1}',
            email=f'user{i+1}@example.com',
            password='testpass',
            age=20 + i,
            height=170 + i,
            weight=70 + i
        )
        users.append(user)
    return users

# Create test teams
def create_teams(users):
    teams = []
    for i in range(2):
        team = Team.objects.create(
            name=f'Team {i+1}',
            description=f'This is team {i+1}',
            members=[user.id for user in users[i*2:(i+1)*2]]
        )
        teams.append(team)
    return teams

# Create test workouts
def create_workouts():
    workouts = []
    for i in range(3):
        workout = Workout.objects.create(
            name=f'Workout {i+1}',
            description=f'Workout {i+1} description',
            difficulty=random.choice(['Easy', 'Medium', 'Hard'])
        )
        workouts.append(workout)
    return workouts

# Create test activities
def create_activities(users, workouts):
    for user in users:
        for workout in workouts:
            Activity.objects.create(
                user=user,
                workout=workout,
                duration=random.randint(20, 60),
                calories=random.randint(100, 500)
            )

def main():
    users = create_users()
    teams = create_teams(users)
    workouts = create_workouts()
    create_activities(users, workouts)
    print('Test data created successfully.')

if __name__ == '__main__':
    main()
