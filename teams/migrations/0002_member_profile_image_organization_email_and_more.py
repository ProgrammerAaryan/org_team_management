# Generated by Django 5.1.4 on 2024-12-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="profile_images/"),
        ),
        migrations.AddField(
            model_name="organization",
            name="email",
            field=models.EmailField(default="example@example.com", max_length=254),
        ),
        migrations.AddField(
            model_name="organization",
            name="location",
            field=models.CharField(default="Unknown Location", max_length=255),
        ),
    ]