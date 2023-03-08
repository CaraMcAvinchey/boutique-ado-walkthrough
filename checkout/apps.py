from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Let Django know there's a new signals moduel
    with some listeners in it. First, override the ready method 
    & import signals module. Every time a line item is saved or 
    deleted, the custom update total model method will be called
    updating the order totals automatically.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
