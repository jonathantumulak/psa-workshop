
from social_core.pipeline.partial import partial

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response


def send_email_verification(strategy, backend, code, token):
    url = '{0}?verification_code={1}&partial_token={2}'.\
        format(
            reverse('social:complete', args=(backend.name,)), code.code,
            token)
    # send email containing verification url
    print url


@partial
def get_username(backend, user=None, *args, **kwargs):
    if not user:
        data = backend.strategy.request_data()
        if data.get('username') is None:
            return render_to_response('project/pick_username.html')
        else:
            print data.get('username')
            # The user selected a new
            return {'username': data.get('username')}
