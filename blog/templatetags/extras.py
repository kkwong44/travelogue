'''
Extras - Function to deal pagination with filter
'''
from django import template

register = template.Library()


@register.simple_tag
def page_url(value, field_name, urlencode=None):
    '''
    Rewrite URL to include page number and filter
    '''
    string = '?{}={}'
    url = string.format(field_name, value)

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(
            lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        string = '{}&{}'
        url = string.format(url, encoded_querystring)

    return url
