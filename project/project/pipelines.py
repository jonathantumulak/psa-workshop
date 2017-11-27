
from django.core.urlresolvers import reverse


def send_email_verification(strategy, backend, code, token):
    url = '{0}?verification_code={1}&partial_token={2}'.\
        format(
            reverse('social:complete', args=(backend.name,)), code.code,
            token)

    # send email containing verification url
    print url
