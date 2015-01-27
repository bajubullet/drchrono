from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UiForm(models.Model):
    author = models.ForeignKey('auth.User', verbose_name=_('author'))
    title = models.CharField(_('title'), max_length=255)
    is_active = models.BooleanField(_('is active'), default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s - %s' % (self.author, self.title)

    def get_absolute_url(self):
        return reverse('render_form', kwargs={'form_id': self.id})


class FormFields(models.Model):
    BOOLEAN_FIELD = 'bool'
    INTEGER_FIELD = 'int'
    FORM_FIELD_CHOICES = (
        (BOOLEAN_FIELD, 'Boolean Field'),
        (INTEGER_FIELD, 'Integer Field'),
    )
    field_type = models.CharField(_('field type'), choices=FORM_FIELD_CHOICES,
        max_length=5)
    field_name = models.CharField(_('field name'), max_length=50)
    field_label = models.CharField(_('field label'), null=True, blank=True,
        max_length=255)
    field_desc = models.TextField(_('field description'), null=True, blank=True)
    form = models.ForeignKey(UiForm, verbose_name=_('form'))

    def __unicode__(self):
        return '%s - %s' % (str(self.form), self.field_name)
