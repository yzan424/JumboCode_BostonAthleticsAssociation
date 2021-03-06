from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.core import serializers
from django.db.models import Q

from api.models import *
from api.serializers import *

import datetime


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        first_name = token.user.get_short_name()


        # return the team captain that just logged in successfully
        team_cap = Volunteer.objects.filter(name=first_name)


        # filter the attendees passed upon the team captain
        qs = Attendee.objects.filter(team_captain__name=team_cap)

        serializer = AttendeeSerializer(qs, many=True)

        time = datetime.datetime.now()

        captain_name = token.user.get_username().replace(".", " ")

        team_cap = Volunteer.objects.filter(name=captain_name)
        event = Event.objects.filter(Q(date=(datetime.date.today() - datetime.timedelta(days=1))) |
                                     Q(date=datetime.date.today()) |
                                     Q(date=(datetime.date.today() + datetime.timedelta(days=1))))  #but assumes only 1 event per day

        volunteers = Attendee.objects.filter(team_captain=team_cap, event=event)

        serializer = AttendeeSerializer(volunteers, many=True)

        #date time NOT in Eastern time
        #time = datetime.datetime.now()
        # datetime.today.().date

        # signing in only on the day of the event, compare that time
        # to the time in the db, get the event that is occurring on that day/during that time
        # (closest future event)
        # filter attendees based on team captain and event

        #TODO still need to filter by event date

        # return the attendees for the teamp captain along with token information
        return Response({'token': token.key, 'first_name': first_name, 'volunteers':serializer.data})