from django.conf import settings
from django.contrib import admin
from .. import models
from django.utils.translation import gettext_lazy as _
from src.base.admin.mixins import TabbedTranslationAdmin
from captcha import fields
from django.contrib.auth.forms import AuthenticationForm


if settings.RECAPTCHA_PRIVATE_KEY:
    class LoginForm(AuthenticationForm):
        captcha = fields.ReCaptchaField()
    admin.site.login_form = LoginForm
