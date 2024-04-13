# Generated by Django 5.0.4 on 2024-04-13 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerQuartalFigure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slctn_nmbr', models.SmallIntegerField()),
                ('client_id', models.CharField(max_length=34)),
                ('npo_account_id', models.CharField(max_length=34)),
                ('npo_accnts_nmbr', models.SmallIntegerField()),
                ('pmnts_type', models.SmallIntegerField()),
                ('year', models.SmallIntegerField()),
                ('quarter', models.CharField(max_length=6)),
                ('gender', models.SmallIntegerField()),
                ('age', models.SmallIntegerField()),
                ('clnt_cprtn_time_d', models.IntegerField()),
                ('actv_prd_d', models.IntegerField()),
                ('lst_pmnt_rcnc_d', models.IntegerField()),
                ('balance', models.FloatField()),
                ('oprtn_sum_per_qrtr', models.FloatField()),
                ('oprtn_sum_per_year', models.FloatField()),
                ('frst_pmnt_date', models.CharField(blank=True, max_length=10, null=True)),
                ('lst_pmnt_date_per_qrtr', models.CharField(blank=True, max_length=10, null=True)),
                ('frst_pmnt', models.FloatField()),
                ('lst_pmnt', models.FloatField()),
                ('pmnts_sum', models.FloatField()),
                ('pmnts_nmbr', models.SmallIntegerField()),
                ('pmnts_sum_per_qrtr', models.FloatField()),
                ('pmnts_sum_per_year', models.FloatField()),
                ('pmnts_nmbr_per_qrtr', models.SmallIntegerField()),
                ('pmnts_nmbr_per_year', models.SmallIntegerField()),
                ('incm_sum', models.FloatField()),
                ('incm_per_qrtr', models.FloatField()),
                ('incm_per_year', models.FloatField()),
                ('mgd_accum_period', models.FloatField()),
                ('mgd_payment_period', models.FloatField()),
                ('phone_number', models.SmallIntegerField()),
                ('email', models.SmallIntegerField()),
                ('lk', models.SmallIntegerField()),
                ('assignee_npo', models.SmallIntegerField()),
                ('assignee_ops', models.SmallIntegerField()),
                ('postal_code', models.FloatField(blank=True, null=True)),
                ('region', models.CharField(blank=True, max_length=60, null=True)),
                ('citizen', models.SmallIntegerField()),
                ('fact_addrss', models.SmallIntegerField()),
                ('appl_mrkr', models.SmallIntegerField()),
                ('evry_qrtr_pmnt', models.SmallIntegerField()),
                ('churn', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
    ]
