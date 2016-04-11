from django.db.models import (
    URLField, CharField, Model, SET_NULL, ForeignKey)
from django.shortcuts import redirect
from django.utils.translation import (
    get_language_from_request, activate, ugettext_lazy as _)
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, PageChooserPanel, StreamFieldPanel)
from wagtail.wagtailcore.blocks import RichTextBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page

from .blocks import ShowcaseBlock, AnchorBlock, CardBlock, RowBlock
from .constants import ICONS


class LanguageRedirectionPage(Page):
    subpage_types = [
        'noripyt.HomePage',
    ]

    def serve(self, request, *args, **kwargs):
        language = get_language_from_request(request)
        return redirect(self.url + language + '/')


class TranslatablePageMixin(Model):
    # FIXME: Change this field to OneToOneField once this issue has been fixed:
    #        https://code.djangoproject.com/ticket/26320
    french_page = ForeignKey(
        Page, on_delete=SET_NULL, null=True, blank=True, related_name='+',
        verbose_name=_('french page'))

    settings_panels = Page.settings_panels + [
        PageChooserPanel('french_page'),
    ]

    class Meta:
        abstract = True

    def get_language(self):
        if not hasattr(self, '_language'):
            sub_language_page_depth = (
                self.get_ancestors().type(LanguageRedirectionPage)
                .order_by('-depth').first().depth + 1)
            language = self.get_ancestors(inclusive=True).only('slug').get(
                depth=sub_language_page_depth)
            self._language = language.slug
        return self._language

    @property
    def english_page(self):
        if self.french_page_id is not None:
            return self
        return self.__class__.objects.filter(french_page=self).first()

    def get_for_lang(self, lang_code):
        if lang_code == 'en':
            return self.english_page
        if lang_code == 'fr':
            return self.french_page
        raise ValueError('`%s` is not in `LANGUAGES`.' % lang_code)

    def serve(self, request, *args, **kwargs):
        activate(self.get_language())
        return super(TranslatablePageMixin, self).serve(request)


class HomePage(TranslatablePageMixin, Page):
    body = StreamField([
        ('text', RichTextBlock(label=_('Text'))),
        ('anchor', AnchorBlock()),
        ('card', CardBlock()),
        ('showcase', ShowcaseBlock()),
        ('row', RowBlock()),
    ], verbose_name=_('body'))

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
    subpage_types = [
        'noripyt.Article', 'noripyt.RedirectPage',
    ]


class Article(TranslatablePageMixin, Page):
    body = StreamField([
        ('text', RichTextBlock(label=_('Text'))),
        ('anchor', AnchorBlock()),
        ('card', CardBlock()),
        ('showcase', ShowcaseBlock()),
        ('row', RowBlock()),
    ], verbose_name=_('body'))

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
    subpage_types = [
        'noripyt.Article', 'noripyt.RedirectPage',
    ]


class RedirectPage(Page):
    redirect_url = URLField(_('redirect URL'))
    icon = CharField(_('icon'), max_length=22, blank=True,
                     choices=[(i, i) for i in ICONS])

    content_panels = Page.content_panels + [
        FieldPanel('redirect_url'),
        FieldPanel('icon'),
    ]
    subpage_types = []

    def serve(self, request, *args, **kwargs):
        return redirect(self.redirect_url)
