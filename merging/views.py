import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests

class MergingViews:

    def __init__(self):
        pass

    def index_view(self, request):
        template = 'index.html'
        return render(request, template)

    def find_organizations(self, name):
        api_url = 'https://admin.leader-id.ru/api/v4/admin/organizations'
        headers = {'Authorization': f'Bearer {os.getenv("API_TOKEN")}'}
        params = {'name': f"{name}", 'paginationSize': 1000}
        response = requests.get(api_url, params=params, headers=headers)
        data = response.json().get('data', None).get('_items', None)
        return data

    def merge_organizations(self, org_ids, preferred_org_id):
        api_url = 'https://leader-id.ru/api/v4/admin/organizations/merge'
        headers = {'Authorization': f'Bearer {os.getenv("API_TOKEN")}'}
        data = {
            'orgIds': org_ids,
            'preferredOrgId': preferred_org_id
        }
        response = requests.post(api_url, json=data, headers=headers)
        return response.json()

    def show_org_view(self, request):
        orgs = self.find_organizations(request.GET.get('name'))
        template = 'show_orgs.html'
        context = {
            'orgs': enumerate(orgs, start=1)
        }
        return render(request, template, context)

    def show_orgs_to_merge_view(self, request):
        if request.method == 'POST':
            selected_orgs = request.POST.getlist('selectedOrgs')

            all_orgs_id = request.POST.getlist('allOrgsId')
            all_orgs_name = request.POST.getlist('allOrgsName')

            all_orgs = dict(zip(all_orgs_id, all_orgs_name))
            orgs_to_merge = []
            for org_id, org_name in all_orgs.items():
                if org_id not in selected_orgs:
                    org_to_merge = {
                        'id': org_id,
                        'name': org_name
                    }
                    orgs_to_merge.append(org_to_merge)
            template = 'preview_orgs.html'
            context = {
                'orgs': enumerate(orgs_to_merge, start=1)
            }
            return render(request, template, context)

        else:
            return HttpResponse('Метод не разрешен', status=405)

    def merge_orgs_view(self, request):
        if request.method == 'POST':
            orgs_to_merge = request.POST.getlist('orgIds')[0].split(',')
            preffered_org = request.POST.get('id')
            errors = []
            error_count = 0
            if preffered_org in orgs_to_merge:
                orgs_to_merge.remove(preffered_org)
            for org in orgs_to_merge:
                merge_result = self.merge_organizations([int(org)], int(preffered_org))
                if merge_result.get('errors'):
                    errors.append(merge_result.get('errors'))
                    error_count += 1
            template = 'merge_orgs.html'
            context = {
                'errors': errors,
                'error_count' : error_count,
            }
            return render(request, template, context)
        else:
            return HttpResponse('Метод не разрешен', status=405)