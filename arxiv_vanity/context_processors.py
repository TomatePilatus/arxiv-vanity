from django.conf import settings


# Some extra settings in templates that Django doesn't do for us
def extra_settings(request):
    return {
        "GOOGLE_ANALYTICS_PROPERTY_ID": settings.GOOGLE_ANALYTICS_PROPERTY_ID,
        "MIXPANEL_TOKEN": settings.MIXPANEL_TOKEN,
        "ROOT_URL": settings.ROOT_URL,
    }
