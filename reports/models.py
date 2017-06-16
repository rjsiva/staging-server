from django.db import models 
from django.db.models.fields import *
from baseapp.models import School,Block,District,Class_Studying
from students.models import Child_detail,School_child_count
import caching.base
from django.db.models.signals import post_save, post_delete

# Create your models here.
class aadhaar_student_count(models.Model):
    school=models.ForeignKey(School,blank=True, null=True)                        
    c1 = models.PositiveIntegerField(blank=True, null=True)
    c2 = models.PositiveIntegerField(blank=True, null=True)
    c3 = models.PositiveIntegerField(blank=True, null=True)
    c4 = models.PositiveIntegerField(blank=True, null=True)
    c5 = models.PositiveIntegerField(blank=True, null=True)
    c6 = models.PositiveIntegerField(blank=True, null=True)
    c7 = models.PositiveIntegerField(blank=True, null=True)
    c8 = models.PositiveIntegerField(blank=True, null=True)
    c9 = models.PositiveIntegerField(blank=True, null=True)
    c10 = models.PositiveIntegerField(blank=True, null=True)
    c11 = models.PositiveIntegerField(blank=True, null=True)
    c12 = models.PositiveIntegerField(blank=True, null=True)
    school_total = models.PositiveIntegerField(blank=True, null=True)
    a_c1 = models.PositiveIntegerField(blank=True, null=True)
    a_c2 = models.PositiveIntegerField(blank=True, null=True)
    a_c3 = models.PositiveIntegerField(blank=True, null=True)
    a_c4 = models.PositiveIntegerField(blank=True, null=True)
    a_c5 = models.PositiveIntegerField(blank=True, null=True)
    a_c6 = models.PositiveIntegerField(blank=True, null=True)
    a_c7 = models.PositiveIntegerField(blank=True, null=True)
    a_c8 = models.PositiveIntegerField(blank=True, null=True)
    a_c9 = models.PositiveIntegerField(blank=True, null=True)
    a_c10 = models.PositiveIntegerField(blank=True, null=True)
    a_c11 = models.PositiveIntegerField(blank=True, null=True)
    a_c12 = models.PositiveIntegerField(blank=True, null=True)
    a_school_total = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.school)

class common_reports(models.Model):
    school=models.ForeignKey(School,blank=True, null=True)
    c1 = models.PositiveIntegerField(blank=True, null=True)
    c2 = models.PositiveIntegerField(blank=True, null=True)
    c3 = models.PositiveIntegerField(blank=True, null=True)
    c4 = models.PositiveIntegerField(blank=True, null=True)
    c5 = models.PositiveIntegerField(blank=True, null=True)
    c6 = models.PositiveIntegerField(blank=True, null=True)
    c7 = models.PositiveIntegerField(blank=True, null=True)
    c8 = models.PositiveIntegerField(blank=True, null=True)
    c9 = models.PositiveIntegerField(blank=True, null=True)
    c10 = models.PositiveIntegerField(blank=True, null=True)
    c11 = models.PositiveIntegerField(blank=True, null=True)
    c12 = models.PositiveIntegerField(blank=True, null=True)
    c_total = models.PositiveIntegerField(blank=True, null=True)
    c1_b = models.PositiveIntegerField(blank=True, null=True)
    c2_b = models.PositiveIntegerField(blank=True, null=True)
    c3_b = models.PositiveIntegerField(blank=True, null=True)
    c4_b = models.PositiveIntegerField(blank=True, null=True)
    c5_b = models.PositiveIntegerField(blank=True, null=True)
    c6_b = models.PositiveIntegerField(blank=True, null=True)
    c7_b = models.PositiveIntegerField(blank=True, null=True)
    c8_b = models.PositiveIntegerField(blank=True, null=True)
    c9_b = models.PositiveIntegerField(blank=True, null=True)
    c10_b = models.PositiveIntegerField(blank=True, null=True)
    c11_b = models.PositiveIntegerField(blank=True, null=True)
    c12_b = models.PositiveIntegerField(blank=True, null=True)
    c_total_b = models.PositiveIntegerField(blank=True, null=True)
    c1_g = models.PositiveIntegerField(blank=True, null=True)
    c2_g = models.PositiveIntegerField(blank=True, null=True)
    c3_g = models.PositiveIntegerField(blank=True, null=True)
    c4_g = models.PositiveIntegerField(blank=True, null=True)
    c5_g = models.PositiveIntegerField(blank=True, null=True)
    c6_g = models.PositiveIntegerField(blank=True, null=True)
    c7_g = models.PositiveIntegerField(blank=True, null=True)
    c8_g = models.PositiveIntegerField(blank=True, null=True)
    c9_g = models.PositiveIntegerField(blank=True, null=True)
    c10_g = models.PositiveIntegerField(blank=True, null=True)
    c11_g = models.PositiveIntegerField(blank=True, null=True)
    c12_g = models.PositiveIntegerField(blank=True, null=True)
    c_total_g = models.PositiveIntegerField(blank=True, null=True)
    c1_t = models.PositiveIntegerField(blank=True, null=True)
    c2_t = models.PositiveIntegerField(blank=True, null=True)
    c3_t = models.PositiveIntegerField(blank=True, null=True)
    c4_t = models.PositiveIntegerField(blank=True, null=True)
    c5_t = models.PositiveIntegerField(blank=True, null=True)
    c6_t = models.PositiveIntegerField(blank=True, null=True)
    c7_t = models.PositiveIntegerField(blank=True, null=True)
    c8_t = models.PositiveIntegerField(blank=True, null=True)
    c9_t = models.PositiveIntegerField(blank=True, null=True)
    c10_t = models.PositiveIntegerField(blank=True, null=True)
    c11_t = models.PositiveIntegerField(blank=True, null=True)
    c12_t = models.PositiveIntegerField(blank=True, null=True)
    c_total_t = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
            return u'%s' % (self.school.school_code)

def report_child_count_increase(sender, instance, **kwargs):
    if kwargs.get('created', True):
        try:
            child = common_reports.objects.get(school_id=instance.school_id)
        except common_reports.DoesNotExist:
            child=common_reports.objects.create(school=instance.school,c1=0,c2=0,c3=0,c4=0,c5=0,c6=0,c7=0,c8=0,c9=0,c10=0,c11=0,c12=0,c_total=0)
        class_studying= instance.class_studying
        gender=instance.gender

        if str(class_studying)=='I':
            child.c1 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c1_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c1_g+=1
                child.c_total_g+=1
            else:
                child.c1_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='II':
            child.c2 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c2_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c2_g+=1
                child.c_total_g+=1
            else:
                child.c2_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='III':
            child.c3 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c3_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c3_g+=1
                child.c_total_g+=1
            else:
                child.c3_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='IV':
            child.c4 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c4_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c4_g+=1
                child.c_total_g+=1
            else:
                child.c4_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='V':
            child.c5 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c5_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c5_g+=1
                child.c_total_g+=1
            else:
                child.c5_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='VI':
            child.c6 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c6_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c6_g+=1
                child.c_total_g+=1
            else:
                child.c6_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='VII':
            child.c7 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c7_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c7_g+=1
                child.c_total_g+=1
            else:
                child.c7_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='VIII':
            child.c8 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c8_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c8_g+=1
                child.c_total_g+=1
            else:
                child.c8_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='IX':
            child.c9+= 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c9_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c9_g+=1
                child.c_total_g+=1
            else:
                child.c9_t+=1
                child.c_total_t+=1
        elif str(class_studying)=='X':
            child.c10 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c10_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c10_g+=1
                child.c_total_g+=1
            else:
                child.c10_t+=1
                child.c_total_t+=1
        elif str(class_studying)=='XI':
            child.c11 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c11_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c11_g+=1
                child.c_total_g+=1
            else:
                child.c11_t+=1
                child.c_total_t+=1
        elif str(class_studying)=='XII':
            child.c12 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c12_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c12_g+=1
                child.c_total_g+=1
            else:
                child.c12_t+=1
                child.c_total_t+=1
        
        child.save()
post_save.connect(report_child_count_increase, sender=Child_detail)

def report_child_count_decrease(sender, instance, **kwargs):
    
    child = common_reports.objects.get(school_id=instance.school_id)
    class_studying= instance.class_studying
    gender=instance.gender
    if str(class_studying)=='I':
        child.c1 -= 1
        child.c_total-=1
        if str(gender)=='Male':
            child.c1_b-=1
            child.c_total_b-=1
        elif str(gender)=='Female':
            child.c1_g-=1
            child.c_total_g-=1
        else:
            child.c1_t-=1
            child.c_total_t-=1
            
    elif str(class_studying)=='II':
        child.c2 -= 1
        child.c_total-=1
        if str(gender)=='Male':
            child.c2_b-=1
            child.c_total_b-=1
        elif str(gender)=='Female':
            child.c2_g-=1
            child.c_total_g-=1
        else:
            child.c2_t-=1
            child.c_total_t-=1
        
    elif str(class_studying)=='III':
        child.c3 -= 1
        child.c_total-=1
        if str(gender)=='Male':
            child.c3_b-=1
            child.c_total_b-=1
        elif str(gender)=='Female':
            child.c3_g-=1
            child.c_total_g-=1
        else:
            child.c3_t-=1
            child.c_total_t-=1
        
    elif str(class_studying)=='IV':
        child.c4 -= 1
        child.c_total-=1
        if str(gender)=='Male':
            child.c4_b-=1
            child.c_total_b-=1
        elif str(gender)=='Female':
            child.c4_g-=1
            child.c_total_g-=1
        else:
            child.c4_t-=1
            child.c_total_t-=1
        
    elif str(class_studying)=='V':
        child.c5 -= 1
        child.c_total-=1
        if str(gender)=='Male':
            child.c5_b-=1
            child.c_total_b-=1
        elif str(gender)=='Female':
            child.c5_g-=1
            child.c_total_g-=1
        else:
            child.c5_t-=1
            child.c_total_t-=1
        
    elif str(class_studying)=='VI':
        child.c6 -= 1
        child.c_total-=1
        if str(gender)=='Male':
            child.c6_b-=1
            child.c_total_b-=1
        elif str(gender)=='Female':
            child.c6_g-=1
            child.c_total_g-=1
        else:
            child.c6_t-=1
            child.c_total_t-=1
        
    elif str(class_studying)=='VII':
        child.c7 -= 1
        child.c_total-=1
        if str(gender)=='Male':
            child.c7_b-=1
            child.c_total_b-=1
        elif str(gender)=='Female':
            child.c7_g-=1
            child.c_total_g-=1
        else:
            child.c7_t-=1
            child.c_total_t-=1
        
    elif str(class_studying)=='VIII':
        child.c8 -= 1
        child.c_total-=1
        if str(gender)=='Male':
            child.c8_b-=1
            child.c_total_b-=1
        elif str(gender)=='Female':
            child.c8_g-=1
            child.c_total_g-=1
        else:
            child.c8_t-=1
            child.c_total_t-=1
        
    elif str(class_studying)=='IX':
        child.c9-= 1
        child.c_total-=1
        if str(gender)=='Male':
            child.c9_b-=1
            child.c_total_b-=1
        elif str(gender)=='Female':
            child.c9_g-=1
            child.c_total_g-=1
        else:
            child.c9_t-=1
            child.c_total_t-=1
    elif str(class_studying)=='X':
        child.c10 -= 1
        child.c_total-=1
        if str(gender)=='Male':
            child.c10_b-=1
            child.c_total_b-=1
        elif str(gender)=='Female':
            child.c10_g-=1
            child.c_total_g-=1
        else:
            child.c10_t-=1
            child.c_total_t-=1
    elif str(class_studying)=='XI':
        child.c11 -= 1
        child.c_total-=1
        if str(gender)=='Male':
            child.c11_b-=1
            child.c_total_b-=1
        elif str(gender)=='Female':
            child.c11_g-=1
            child.c_total_g-=1
        else:
            child.c11_t-=1
            child.c_total_t-=1
    elif str(class_studying)=='XII':
        child.c12 -= 1
        child.c_total-=1
        if str(gender)=='Male':
            child.c12_b-=1
            child.c_total_b-=1
        elif str(gender)=='Female':
            child.c12_g-=1
            child.c_total_g-=1
        else:
            child.c12_t-=1
            child.c_total_t-=1
    child.save()
post_delete.connect(report_child_count_decrease, sender=Child_detail)
    

class medium_of_instrction(models.Model):
    school=models.ForeignKey(School,blank=True, null=True) 
    common_rep=models.ForeignKey(common_reports,blank=True,null=True)                       
    c1_tamil = models.PositiveIntegerField(blank=True, null=True)
    c2_tamil = models.PositiveIntegerField(blank=True, null=True)
    c3_tamil = models.PositiveIntegerField(blank=True, null=True)
    c4_tamil = models.PositiveIntegerField(blank=True, null=True)
    c5_tamil = models.PositiveIntegerField(blank=True, null=True)
    c6_tamil = models.PositiveIntegerField(blank=True, null=True)
    c7_tamil = models.PositiveIntegerField(blank=True, null=True)
    c8_tamil = models.PositiveIntegerField(blank=True, null=True)
    c9_tamil = models.PositiveIntegerField(blank=True, null=True)
    c10_tamil = models.PositiveIntegerField(blank=True, null=True)
    c11_tamil = models.PositiveIntegerField(blank=True, null=True)
    c12_tamil = models.PositiveIntegerField(blank=True, null=True)
    total_tamil = models.PositiveIntegerField(blank=True, null=True)
    c1_eng = models.PositiveIntegerField(blank=True, null=True)
    c2_eng = models.PositiveIntegerField(blank=True, null=True)
    c3_eng = models.PositiveIntegerField(blank=True, null=True)
    c4_eng = models.PositiveIntegerField(blank=True, null=True)
    c5_eng = models.PositiveIntegerField(blank=True, null=True)
    c6_eng = models.PositiveIntegerField(blank=True, null=True)
    c7_eng = models.PositiveIntegerField(blank=True, null=True)
    c8_eng = models.PositiveIntegerField(blank=True, null=True)
    c9_eng = models.PositiveIntegerField(blank=True, null=True)
    c10_eng = models.PositiveIntegerField(blank=True, null=True)
    c11_eng = models.PositiveIntegerField(blank=True, null=True)
    c12_eng = models.PositiveIntegerField(blank=True, null=True)
    total_eng = models.PositiveIntegerField(blank=True, null=True)
    c1_telugu = models.PositiveIntegerField(blank=True, null=True)
    c2_telugu = models.PositiveIntegerField(blank=True, null=True)
    c3_telugu = models.PositiveIntegerField(blank=True, null=True)
    c4_telugu = models.PositiveIntegerField(blank=True, null=True)
    c5_telugu = models.PositiveIntegerField(blank=True, null=True)
    c6_telugu = models.PositiveIntegerField(blank=True, null=True)
    c7_telugu = models.PositiveIntegerField(blank=True, null=True)
    c8_telugu = models.PositiveIntegerField(blank=True, null=True)
    c9_telugu = models.PositiveIntegerField(blank=True, null=True)
    c10_telugu = models.PositiveIntegerField(blank=True, null=True)
    c11_telugu = models.PositiveIntegerField(blank=True, null=True)
    c12_telugu = models.PositiveIntegerField(blank=True, null=True)
    total_telugu = models.PositiveIntegerField(blank=True, null=True)
    c1_mlym = models.PositiveIntegerField(blank=True, null=True)
    c2_mlym = models.PositiveIntegerField(blank=True, null=True)
    c3_mlym = models.PositiveIntegerField(blank=True, null=True)
    c4_mlym = models.PositiveIntegerField(blank=True, null=True)
    c5_mlym = models.PositiveIntegerField(blank=True, null=True)
    c6_mlym = models.PositiveIntegerField(blank=True, null=True)
    c7_mlym = models.PositiveIntegerField(blank=True, null=True)
    c8_mlym = models.PositiveIntegerField(blank=True, null=True)
    c9_mlym = models.PositiveIntegerField(blank=True, null=True)
    c10_mlym = models.PositiveIntegerField(blank=True, null=True)
    c11_mlym = models.PositiveIntegerField(blank=True, null=True)
    c12_mlym = models.PositiveIntegerField(blank=True, null=True)
    total_mlym = models.PositiveIntegerField(blank=True, null=True)
    c1_kanada = models.PositiveIntegerField(blank=True, null=True)
    c2_kanada = models.PositiveIntegerField(blank=True, null=True)
    c3_kanada = models.PositiveIntegerField(blank=True, null=True)
    c4_kanada = models.PositiveIntegerField(blank=True, null=True)
    c5_kanada = models.PositiveIntegerField(blank=True, null=True)
    c6_kanada = models.PositiveIntegerField(blank=True, null=True)
    c7_kanada = models.PositiveIntegerField(blank=True, null=True)
    c8_kanada = models.PositiveIntegerField(blank=True, null=True)
    c9_kanada = models.PositiveIntegerField(blank=True, null=True)
    c10_kanada = models.PositiveIntegerField(blank=True, null=True)
    c11_kanada = models.PositiveIntegerField(blank=True, null=True)
    c12_kanada = models.PositiveIntegerField(blank=True, null=True)
    total_kanada = models.PositiveIntegerField(blank=True, null=True)
    c1_urdu = models.PositiveIntegerField(blank=True, null=True)
    c2_urdu = models.PositiveIntegerField(blank=True, null=True)
    c3_urdu = models.PositiveIntegerField(blank=True, null=True)
    c4_urdu = models.PositiveIntegerField(blank=True, null=True)
    c5_urdu = models.PositiveIntegerField(blank=True, null=True)
    c6_urdu = models.PositiveIntegerField(blank=True, null=True)
    c7_urdu = models.PositiveIntegerField(blank=True, null=True)
    c8_urdu = models.PositiveIntegerField(blank=True, null=True)
    c9_urdu = models.PositiveIntegerField(blank=True, null=True)
    c10_urdu = models.PositiveIntegerField(blank=True, null=True)
    c11_urdu = models.PositiveIntegerField(blank=True, null=True)
    c12_urdu = models.PositiveIntegerField(blank=True, null=True)
    total_urdu = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
            return u'%s' % (self.school.school_code)

def medium_count_increase(sender, instance, **kwargs):
    if kwargs.get('created', True):
        try:
            child = medium_of_instrction.objects.get(school_id=instance.school_id)
        except medium_of_instrction.DoesNotExist:
            child=medium_of_instrction.objects.create(school=instance.school,c1=0,c2=0,c3=0,c4=0,c5=0,c6=0,c7=0,c8=0,c9=0,c10=0,c11=0,c12=0,c_total=0)
        class_studying= instance.class_studying
        medium=instance.education_medium_id
        if str(class_studying)=='I':
            if int(medium)==1:
                child.c1_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c1_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c1_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c1_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c1_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c1_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='II':
            if int(medium)==1:
                child.c2_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c2_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c2_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c2_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c2_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c2_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='III':
            if int(medium)==1:
                child.c3_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c3_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c3_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c3_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c3_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c4_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='IV':
            if int(medium)==1:
                child.c4_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c4_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c4_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c4_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c4_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c4_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='V`':
            if int(medium)==1:
                child.c5_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c5_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c5_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c5_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c5_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c5_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='VI':
            if int(medium)==1:
                child.c6_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c6_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c6_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c6_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c6_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c6_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='VII':
            if int(medium)==1:
                child.c7_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c7_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c7_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c7_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c7_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c7_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='VIII':
            if int(medium)==1:
                child.c8_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c8_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c8_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c8_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c8_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c8_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='IX':
            if int(medium)==1:
                child.c9_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c9_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c9_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c9_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c9_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c9_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='X':
            if int(medium)==1:
                child.c10_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c10_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c10_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c10_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c10_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c10_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='XI':
            if int(medium)==1:
                child.c11_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c11_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c11_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c11_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c11_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c11_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='XII':
            if int(medium)==1:
                child.c12_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c12_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c12_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c12_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c12_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c12_urdu+=1
                child.total_urdu+=1
            child.save()
post_save.connect(medium_count_increase, sender=Child_detail)

def medium_count_decrease(sender, instance, **kwargs):    
    child = medium_of_instrction.objects.get(school_id=instance.school_id)
    class_studying= instance.class_studying
    medium=instance.education_medium_id
    if str(class_studying)=='I':
        if int(medium)==1:
            child.c1_tamil-=1
            child.total_tamil-=1
        elif int(medium)==2:
            child.c1_eng-=1
            child.total_eng-=1
        elif int(medium)==4:
            child.c1_telugu-=1
            child.total_telugu-=1
        elif int(medium)==5:
            child.c1_mlym-=1
            child.total_mlym-=1
        elif int(medium)==6:
            child.c1_kanada-=1
            child.total_kanada-=1
        elif int(medium)==7:
            child.c1_urdu-=1
            child.total_urdu-=1
    elif str(class_studying)=='II':
        if int(medium)==1:
            child.c2_tamil-=1
            child.total_tamil-=1
        elif int(medium)==2:
            child.c2_eng-=1
            child.total_eng-=1
        elif int(medium)==4:
            child.c2_telugu-=1
            child.total_telugu-=1
        elif int(medium)==5:
            child.c2_mlym-=1
            child.total_mlym-=1
        elif int(medium)==6:
            child.c2_kanada-=1
            child.total_kanada-=1
        elif int(medium)==7:
            child.c2_urdu-=1
            child.total_urdu-=1 
    elif str(class_studying)=='III':
        if int(medium)==1:
            child.c3_tamil-=1
            child.total_tamil-=1
        elif int(medium)==2:
            child.c3_eng-=1
            child.total_eng-=1
        elif int(medium)==4:
            child.c3_telugu-=1
            child.total_telugu-=1
        elif int(medium)==5:
            child.c3_mlym-=1
            child.total_mlym-=1
        elif int(medium)==6:
            child.c3_kanada-=1
            child.total_kanada-=1
        elif int(medium)==7:
            child.c3_urdu-=1
            child.total_urdu-=1
    elif str(class_studying)=='IV':
        if int(medium)==1:
            child.c4_tamil-=1
            child.total_tamil-=1
        elif int(medium)==2:
            child.c4_eng-=1
            child.total_eng-=1
        elif int(medium)==4:
            child.c4_telugu-=1
            child.total_telugu-=1
        elif int(medium)==5:
            child.c4_mlym-=1
            child.total_mlym-=1
        elif int(medium)==6:
            child.c4_kanada-=1
            child.total_kanada-=1
        elif int(medium)==7:
            child.c4_urdu-=1
            child.total_urdu-=1
    elif str(class_studying)=='V':
        if int(medium)==1:
            child.c5_tamil-=1
            child.total_tamil-=1
        elif int(medium)==2:
            child.c5_eng-=1
            child.total_eng-=1
        elif int(medium)==4:
            child.c5_telugu-=1
            child.total_telugu-=1
        elif int(medium)==5:
            child.c5_mlym-=1
            child.total_mlym-=1
        elif int(medium)==6:
            child.c5_kanada-=1
            child.total_kanada-=1
        elif int(medium)==7:
            child.c5_urdu-=1
            child.total_urdu-=1
    elif str(class_studying)=='VI':
        if int(medium)==1:
            child.c6_tamil-=1
            child.total_tamil-=1
        elif int(medium)==2:
            child.c6_eng-=1
            child.total_eng-=1
        elif int(medium)==4:
            child.c6_telugu-=1
            child.total_telugu-=1
        elif int(medium)==5:
            child.c6_mlym-=1
            child.total_mlym-=1
        elif int(medium)==6:
            child.c6_kanada-=1
            child.total_kanada-=1
        elif int(medium)==7:
            child.c6_urdu-=1
            child.total_urdu-=1
    elif str(class_studying)=='VII':
        if int(medium)==1:
            child.c7_tamil-=1
            child.total_tamil-=1
        elif int(medium)==2:
            child.c7_eng-=1
            child.total_eng-=1
        elif int(medium)==4:
            child.c7_telugu-=1
            child.total_telugu-=1
        elif int(medium)==5:
            child.c7_mlym-=1
            child.total_mlym-=1
        elif int(medium)==6:
            child.c7_kanada-=1
            child.total_kanada-=1
        elif int(medium)==7:
            child.c7_urdu-=1
            child.total_urdu-=1
    elif str(class_studying)=='VIII':
        if int(medium)==1:
            child.c8_tamil-=1
            child.total_tamil-=1
        elif int(medium)==2:
            child.c8_eng-=1
            child.total_eng-=1
        elif int(medium)==4:
            child.c8_telugu-=1
            child.total_telugu-=1
        elif int(medium)==5:
            child.c8_mlym-=1
            child.total_mlym-=1
        elif int(medium)==6:
            child.c8_kanada-=1
            child.total_kanada-=1
        elif int(medium)==7:
            child.c8_urdu-=1
            child.total_urdu-=1
    elif str(class_studying)=='IX':
        if int(medium)==1:
            child.c9_tamil-=1
            child.total_tamil-=1
        elif int(medium)==2:
            child.c9_eng-=1
            child.total_eng-=1
        elif int(medium)==4:
            child.c9_telugu-=1
            child.total_telugu-=1
        elif int(medium)==5:
            child.c9_mlym-=1
            child.total_mlym-=1
        elif int(medium)==6:
            child.c9_kanada-=1
            child.total_kanada-=1
        elif int(medium)==7:
            child.c9_urdu-=1
            child.total_urdu-=1        
    elif str(class_studying)=='X':
        if int(medium)==1:
            child.c10_tamil-=1
            child.total_tamil-=1
        elif int(medium)==2:
            child.c10_eng-=1
            child.total_eng-=1
        elif int(medium)==4:
            child.c10_telugu-=1
            child.total_telugu-=1
        elif int(medium)==5:
            child.c10_mlym-=1
            child.total_mlym-=1
        elif int(medium)==6:
            child.c10_kanada-=1
            child.total_kanada-=1
        elif int(medium)==7:
            child.c10_urdu-=1
            child.total_urdu-=1
    elif str(class_studying)=='XI':
        if int(medium)==1:
            child.c11_tamil-=1
            child.total_tamil-=1
        elif int(medium)==2:
            child.c11_eng-=1
            child.total_eng-=1
        elif int(medium)==4:
            child.c11_telugu-=1
            child.total_telugu-=1
        elif int(medium)==5:
            child.c11_mlym-=1
            child.total_mlym-=1
        elif int(medium)==6:
            child.c11_kanada-=1
            child.total_kanada-=1
        elif int(medium)==7:
            child.c11_urdu-=1
            child.total_urdu-=1
    elif str(class_studying)=='XII':
        if int(medium)==1:
            child.c12_tamil-=1
            child.total_tamil-=1
        elif int(medium)==2:
            child.c12_eng-=1
            child.total_eng-=1
        elif int(medium)==4:
            child.c12_telugu-=1
            child.total_telugu-=1
        elif int(medium)==5:
            child.c12_mlym-=1
            child.total_mlym-=1
        elif int(medium)==6:
            child.c12_kanada-=1
            child.total_kanada-=1
        elif int(medium)==7:
            child.c12_urdu-=1
            child.total_urdu-=1        
    child.save()
post_delete.connect(medium_count_decrease, sender=Child_detail)
  
       

