# Generated by Django 4.1.5 on 2023-08-18 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pump', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tank', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VinanPetLtd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_Date', models.DateTimeField(auto_now_add=True, null=True)),
                ('entry_Date', models.DateTimeField(null=True)),
                ('tank_Opening', models.DecimalField(decimal_places=3, max_digits=13, null=True)),
                ('tank_Closing', models.DecimalField(decimal_places=3, max_digits=13, null=True)),
                ('tank_Difference', models.DecimalField(decimal_places=3, max_digits=13, null=True)),
                ('pump_Opening', models.FloatField(null=True)),
                ('pump_Closing', models.FloatField(null=True)),
                ('pump_Difference', models.DecimalField(decimal_places=3, max_digits=13, null=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=13, null=True)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=13, null=True)),
                ('pos', models.DecimalField(decimal_places=3, max_digits=13, null=True)),
                ('cash', models.DecimalField(decimal_places=3, max_digits=13, null=True)),
                ('expenses', models.DecimalField(decimal_places=3, max_digits=13, null=True)),
                ('balance', models.DecimalField(decimal_places=3, max_digits=13, null=True)),
                ('amount_Deposited', models.DecimalField(decimal_places=3, max_digits=13, null=True)),
                ('teller_ID', models.IntegerField(null=True)),
                ('teller', models.ImageField(null=True, upload_to='teller')),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vinanpet.branch')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vinanpet.product')),
                ('pump', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vinanpet.pump')),
                ('tank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vinanpet.tank')),
            ],
        ),
    ]
