from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = [
            'category', 'assigned', 'assigned_to', 'room_number', 'block',
            'status', 'serial_number', 'tag_number', 'date_acquired',
            'engraved', 'engravement_number', 'brand'
        ]

    def clean(self):
        cleaned_data = super().clean()
        assigned = cleaned_data.get('assigned')
        assigned_to = cleaned_data.get('assigned_to')
        room_number = cleaned_data.get('room_number')
        block = cleaned_data.get('block')
        engraved = cleaned_data.get('engraved')
        engravement_number = cleaned_data.get('engravement_number')

        # If assigned is yes, then assigned_to, room_number, block required
        if assigned == 'yes':
            if not assigned_to:
                self.add_error('assigned_to', 'Please specify who the device is assigned to.')
            if not room_number:
                self.add_error('room_number', 'Please specify the room number.')
            if not block:
                self.add_error('block', 'Please specify the block.')

        # If engraved is yes, then engravement_number required
        if engraved == 'yes' and not engravement_number:
            self.add_error('engravement_number', 'Please provide the engravement number.')

        # status is required and must be one of the choices (default Django validation handles this)

        return cleaned_data
