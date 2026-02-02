 # Populate the octofit_db database with test data
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout
import random

class Command(BaseCommand):

    help = 'Populate the database with test data for OctoFit Tracker'

    def handle(self, *args, **options):
        print('Populate the octofit_db database with test data')
        users = []
        for i in range(5):
            user = User.objects.create(
                name=f'user{i+1}',
                email=f'user{i+1}@example.com',
                password='testpass',
                age=20 + i,
                height=170 + i,
                weight=70 + i
            )
            users.append(user)
        self.stdout.write(self.style.SUCCESS('Created test users.'))

        teams = []
        for i in range(2):
            team = Team.objects.create(
                name=f'Team {i+1}'
            )
            # Assign users to this team
            for user in users[i*2:(i+1)*2]:
                user.team = team
                user.save()
            teams.append(team)
        self.stdout.write(self.style.SUCCESS('Created test teams and assigned users.'))

        workouts = []
        for i in range(3):
            workout = Workout.objects.create(
                name=f'Workout {i+1}',
                description=f'Workout {i+1} description',
                suggested_for=random.choice(['Beginner', 'Intermediate', 'Advanced'])
            )
            workouts.append(workout)
        self.stdout.write(self.style.SUCCESS('Created test workouts.'))

        for user in users:
            for workout in workouts:
                Activity.objects.create(
                    user=user,
                    type=workout.name,
                    duration=random.randint(20, 60),
                    date='2026-02-02'
                )
        self.stdout.write(self.style.SUCCESS('Created test activities.'))
        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
