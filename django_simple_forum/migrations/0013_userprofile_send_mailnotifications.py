from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0012_comment_mentioned'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='send_mailnotifications',
            field=models.BooleanField(default=False),
        ),
    ]
