from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'category', 'assigned', 'assigned_to', 'room_number', 'block', 'status',
        'serial_number', 'tag_number', 'date_acquired', 'engraved', 'engravement_number', 'brand')
    list_filter = ('category', 'assigned', 'status')
    search_fields = ('device_id', 'assigned_to', 'room_number', 'tag_number', 'serial_number')
    readonly_fields = ('device_id',)


admin.site.site_header = "Inventory Management Admin"
admin.site.site_title = "Inventory Management Portal"
admin.site.index_title = "Welcome to the Inventory Dashboard"
