from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from jinja2 import Markup
from wagtail.wagtailcore.blocks import (
    StructBlock, CharBlock, RichTextBlock, ChoiceBlock, StreamBlock, ListBlock,
    BooleanBlock, PageChooserBlock, URLBlock)
from wagtail.wagtailcore.rich_text import RichText
from wagtail.wagtailimages.blocks import ImageChooserBlock

from .constants import WIDTH_RATIOS


# TODO: Report to wagtail that:
#       - labels should be `capfirst`ed when rendered
#       - `RichTextBlock` has a wrong toolbar position
#       - non-standard spaces are replaced with standard spaces in RichText
# FIXME: FixedRichText & FixedRichTextBlock are a workaround to this issue:
#        https://github.com/torchbox/wagtail/issues/2336

class FixedRichText(RichText):
    def __bool__(self):
        return bool(self.source)


class FixedRichTextBlock(RichTextBlock):
    def to_python(self, value):
        return FixedRichText(value)


# FIXME: Remove when this issue is fixed:
#        https://github.com/torchbox/wagtail/issues/2330
class FixedJinja2Mixin:
    def render(self, value):
        return Markup(super(FixedJinja2Mixin, self).render(value))


class AnchorBlock(FixedJinja2Mixin, CharBlock):
    class Meta:
        label = _('Anchor')
        template = 'noripyt/include/anchor_block.html'


class ButtonBlock(FixedJinja2Mixin, StructBlock):
    TYPES = (
        ('default', _('Default')),
        ('primary', _('Primary')),
    )
    type = ChoiceBlock(choices=TYPES, default='default', label=_('Type'))
    page = PageChooserBlock(required=False, label=_('Page'))
    text = CharBlock(required=False, label=_('Text'))
    url = URLBlock(required=False, label=_('URL'))
    anchor = CharBlock(
        required=False, label=_('Anchor'),
        help_text=_('Anchor of the element in the linked page.'))
    full_width = BooleanBlock(required=False, label=_('Full width'))

    class Meta:
        label = _('Button')
        template = 'noripyt/include/button_block.html'

    def clean(self, value):
        out = super(ButtonBlock, self).clean(value)
        if value['page']:
            if value['url']:
                msg = _('Cannot fill both “Page” and “URL”.')
                raise ValidationError(msg, params={'page': [msg],
                                                   'url': [msg]})
        elif bool(value['url']) ^ bool(value['text']):
            msg = _('“URL” and “Text” must be filled together.')
            raise ValidationError(msg, params={'url': [msg], 'text': [msg]})
        return out


class CardBlock(FixedJinja2Mixin, StructBlock):
    TYPES = (
        ('default', _('Default')),
        ('primary', _('Primary')),
    )
    type = ChoiceBlock(choices=TYPES, default='default', label=_('Type'))
    title = CharBlock(label=_('Title'))
    body = FixedRichTextBlock(required=False, label=_('Body'))
    buttons = ListBlock(ButtonBlock(required=False), label=_('Buttons'))

    class Meta:
        label = _('Card')
        template = 'noripyt/include/card_block.html'


class ShowcaseBlock(FixedJinja2Mixin, StructBlock):
    title = CharBlock(label=_('Title'))
    subtitle = CharBlock(required=False, label=_('Subtitle'))
    image = ImageChooserBlock(label=_('Image'))
    description = FixedRichTextBlock(required=False, label=_('Description'))
    width_ratio = ChoiceBlock(
        default='4/3', choices=[(r, r) for r in WIDTH_RATIOS],
        label=_('Width ratio'))

    class Meta:
        label = _('Showcase')
        template = 'noripyt/include/showcase_block.html'

    @staticmethod
    def get_image_resizing(width_ratio, container_width=1170):
        num, den = map(int, width_ratio.split('/'))
        width_ratio = num / den
        return 'fill-%dx%d' % (container_width, container_width / width_ratio)


class ColumnBlock(FixedJinja2Mixin, StructBlock):
    COL_COUNT = 12
    COL_CHOICES = [(i, '%d %%' % ((100 * i) // 12))
                   for i in range(COL_COUNT + 1)]
    width_xs = ChoiceBlock(choices=COL_CHOICES[1:], required=True, default=12,
                           label=_('Width [extra-small]'))
    width_sm = ChoiceBlock(choices=COL_CHOICES[1:], required=True, default=6,
                           label=_('Width [small]'))
    width_md = ChoiceBlock(choices=COL_CHOICES[1:], required=True, default=6,
                           label=_('Width [medium]'))
    width_lg = ChoiceBlock(choices=COL_CHOICES[1:], required=True, default=4,
                           label=_('Width [large]'))
    offset_xs = ChoiceBlock(
        choices=COL_CHOICES[:-1], label=_('Offset [extra-small]'),
        required=True, default=0)
    offset_sm = ChoiceBlock(
        choices=COL_CHOICES[:-1], label=_('Offset [small]'),
        required=True, default=0)
    offset_md = ChoiceBlock(
        choices=COL_CHOICES[:-1], label=_('Offset [medium]'),
        required=True, default=0)
    offset_lg = ChoiceBlock(
        choices=COL_CHOICES[:-1], label=_('Offset [large]'),
        required=True, default=0)
    body = StreamBlock([
        ('card', CardBlock()),
        ('showcase', ShowcaseBlock()),
        ('text', FixedRichTextBlock()),
    ], required=True, label=_('Body'))

    class Meta:
        label = _('Column')
        template = 'noripyt/include/column_block.html'

    def clean(self, value):
        out = super(ColumnBlock, self).clean(value)
        for screen_size in ('xs', 'sm', 'md', 'lg'):
            width = 'width_' + screen_size
            offset = 'offset_' + screen_size
            if int(value[width]) + int(value[offset]) > self.COL_COUNT:
                msg = _('“{}” + “{}” cannot exceed 100%.').format(
                    self.child_blocks[width].label,
                    self.child_blocks[offset].label,
                )
                raise ValidationError(msg, params={width: [msg],
                                                   offset: [msg]})
        return out


class RowBlock(FixedJinja2Mixin, StructBlock):
    height_xs = CharBlock(required=False, label=_('Height [extra-small]'))
    height_sm = CharBlock(required=False, label=_('Height [small]'))
    height_md = CharBlock(required=False, label=_('Height [medium]'))
    height_lg = CharBlock(required=False, label=_('Height [large]'))
    columns = ListBlock(ColumnBlock(), label=_('Columns'))

    class Meta:
        label = _('Row')
        template = 'noripyt/include/row_block.html'
