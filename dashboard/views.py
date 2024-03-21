from django.shortcuts import render
from .models import DigitalForensicHub


def home(request):
    hubs = DigitalForensicHub.objects.all()

    hub_charts = [{
        'hub_index': {
            'CDFH Kent': 1,
            'CDFH Essex': 2,
            'DFH Maidstone': 3,
            'DFH Harlow': 4,
            'DFH Medway': 5,
            'DFH Colchester': 6,
            'DFH Folkestone': 7,
            'DFH Southend': 8
        }.get(hub.name, 0),
        'hub_name': hub.name,
        'authorised': hub.submissions_authorised,
        'pending': hub.submissions_pending,
        'processing': hub.submissions_processing,
        'holding': hub.submissions_holding,
        'completed': hub.submissions_completed
    } for hub in hubs]

    hub_charts_sorted = sorted(hub_charts, key=lambda x: x['hub_index'])

    return render(request, 'home.html', context={'hub_charts': hub_charts_sorted})
