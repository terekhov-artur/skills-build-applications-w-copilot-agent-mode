from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel')
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel')
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc')
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team='dc')

        # Activities
        Activity.objects.create(user=tony.email, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve.email, type='swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce.email, type='cycle', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark.email, type='fly', duration=120, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(user=tony.email, score=100)
        Leaderboard.objects.create(user=steve.email, score=90)
        Leaderboard.objects.create(user=bruce.email, score=110)
        Leaderboard.objects.create(user=clark.email, score=120)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
        Workout.objects.create(name='Situps', description='Do situps', difficulty='easy')
        Workout.objects.create(name='Squats', description='Do squats', difficulty='medium')
        Workout.objects.create(name='Deadlift', description='Heavy deadlift', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
