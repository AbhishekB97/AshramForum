from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0003_topic_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='no_of_likes',
            field=models.IntegerField(default='0'),
        ),
    ]
