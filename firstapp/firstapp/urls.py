from django.conf.urls import include, url
from django.contrib import admin
from registration.forms import RegistrationFormUniqueEmail
from registration.backends.default.views import RegistrationView

urlpatterns = [
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    url(r'^fridgeroom/', include('fridgeroom.urls', namespace="room")),
    url(r'^novels/', include('novels.urls', namespace="novels")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^polls/', include('polls.urls', namespace="polls")),	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^comments/', include('django_comments.urls')),
]
