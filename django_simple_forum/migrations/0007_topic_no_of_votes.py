from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0006_forumcategory_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='no_of_votes',
            field=models.IntegerField(default='0'),
        ),
    ]
