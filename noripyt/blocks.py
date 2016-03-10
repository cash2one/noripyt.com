from django.utils.translation import ugettext_lazy as _
from jinja2 import Markup
from wagtail.wagtailcore.blocks import (
    StructBlock, CharBlock, RichTextBlock, ChoiceBlock, StreamBlock, ListBlock)
from wagtail.wagtailcore.rich_text import RichText
from wagtail.wagtailimages.blocks import ImageChooserBlock


# FIXME: FixedRichText & FixedRichTextBlock are a workaround to this issue:
#        https://github.com/torchbox/wagtail/issues/2336

class FixedRichText(RichText):
    def __bool__(self):
        return bool(self.source)


class FixedRichTextBlock(RichTextBlock):
    def to_python(self, value):
        return FixedRichText(value)


class ShowcaseBlock(StructBlock):
    # TODO: Report to wagtail that labels should be `capfirst`ed when rendered.
    title = CharBlock(label=_('Title'))
    subtitle = CharBlock(required=False, label=_('Subtitle'))
    image = ImageChooserBlock(label=_('Image'))
    # TODO: Report to wagtail that RichTextBlock has a wrong toolbar position.
    description = FixedRichTextBlock(required=False, label=_('Description'))

    class Meta:
        label = _('Showcase')
        template = 'noripyt/include/showcase_block.html'

    def render(self, value):
        return Markup(super(ShowcaseBlock, self).render(value))

    @property
    def has_description(self):
        return bool(self.description.value)


class ColumnBlock(StructBlock):
    WIDTH_CHOICES = [(i, '%d %%' % ((100 * i) // 12)) for i in range(1, 13)]
    width = ChoiceBlock(choices=WIDTH_CHOICES, required=True, default=6,
                        label=_('Width'))
    body = StreamBlock([
        ('showcase', ShowcaseBlock()),
        ('text', FixedRichTextBlock()),
    ], required=True, label=_('Body'))

    class Meta:
        label = _('Column')
        template = 'noripyt/include/column_block.html'

    def render(self, value):
        return Markup(super(ColumnBlock, self).render(value))


class RowBlock(ListBlock):
    class Meta:
        label = _('Row')
        template = 'noripyt/include/row_block.html'

    def render(self, value):
        return Markup(super(RowBlock, self).render(value))


row_block = RowBlock(ColumnBlock())