from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create Users
        users = [
            User.objects.create(name='Tony Stark', email='tony@marvel.com', team='marvel'),
            User.objects.create(name='Steve Rogers', email='steve@marvel.com', team='marvel'),
            User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team='dc'),
            User.objects.create(name='Clark Kent', email='clark@dc.com', team='dc'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='run', duration=30, date='2024-01-01')
        Activity.objects.create(user=users[1], type='cycle', duration=45, date='2024-01-02')
        Activity.objects.create(user=users[2], type='swim', duration=25, date='2024-01-03')
        Activity.objects.create(user=users[3], type='yoga', duration=60, date='2024-01-04')

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=120, rank=1)
        Leaderboard.objects.create(user=users[1], score=110, rank=2)
        Leaderboard.objects.create(user=users[2], score=100, rank=3)
        Leaderboard.objects.create(user=users[3], score=90, rank=4)

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
