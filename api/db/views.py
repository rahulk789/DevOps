from django.shortcuts import render

from db.models import stats

def jsonout(request, pk):
    stats_obj = stats.objects.get(pk=pk)
    context = {
        "data":stats.objs,
    }
    return( request, "stats_detail.html", context)
