from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

"""
The above imports two signals post_save and post_delete.
(post meaning after in this case)
These signals are sent by django to the entire application
after a model instance is saved and after it's deleted.

To receive these signals we can import receiver from django.dispatch.
and we'll be listening for signals from the OrderLineItem model.
"""


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create.
    A special type of function that will handle signals 
    from the post_save event (imported)
    Parameters: 
    1. sender of the signal (OrderLineItem)
    2. instance of the model that sent the signal
    3. boolean (new instance or being updated)
    4. keyword arguments
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
