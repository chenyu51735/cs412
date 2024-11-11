from django.shortcuts import render
# Create your views here.
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

import plotly
import plotly.graph_objects as go

from typing import Any
from datetime import date
from plotly.offline import plot


class VotersListView(ListView):
    '''View to display Voter results'''

    template_name = 'voter_analytics/voters.html'
    model = Voter
    context_object_name = 'voters'
    paginate_by = 100

    def get_queryset(self):
        '''Customize the queryset based on GET parameters'''
        qs = super().get_queryset()
        request = self.request

        # Retrieve search parameters
        party = request.GET.get('party_affiliation')
        min_birth_year = request.GET.get('min_birth_year')
        max_birth_year = request.GET.get('max_birth_year')
        voter_score = request.GET.get('voter_score')

        # Election checkboxes
        v20state = request.GET.get('v20state', '')
        v21town = request.GET.get('v21town', '')
        v21primary = request.GET.get('v21primary', '')
        v22general = request.GET.get('v22general', '')
        v23town = request.GET.get('v23town', '')

        # Filter by Party Affiliation
        if party:
            qs = qs.filter(party_affiliation=party)

        # Filter by Minimum Birth Year
        if min_birth_year:
            qs = qs.filter(dob__year__gte=min_birth_year)

        # Filter by Maximum Birth Year
        if max_birth_year:
            qs = qs.filter(dob__year__lte=max_birth_year)

        # Filter by Voter Score
        if voter_score:
            qs = qs.filter(voter_score=voter_score)

        # Filter by past Elections
        if v20state:
            qs = qs.filter(v20state="TRUE")
        if v21town:
            qs = qs.filter(v21town="TRUE")
        if v21primary:
            qs = qs.filter(v21primary="TRUE")
        if v22general:
            qs = qs.filter(v22general="TRUE")
        if v23town:
            qs = qs.filter(v23town="TRUE")

        return qs
    
    def get_context_data(self, **kwargs):

        '''Add additional context for template rendering'''

        context = super().get_context_data(**kwargs)
        request = self.request
        context['search_params'] = {
            'party_affiliation': request.GET.get('party_affiliation', ''),
            'min_birth_year': request.GET.get('min_birth_year', ''),
            'max_birth_year': request.GET.get('max_birth_year', ''),
            'voter_score': request.GET.get('voter_score', ''),
            'v20state': request.GET.get('v20state', ''),
            'v21town': request.GET.get('v21town', ''),
            'v21primary': request.GET.get('v21primary', ''),
            'v22general': request.GET.get('v22general', ''),
            'v23town': request.GET.get('v23town', ''),
        }

        return context

class ShowVoterView(DetailView):
    '''the view ot show a single voter'''
    model = Voter
    template_name = 'voter_analytics/show_voter.html'
    context_object_name = 'voter'


class VoterGraphsView(ListView):
    model = Voter
    template_name = 'voter_analytics/graphs.html'
    context_object_name = 'voters'

    def get_queryset(self):
        '''Customize the queryset based on GET parameters'''
        qs = super().get_queryset()
        request = self.request

        # Retrieve search parameters
        party = request.GET.get('party_affiliation')
        min_birth_year = request.GET.get('min_birth_year')
        max_birth_year = request.GET.get('max_birth_year')
        voter_score = request.GET.get('voter_score')

        # Election checkboxes
        v20state = request.GET.get('v20state', '')
        v21town = request.GET.get('v21town', '')
        v21primary = request.GET.get('v21primary', '')
        v22general = request.GET.get('v22general', '')
        v23town = request.GET.get('v23town', '')

        # Filter by Party Affiliation
        if party:
            qs = qs.filter(party_affiliation=party)

        # Filter by Minimum Birth Year
        if min_birth_year:
            qs = qs.filter(dob__year__gte=min_birth_year)

        # Filter by Maximum Birth Year
        if max_birth_year:
            qs = qs.filter(dob__year__lte=max_birth_year)

        # Filter by Voter Score
        if voter_score:
            qs = qs.filter(voter_score=voter_score)

        # Filter by past Elections
        if v20state:
            qs = qs.filter(v20state="TRUE")
        if v21town:
            qs = qs.filter(v21town="TRUE")
        if v21primary:
            qs = qs.filter(v21primary="TRUE")
        if v22general:
            qs = qs.filter(v22general="TRUE")
        if v23town:
            qs = qs.filter(v23town="TRUE")

        return qs
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        # get the superclass version of context
        context = super().get_context_data(**kwargs)
        voters = self.get_queryset()
        request = self.request
        total = voters.count()
        context['total'] = total
        context['search_params'] = {
            'party_affiliation': request.GET.get('party_affiliation', ''),
            'min_birth_year': request.GET.get('min_birth_year', ''),
            'max_birth_year': request.GET.get('max_birth_year', ''),
            'voter_score': request.GET.get('voter_score', ''),
            'v20state': request.GET.get('v20state', ''),
            'v21town': request.GET.get('v21town', ''),
            'v21primary': request.GET.get('v21primary', ''),
            'v22general': request.GET.get('v22general', ''),
            'v23town': request.GET.get('v23town', ''),
        }

        # Histogram for voters' birth year
        current_year = date.today().year
        context['years'] = range(1924, current_year + 1)
        context['scores'] = range(1, 6)
        context['Voter'] = Voter
        birth_years = voters.values_list('dob__year', flat=True)
        birth_year_counts = {}
        for year in birth_years:
            if year:
                birth_year_counts[year] = birth_year_counts.get(year, 0) + 1

        fig1 = go.Figure(data=[go.Bar(
            x=list(birth_year_counts.keys()),
            y=list(birth_year_counts.values())
        )])
        fig1.update_layout(title=f'Distribution of Voters by Year of Birth (n={total})',
                           xaxis_title='Year of Birth',
                           yaxis_title='Number of Voters')
        
        context['birth_year_hist'] = plot(fig1, output_type='div')

        # Pie chart for voters' party affiliation
        party_affiliations = voters.values_list('party_affiliation', flat=True)
        party_counts = {}
        for party in party_affiliations:
            if party:
                party_counts[party] = party_counts.get(party, 0) + 1

        fig2 = go.Figure(data=[go.Pie(
            labels=list(party_counts.keys()),
            values=list(party_counts.values())
        )])
        fig2.update_layout(title=f'Distribution of Voters by Party Affiliation (n={total})')
        context['party_affiliation_pie'] = plot(fig2, output_type='div')

        # Histogram for voters' past election
        elections = {
            '2020 State Election': 'v20state',
            '2021 Town Election': 'v21town',
            '2021 Primary Election': 'v21primary',
            '2022 General Election': 'v22general',
            '2023 Town Election': 'v23town',
        }
        election_counts = {}
        for election_name, field in elections.items():
            count = voters.filter(**{field: "TRUE"}).count()
            election_counts[election_name] = count

        fig3 = go.Figure(data=[go.Bar(
            x=list(election_counts.keys()),
            y=list(election_counts.values())
        )])
        fig3.update_layout(title=f'Voter Participation by Election (n={total})',
                           xaxis_title='Election',
                           yaxis_title='Number of Voters')
        context['election_participation_hist'] = plot(fig3, output_type='div')

        return context