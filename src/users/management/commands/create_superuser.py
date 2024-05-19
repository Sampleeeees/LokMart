"""
Module for the management command 'create_superuser'
"""
from django.core.management import BaseCommand

from src.users.models import User


class Command(BaseCommand):
    """
    Command for basic data initialization
    """

    def handle(self, *args, **options):
        """
        Handle command
        """
        self._create_superuser()

    def _create_superuser(self):
        """
        Create superuser if superuser is None.
        """
        if not User.objects.filter(is_superuser=True, email="admin@admin.com").exists():
            User.objects.create_superuser("admin@admin.com", "admin", is_superuser=True)
        else:
            self.stdout.write(self.style.ERROR("Superuser already created!"))