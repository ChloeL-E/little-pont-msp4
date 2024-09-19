from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """Allow to add/edit inline from inside order model"""

    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "order_number",
        "date",
        "order_total",
        "total",
        "original_bag",
        "stripe_pid",
    )

    fields = (
        "order_number",
        "user_profile",
        "date",
        "full_name",
        "email",
        "phone_number",
        "street_address1",
        "street_address2",
        "town_or_city",
        "postcode",
        "county",
        "country",
        "order_total",
        "total",
        "original_bag",
        "stripe_pid",
    )

    list_display = ("order_number", "date",
                    "full_name", "order_total", "total")

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
