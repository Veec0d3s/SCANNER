import csv
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Device
from .forms import DeviceForm

def device_list(request):
    devices = Device.objects.all()
    return render(request, 'scanner/device_list.html', {'devices': devices})

def device_create(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('device-list')
    else:
        form = DeviceForm()
    return render(request, 'scanner/device_form.html', {'form': form})

def device_edit(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('device-list')
    else:
        form = DeviceForm(instance=device)
    return render(request, 'scanner/device_form.html', {'form': form})

def device_delete(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == 'POST':
        device.delete()
        return redirect('device-list')
    return render(request, 'scanner/device_confirm_delete.html', {'device': device})


def export_devices_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="devices.csv"'

    writer = csv.writer(response)
    # Header row
    writer.writerow(['Device ID', 'Category', 'Assigned?', 'Assigned To', 'Room Number', 'Block',
                     'Status', 'Serial Number', 'Tag Number', 'Date Acquired',
                     'Engraved?', 'Engravement Number', 'Brand'])

    devices = Device.objects.all()
    for d in devices:
        writer.writerow([
            d.device_id, d.category, d.assigned, d.assigned_to, d.room_number, d.block,
            d.status, d.serial_number, d.tag_number, d.date_acquired,
            d.engraved, d.engravement_number, d.brand
        ])
    return response
