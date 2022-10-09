from django.shortcuts import render

from db.models import statslist

def jsonout(request, pk):
    statslist_obj = statslist.objects.get(pk=pk)
    context = {
        "data":statslist.objs,
    }
    return( request, "stats_detail.html", context)
