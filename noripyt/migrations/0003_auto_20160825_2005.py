# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 18:05
from __future__ import unicode_literals

from django.db import migrations
import noripyt.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('noripyt', '0002_auto_20160411_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('text', wagtail.wagtailcore.blocks.RichTextBlock(label='Text')), ('anchor', noripyt.blocks.AnchorBlock()), ('card', wagtail.wagtailcore.blocks.StructBlock((('type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('default', 'Default'), ('primary', 'Primary')], default='default', label='Type')), ('title', wagtail.wagtailcore.blocks.CharBlock(label='Title')), ('body', wagtail.wagtailcore.blocks.RichTextBlock(label='Body', required=False)), ('buttons', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('default', 'Default'), ('primary', 'Primary')], default='default', label='Type')), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(label='Page', required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(label='Text', required=False)), ('url', wagtail.wagtailcore.blocks.URLBlock(label='URL', required=False)), ('anchor', wagtail.wagtailcore.blocks.CharBlock(help_text='Anchor of the element in the linked page.', label='Anchor', required=False)), ('full_width', wagtail.wagtailcore.blocks.BooleanBlock(label='Full width', required=False))), required=False), label='Buttons'))))), ('showcase', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(label='Title')), ('subtitle', wagtail.wagtailcore.blocks.CharBlock(label='Subtitle', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Image')), ('description', wagtail.wagtailcore.blocks.RichTextBlock(label='Description', required=False)), ('width_ratio', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('1/2', '1/2'), ('2/3', '2/3'), ('3/4', '3/4'), ('1/1', '1/1'), ('4/3', '4/3'), ('3/2', '3/2'), ('5/3', '5/3'), ('16/9', '16/9'), ('2/1', '2/1'), ('3/1', '3/1'), ('4/1', '4/1')], default='4/3', label='Width ratio'))))), ('row', wagtail.wagtailcore.blocks.StructBlock((('height_xs', wagtail.wagtailcore.blocks.CharBlock(label='Height [extra-small]', required=False)), ('height_sm', wagtail.wagtailcore.blocks.CharBlock(label='Height [small]', required=False)), ('height_md', wagtail.wagtailcore.blocks.CharBlock(label='Height [medium]', required=False)), ('height_lg', wagtail.wagtailcore.blocks.CharBlock(label='Height [large]', required=False)), ('columns', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('width_xs', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%'), (12, '100\u202f%')], default=12, label='Width [extra-small]')), ('width_sm', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%'), (12, '100\u202f%')], default=6, label='Width [small]')), ('width_md', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%'), (12, '100\u202f%')], default=6, label='Width [medium]')), ('width_lg', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%'), (12, '100\u202f%')], default=4, label='Width [large]')), ('offset_xs', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(0, '0\u202f%'), (1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%')], default=0, label='Offset [extra-small]')), ('offset_sm', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(0, '0\u202f%'), (1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%')], default=0, label='Offset [small]')), ('offset_md', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(0, '0\u202f%'), (1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%')], default=0, label='Offset [medium]')), ('offset_lg', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(0, '0\u202f%'), (1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%')], default=0, label='Offset [large]')), ('body', wagtail.wagtailcore.blocks.StreamBlock((('card', wagtail.wagtailcore.blocks.StructBlock((('type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('default', 'Default'), ('primary', 'Primary')], default='default', label='Type')), ('title', wagtail.wagtailcore.blocks.CharBlock(label='Title')), ('body', wagtail.wagtailcore.blocks.RichTextBlock(label='Body', required=False)), ('buttons', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('default', 'Default'), ('primary', 'Primary')], default='default', label='Type')), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(label='Page', required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(label='Text', required=False)), ('url', wagtail.wagtailcore.blocks.URLBlock(label='URL', required=False)), ('anchor', wagtail.wagtailcore.blocks.CharBlock(help_text='Anchor of the element in the linked page.', label='Anchor', required=False)), ('full_width', wagtail.wagtailcore.blocks.BooleanBlock(label='Full width', required=False))), required=False), label='Buttons'))))), ('showcase', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(label='Title')), ('subtitle', wagtail.wagtailcore.blocks.CharBlock(label='Subtitle', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Image')), ('description', wagtail.wagtailcore.blocks.RichTextBlock(label='Description', required=False)), ('width_ratio', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('1/2', '1/2'), ('2/3', '2/3'), ('3/4', '3/4'), ('1/1', '1/1'), ('4/3', '4/3'), ('3/2', '3/2'), ('5/3', '5/3'), ('16/9', '16/9'), ('2/1', '2/1'), ('3/1', '3/1'), ('4/1', '4/1')], default='4/3', label='Width ratio'))))), ('text', wagtail.wagtailcore.blocks.RichTextBlock())), label='Body', required=True)))), label='Columns')))))), verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='home',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('text', wagtail.wagtailcore.blocks.RichTextBlock(label='Text')), ('anchor', noripyt.blocks.AnchorBlock()), ('card', wagtail.wagtailcore.blocks.StructBlock((('type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('default', 'Default'), ('primary', 'Primary')], default='default', label='Type')), ('title', wagtail.wagtailcore.blocks.CharBlock(label='Title')), ('body', wagtail.wagtailcore.blocks.RichTextBlock(label='Body', required=False)), ('buttons', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('default', 'Default'), ('primary', 'Primary')], default='default', label='Type')), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(label='Page', required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(label='Text', required=False)), ('url', wagtail.wagtailcore.blocks.URLBlock(label='URL', required=False)), ('anchor', wagtail.wagtailcore.blocks.CharBlock(help_text='Anchor of the element in the linked page.', label='Anchor', required=False)), ('full_width', wagtail.wagtailcore.blocks.BooleanBlock(label='Full width', required=False))), required=False), label='Buttons'))))), ('showcase', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(label='Title')), ('subtitle', wagtail.wagtailcore.blocks.CharBlock(label='Subtitle', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Image')), ('description', wagtail.wagtailcore.blocks.RichTextBlock(label='Description', required=False)), ('width_ratio', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('1/2', '1/2'), ('2/3', '2/3'), ('3/4', '3/4'), ('1/1', '1/1'), ('4/3', '4/3'), ('3/2', '3/2'), ('5/3', '5/3'), ('16/9', '16/9'), ('2/1', '2/1'), ('3/1', '3/1'), ('4/1', '4/1')], default='4/3', label='Width ratio'))))), ('row', wagtail.wagtailcore.blocks.StructBlock((('height_xs', wagtail.wagtailcore.blocks.CharBlock(label='Height [extra-small]', required=False)), ('height_sm', wagtail.wagtailcore.blocks.CharBlock(label='Height [small]', required=False)), ('height_md', wagtail.wagtailcore.blocks.CharBlock(label='Height [medium]', required=False)), ('height_lg', wagtail.wagtailcore.blocks.CharBlock(label='Height [large]', required=False)), ('columns', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('width_xs', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%'), (12, '100\u202f%')], default=12, label='Width [extra-small]')), ('width_sm', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%'), (12, '100\u202f%')], default=6, label='Width [small]')), ('width_md', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%'), (12, '100\u202f%')], default=6, label='Width [medium]')), ('width_lg', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%'), (12, '100\u202f%')], default=4, label='Width [large]')), ('offset_xs', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(0, '0\u202f%'), (1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%')], default=0, label='Offset [extra-small]')), ('offset_sm', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(0, '0\u202f%'), (1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%')], default=0, label='Offset [small]')), ('offset_md', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(0, '0\u202f%'), (1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%')], default=0, label='Offset [medium]')), ('offset_lg', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(0, '0\u202f%'), (1, '8\u202f%'), (2, '16\u202f%'), (3, '25\u202f%'), (4, '33\u202f%'), (5, '41\u202f%'), (6, '50\u202f%'), (7, '58\u202f%'), (8, '66\u202f%'), (9, '75\u202f%'), (10, '83\u202f%'), (11, '91\u202f%')], default=0, label='Offset [large]')), ('body', wagtail.wagtailcore.blocks.StreamBlock((('card', wagtail.wagtailcore.blocks.StructBlock((('type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('default', 'Default'), ('primary', 'Primary')], default='default', label='Type')), ('title', wagtail.wagtailcore.blocks.CharBlock(label='Title')), ('body', wagtail.wagtailcore.blocks.RichTextBlock(label='Body', required=False)), ('buttons', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('default', 'Default'), ('primary', 'Primary')], default='default', label='Type')), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(label='Page', required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(label='Text', required=False)), ('url', wagtail.wagtailcore.blocks.URLBlock(label='URL', required=False)), ('anchor', wagtail.wagtailcore.blocks.CharBlock(help_text='Anchor of the element in the linked page.', label='Anchor', required=False)), ('full_width', wagtail.wagtailcore.blocks.BooleanBlock(label='Full width', required=False))), required=False), label='Buttons'))))), ('showcase', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(label='Title')), ('subtitle', wagtail.wagtailcore.blocks.CharBlock(label='Subtitle', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Image')), ('description', wagtail.wagtailcore.blocks.RichTextBlock(label='Description', required=False)), ('width_ratio', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('1/2', '1/2'), ('2/3', '2/3'), ('3/4', '3/4'), ('1/1', '1/1'), ('4/3', '4/3'), ('3/2', '3/2'), ('5/3', '5/3'), ('16/9', '16/9'), ('2/1', '2/1'), ('3/1', '3/1'), ('4/1', '4/1')], default='4/3', label='Width ratio'))))), ('text', wagtail.wagtailcore.blocks.RichTextBlock())), label='Body', required=True)))), label='Columns')))))), verbose_name='body'),
        ),
    ]
