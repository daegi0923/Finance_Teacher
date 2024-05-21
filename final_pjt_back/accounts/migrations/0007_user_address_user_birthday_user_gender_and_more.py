# Generated by Django 4.2.13 on 2024-05-20 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_subscribeddeposit_deposit_option_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(choices=[('서울특별시', '서울특별시'), ('인천광역시', '인천광역시'), ('대전광역시', '대전광역시'), ('대구광역시', '대구광역시'), ('광주광역시', '광주광역시'), ('부산광역시', '부산광역시'), ('울산광역시', '울산광역시'), ('세종특별자치시', '세종특별자치시'), ('경기도', '경기도'), ('강원도', '강원도'), ('충청북도', '충청북도'), ('충청남도', '충청남도'), ('경상북도', '경상북도'), ('경상남도', '경상남도'), ('전라북도', '전라북도'), ('전라남도', '전라남도'), ('제주특별자치도', '제주특별자치도')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('남성', '남성'), ('여성', '여성'), ('미선택', '미선택')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='primary_bank',
            field=models.CharField(choices=[('우리은행', '우리은행'), ('한국스탠다드차타드은행', '한국스탠다드차타드은행'), ('대구은행', '대구은행'), ('부산은행', '부산은행'), ('광주은행', '광주은행'), ('제주은행', '제주은행'), ('전북은행', '전북은행'), ('경남은행', '경남은행'), ('중소기업은행', '중소기업은행'), ('한국산업은행', '한국산업은행'), ('국민은행', '국민은행'), ('신한은행', '신한은행'), ('농협은행', '농협은행'), ('KEB하나은행', 'KEB하나은행'), ('수협은행', '수협은행'), ('주식회사 카카오뱅크', '주식회사 카카오뱅크'), ('주식회사 케이뱅크', '주식회사 케이뱅크'), ('토스뱅크 주식회사', '토스뱅크 주식회사'), ('기타', '기타')], max_length=20, null=True),
        ),
    ]
