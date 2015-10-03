# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields
import django.utils.timezone
from django.conf import settings
import cms.models.static_placeholder


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSPlugin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(unique=True, max_length=255, editable=False)),
                ('depth', models.PositiveIntegerField(editable=False)),
                ('numchild', models.PositiveIntegerField(default=0, editable=False)),
                ('position', models.PositiveSmallIntegerField(verbose_name='position', null=True, editable=False, blank=True)),
                ('language', models.CharField(verbose_name='language', max_length=15, editable=False, db_index=True)),
                ('plugin_type', models.CharField(verbose_name='plugin_name', max_length=50, editable=False, db_index=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date', editable=False)),
                ('changed_date', models.DateTimeField(auto_now=True)),
                ('editable_in_content_mode', models.BooleanField(default=True, verbose_name='Is editable in content mode.')),
            ],
        ),
        migrations.CreateModel(
            name='GlobalPagePermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('can_change', models.BooleanField(default=True, verbose_name='can edit')),
                ('can_add', models.BooleanField(default=True, verbose_name='can add')),
                ('can_delete', models.BooleanField(default=True, verbose_name='can delete')),
                ('can_change_advanced_settings', models.BooleanField(default=False, verbose_name='can change advanced settings')),
                ('can_publish', models.BooleanField(default=True, verbose_name='can publish')),
                ('can_change_permissions', models.BooleanField(default=False, help_text='on page level', verbose_name='can change permissions')),
                ('can_move_page', models.BooleanField(default=True, verbose_name='can move')),
                ('can_view', models.BooleanField(default=False, help_text='frontend view restriction', verbose_name='view restricted')),
                ('can_recover_page', models.BooleanField(default=True, help_text='can recover any deleted page', verbose_name='can recover pages')),
            ],
            options={
                'verbose_name': 'Page global permission',
                'verbose_name_plural': 'Pages global permissions',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(unique=True, max_length=255)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('created_by', models.CharField(verbose_name='created by', max_length=255, editable=False)),
                ('changed_by', models.CharField(verbose_name='changed by', max_length=255, editable=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now=True)),
                ('publication_date', models.DateTimeField(help_text='When the page should go live. Status must be "Published" for page to go live.', null=True, verbose_name='publication date', db_index=True, blank=True)),
                ('publication_end_date', models.DateTimeField(help_text='When to expire the page. Leave empty to never expire.', null=True, verbose_name='publication end date', db_index=True, blank=True)),
                ('in_navigation', models.BooleanField(default=True, db_index=True, verbose_name='in navigation')),
                ('soft_root', models.BooleanField(default=False, help_text='All ancestors will not be displayed in the navigation', db_index=True, verbose_name='soft root')),
                ('reverse_id', models.CharField(max_length=40, blank=True, help_text='A unique identifier that is used with the page_url templatetag for linking to this page', null=True, verbose_name='id', db_index=True)),
                ('navigation_extenders', models.CharField(db_index=True, max_length=80, null=True, verbose_name='attached menu', blank=True)),
                ('template', models.CharField(default=b'INHERIT', help_text='The template used to render the content.', max_length=100, verbose_name='template', choices=[(b'one_page_template.html', 'One Page Layout'), (b'one_page_child_template.html', 'One Page Child Layout'), (b'INHERIT', 'Inherit the template of the nearest ancestor')])),
                ('login_required', models.BooleanField(default=False, verbose_name='login required')),
                ('limit_visibility_in_menu', models.SmallIntegerField(default=None, choices=[(1, 'for logged in users only'), (2, 'for anonymous users only')], blank=True, help_text='limit when this page is visible in the menu', null=True, verbose_name='menu visibility', db_index=True)),
                ('is_home', models.BooleanField(default=False, db_index=True, editable=False)),
                ('application_urls', models.CharField(db_index=True, max_length=200, null=True, verbose_name='application', blank=True)),
                ('application_namespace', models.CharField(max_length=200, null=True, verbose_name='application instance name', blank=True)),
                ('publisher_is_draft', models.BooleanField(default=True, db_index=True, editable=False)),
                ('languages', models.CharField(max_length=255, null=True, editable=False, blank=True)),
                ('revision_id', models.PositiveIntegerField(default=0, editable=False)),
                ('xframe_options', models.IntegerField(default=0, choices=[(0, 'Inherit from parent page'), (1, 'Deny'), (2, 'Only this website'), (3, 'Allow')])),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='cms.Page', null=True)),
            ],
            options={
                'ordering': ('path',),
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
                'permissions': (('view_page', 'Can view page'), ('publish_page', 'Can publish page'), ('edit_static_placeholder', 'Can edit static placeholders')),
            },
        ),
        migrations.CreateModel(
            name='PagePermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('can_change', models.BooleanField(default=True, verbose_name='can edit')),
                ('can_add', models.BooleanField(default=True, verbose_name='can add')),
                ('can_delete', models.BooleanField(default=True, verbose_name='can delete')),
                ('can_change_advanced_settings', models.BooleanField(default=False, verbose_name='can change advanced settings')),
                ('can_publish', models.BooleanField(default=True, verbose_name='can publish')),
                ('can_change_permissions', models.BooleanField(default=False, help_text='on page level', verbose_name='can change permissions')),
                ('can_move_page', models.BooleanField(default=True, verbose_name='can move')),
                ('can_view', models.BooleanField(default=False, help_text='frontend view restriction', verbose_name='view restricted')),
                ('grant_on', models.IntegerField(default=5, verbose_name='Grant on', choices=[(1, 'Current page'), (2, 'Page children (immediate)'), (3, 'Page and children (immediate)'), (4, 'Page descendants'), (5, 'Page and descendants')])),
            ],
            options={
                'verbose_name': 'Page permission',
                'verbose_name_plural': 'Page permissions',
            },
        ),
        migrations.CreateModel(
            name='PageUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(related_name='created_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User (page)',
                'verbose_name_plural': 'Users (page)',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='PageUserGroup',
            fields=[
                ('group_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='auth.Group')),
                ('created_by', models.ForeignKey(related_name='created_usergroups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User group (page)',
                'verbose_name_plural': 'User groups (page)',
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Placeholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slot', models.CharField(verbose_name='slot', max_length=255, editable=False, db_index=True)),
                ('default_width', models.PositiveSmallIntegerField(verbose_name='width', null=True, editable=False)),
            ],
            options={
                'permissions': (('use_structure', 'Can use Structure mode'),),
            },
        ),
        migrations.CreateModel(
            name='StaticPlaceholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', help_text='Descriptive name to identify this static placeholder. Not displayed to users.', max_length=255, verbose_name='static placeholder name', blank=True)),
                ('code', models.CharField(help_text='To render the static placeholder in templates.', max_length=255, verbose_name='placeholder code', blank=True)),
                ('dirty', models.BooleanField(default=False, editable=False)),
                ('creation_method', models.CharField(default=b'code', max_length=20, verbose_name='creation_method', blank=True, choices=[(b'template', 'by template'), (b'code', 'by code')])),
                ('draft', cms.models.fields.PlaceholderField(related_name='static_draft', slotname=cms.models.static_placeholder.static_slotname, editable=False, to='cms.Placeholder', null=True, verbose_name='placeholder content')),
                ('public', cms.models.fields.PlaceholderField(related_name='static_public', slotname=cms.models.static_placeholder.static_slotname, editable=False, to='cms.Placeholder', null=True)),
                ('site', models.ForeignKey(blank=True, to='sites.Site', null=True)),
            ],
            options={
                'verbose_name': 'static placeholder',
                'verbose_name_plural': 'static placeholders',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=15, verbose_name='language', db_index=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('page_title', models.CharField(help_text='overwrite the title (html title tag)', max_length=255, null=True, verbose_name='title', blank=True)),
                ('menu_title', models.CharField(help_text='overwrite the title in the menu', max_length=255, null=True, verbose_name='title', blank=True)),
                ('meta_description', models.TextField(help_text='The text displayed in search engines.', max_length=155, null=True, verbose_name='description', blank=True)),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('path', models.CharField(max_length=255, verbose_name='Path', db_index=True)),
                ('has_url_overwrite', models.BooleanField(default=False, verbose_name='has url overwrite', db_index=True, editable=False)),
                ('redirect', models.CharField(max_length=2048, null=True, verbose_name='redirect', blank=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date', editable=False)),
                ('published', models.BooleanField(default=False, verbose_name='is published')),
                ('publisher_is_draft', models.BooleanField(default=True, db_index=True, editable=False)),
                ('publisher_state', models.SmallIntegerField(default=0, editable=False, db_index=True)),
                ('page', models.ForeignKey(related_name='title_set', verbose_name='page', to='cms.Page')),
                ('publisher_public', models.OneToOneField(related_name='publisher_draft', null=True, editable=False, to='cms.Title')),
            ],
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(help_text='The language for the admin interface and toolbar', max_length=10, verbose_name='Language', choices=[(b'fi', b'Suomi')])),
                ('clipboard', models.ForeignKey(blank=True, editable=False, to='cms.Placeholder', null=True)),
                ('user', models.OneToOneField(related_name='djangocms_usersettings', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user setting',
                'verbose_name_plural': 'user settings',
            },
        ),
        migrations.CreateModel(
            name='AliasPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('alias_placeholder', models.ForeignKey(related_name='alias_placeholder', editable=False, to='cms.Placeholder', null=True)),
            ],
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PlaceholderReference',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=255)),
                ('placeholder_ref', cms.models.fields.PlaceholderField(slotname=b'clipboard', editable=False, to='cms.Placeholder', null=True)),
            ],
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='pagepermission',
            name='group',
            field=models.ForeignKey(verbose_name='group', blank=True, to='auth.Group', null=True),
        ),
        migrations.AddField(
            model_name='pagepermission',
            name='page',
            field=models.ForeignKey(verbose_name='page', blank=True, to='cms.Page', null=True),
        ),
        migrations.AddField(
            model_name='pagepermission',
            name='user',
            field=models.ForeignKey(verbose_name='user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='placeholders',
            field=models.ManyToManyField(to='cms.Placeholder', editable=False),
        ),
        migrations.AddField(
            model_name='page',
            name='publisher_public',
            field=models.OneToOneField(related_name='publisher_draft', null=True, editable=False, to='cms.Page'),
        ),
        migrations.AddField(
            model_name='page',
            name='site',
            field=models.ForeignKey(related_name='djangocms_pages', verbose_name='site', to='sites.Site', help_text='The site the page is accessible at.'),
        ),
        migrations.AddField(
            model_name='globalpagepermission',
            name='group',
            field=models.ForeignKey(verbose_name='group', blank=True, to='auth.Group', null=True),
        ),
        migrations.AddField(
            model_name='globalpagepermission',
            name='sites',
            field=models.ManyToManyField(help_text='If none selected, user haves granted permissions to all sites.', to='sites.Site', verbose_name='sites', blank=True),
        ),
        migrations.AddField(
            model_name='globalpagepermission',
            name='user',
            field=models.ForeignKey(verbose_name='user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='cmsplugin',
            name='parent',
            field=models.ForeignKey(blank=True, editable=False, to='cms.CMSPlugin', null=True),
        ),
        migrations.AddField(
            model_name='cmsplugin',
            name='placeholder',
            field=models.ForeignKey(editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='title',
            unique_together=set([('language', 'page')]),
        ),
        migrations.AlterUniqueTogether(
            name='staticplaceholder',
            unique_together=set([('code', 'site')]),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('reverse_id', 'site', 'publisher_is_draft'), ('publisher_is_draft', 'site', 'application_namespace')]),
        ),
        migrations.AddField(
            model_name='aliaspluginmodel',
            name='plugin',
            field=models.ForeignKey(related_name='alias_reference', editable=False, to='cms.CMSPlugin', null=True),
        ),
    ]
