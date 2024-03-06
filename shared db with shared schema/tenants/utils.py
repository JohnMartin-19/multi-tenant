from sqlite3 import Connection
from .models import Tenant

def hostname_from_request(request):
    #split on ':' to remove  the port number if present.
    return request.get_host().split(':')[0].lower()

def tenant_from_request(request):
    hostname = hostname_from_request(request)
    subdomain_prefix = hostname.split('.')[0]

    return Tenant.objects.filter(subdomain=subdomain_prefix).first()

def tenant_schema_from_request(request):
    hostname = hostname_from_request(request)
    tenants_map = get_tenants_map.get()
    return tenants_map.get(hostname, None)


def set_tenant_schema_for_request(request):
    schema = tenant_schema_from_request(request)
    with Connection.cursor() as cursor:
        cursor.execute(f'SET search_path to {schema}')
def get_tenants_map():
    return{
        'thor.polls.local':'Thor',
        'potter.polls.local':"potter",
    }

