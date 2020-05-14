from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0015_auto_20200329_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
