from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_simple_forum', '0011_facebook_github_google_twitter'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='mentioned',
            field=models.ManyToManyField(related_name='mentioned_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
