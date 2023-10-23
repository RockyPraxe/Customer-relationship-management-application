from django.apps import AppConfig


# Define the configuration for the 'crmapp' Django app
# Use the 'BigAutoField' for the default primary key
# Define a method that is executed when the app is ready
# Import and execute the signals defined in the 'crmapp.signals' module


class CrmappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crmapp'

    def ready(self):
        import crmapp.signals
