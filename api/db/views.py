from django.shortcuts import render
import db
from db.models import statslist

def jsonout(request):
    statslist_obj = statslist.objects
    context = {
        "statslist_obj":statslist_obj,
    }
    return render( request, "stats_detail.html", context)
