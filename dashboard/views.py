from django.shortcuts import render
from .models import DigitalForensicHub


# Create your views here.


def home(request):
    hubs = DigitalForensicHub.objects.all()

    cdfh_k_status_labels = ['CDFH K Authorised', 'CDFH K Processing', 'CDFH K Holding', 'CDFH K Completed']

    cdfh_k_status_count = [hubs[0].submissions_authorised,
                           hubs[0].submissions_processing,
                           hubs[0].submissions_holding,
                           hubs[0].submissions_completed]

    cdfh_e_status_labels = ['CDFH E Authorised', 'CDFH E Processing', 'CDFH E Holding', 'CDFH E Completed']

    cdfh_e_status_count = [hubs[1].submissions_authorised,
                           hubs[1].submissions_processing,
                           hubs[1].submissions_holding,
                           hubs[1].submissions_completed]

    dfh_kw_status_labels = ['DFH KW Authorised', 'DFH KW Processing', 'DFH KW Holding', 'DFH KW Completed']

    dfh_kw_status_count = [hubs[2].submissions_authorised,
                           hubs[2].submissions_processing,
                           hubs[2].submissions_holding,
                           hubs[2].submissions_completed]

    dfh_kn_status_labels = ['DFH KN Authorised', 'DFH KN Processing', 'DFH KN Holding', 'DFH KN Completed']

    dfh_kn_status_count = [hubs[3].submissions_authorised,
                           hubs[3].submissions_processing,
                           hubs[3].submissions_holding,
                           hubs[3].submissions_completed]

    dfh_ke_status_labels = ['DFH KE Authorised', 'DFH KE Processing', 'DFH KE Holding', 'DFH KE Completed']

    dfh_ke_status_count = [hubs[4].submissions_authorised,
                           hubs[4].submissions_processing,
                           hubs[4].submissions_holding,
                           hubs[4].submissions_completed]

    dfh_ew_status_labels = ['DFH EW Authorised', 'DFH EW Processing', 'DFH EW Holding', 'DFH EW Completed']

    dfh_ew_status_count = [hubs[5].submissions_authorised,
                           hubs[5].submissions_processing,
                           hubs[5].submissions_holding,
                           hubs[5].submissions_completed]

    dfh_en_status_labels = ['DFH EN Authorised', 'DFH EN Processing', 'DFH EN Holding', 'DFH EN Completed']

    dfh_en_status_count = [hubs[6].submissions_authorised,
                           hubs[6].submissions_processing,
                           hubs[6].submissions_holding,
                           hubs[6].submissions_completed]

    dfh_es_status_labels = ['DFH ES Authorised', 'DFH ES Processing', 'DFH ES Holding', 'DFH ES Completed']

    dfh_es_status_count = [hubs[7].submissions_authorised,
                           hubs[7].submissions_processing,
                           hubs[7].submissions_holding,
                           hubs[7].submissions_completed]

    context = {
        # All Digital Forensic Hubs
        'hubs': hubs,

        # CDFH Kent
        'cdfh_k_status_labels': cdfh_k_status_labels,
        'cdfh_k_status_count': cdfh_k_status_count,

        # CDFH Essex
        'cdfh_e_status_labels': cdfh_e_status_labels,
        'cdfh_e_status_count': cdfh_e_status_count,

        # DFH Maidstone
        'dfh_kw_status_labels': dfh_kw_status_labels,
        'dfh_kw_status_count': dfh_kw_status_count,

        # DFH Medway
        'dfh_kn_status_labels': dfh_kn_status_labels,
        'dfh_kn_status_count': dfh_kn_status_count,

        # DFH Folkestone
        'dfh_ke_status_labels': dfh_ke_status_labels,
        'dfh_ke_status_count': dfh_ke_status_count,

        # DFH Harlow
        'dfh_ew_status_labels': dfh_ew_status_labels,
        'dfh_ew_status_count': dfh_ew_status_count,

        # DFH Colchester
        'dfh_en_status_labels': dfh_en_status_labels,
        'dfh_en_status_count': dfh_en_status_count,

        # DFH Southend
        'dfh_es_status_labels': dfh_es_status_labels,
        'dfh_es_status_count': dfh_es_status_count

        # Temp
    }

    return render(request, 'home.html', context)
