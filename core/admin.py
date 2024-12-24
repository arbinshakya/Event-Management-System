from django.contrib import admin
from .models import Be_an_organizer, CreateEvent, Ticket
from .models import *

# Inline model to display tickets for each event
class TicketInline(admin.TabularInline):
    model = Ticket
    fields = ('buyer', 'quantity', 'total_price', 'purchase_date')  # Fields to display for each ticket
    readonly_fields = ('buyer', 'quantity', 'total_price', 'purchase_date')  # Make fields readonly
    extra = 0  # Do not show extra empty rows for new tickets

# Custom admin for CreateEvent to display related tickets
class CreateEventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'event_date','location', 'price', 'total_ticket')  # Fields to display for events
    inlines = [TicketInline]  # Add the TicketInline to the CreateEventAdmin

# Custom admin for Be_an_organizer
class BeAnOrganizerAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'organizer_name', 'organization_email', 'user')  # Fields to display
    readonly_fields = ('user',)  # Make 'user' read-only

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = db_field.related_model.objects.filter(pk=request.user.pk)
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def approve_organizers(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, f"{queryset.count()} organizers approved successfully.")
    approve_organizers.short_description = "Approve selected organizers"


# class TicketAdmin(admin.ModelAdmin):
#     list_display = 

# Register models with the custom admins
admin.site.register(Be_an_organizer, BeAnOrganizerAdmin)
admin.site.register(CreateEvent, CreateEventAdmin)
admin.site.register(Ticket)
admin.site.register(TradeEvent)
admin.site.register(Seller)
admin.site.register(Meeting)
