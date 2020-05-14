from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0007_topic_no_of_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='no_of_down_votes',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='usertopics',
            name='no_of_down_votes',
            field=models.IntegerField(default='0'),
        ),
    ]
