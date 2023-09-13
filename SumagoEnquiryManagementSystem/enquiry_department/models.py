from django.db import models
import datetime

# Create your models here.

class Course(models.Model):
    course_name=models.CharField(max_length=200)    
    course_fee=models.IntegerField()
    course_duration=models.CharField(max_length=20)
  
    def __str__(self):
        return f"{self.course_name}"
    
class Enquiry(models.Model):
    #Personal Info
    contact_person_choice = (('Dipti Pawar','Dipti Pawar'),('Ashwini Gite','Ashwini Gite'),('Vrushali Varpe','Vrushali Varpe'))
    contact_person = models.CharField(max_length=50,choices=contact_person_choice,default="Online Platform")
    seleted_course = models.ForeignKey(Course,on_delete=models.RESTRICT)
    full_name=models.CharField(max_length=250)
    gender_choice = (('Male','Male'),('Female','Female'),('Other','Other'))
    gender=models.CharField(max_length=10,choices=gender_choice)
    email_address=models.EmailField()
    contact_number=models.CharField(max_length=13) 
    permanent_address=models.TextField()
    date_of_birth=models.DateField()   
    whatsapp_number=models.CharField(max_length=13)
    alternate_number=models.CharField(max_length=13)
    enquiry_message=models.TextField(blank=True,null=True)

    #Technical Info
    how_did_you_hear_about_us_choice = (('Website','Website'),('Social Media','Social Media'),('Friends and Family','Friends and Family'),('Staff','Staff'),('Sulekha','Sulekha'))
    how_did_you_hear_about_us=models.CharField(max_length=20,choices=how_did_you_hear_about_us_choice)
    qualification=models.CharField(max_length=200)
    technical_skills=models.CharField(max_length=200)
    certifications_done=models.CharField(max_length=200)
    area_of_interest=models.CharField(max_length=200,null=True,blank=True)
    reference=models.CharField(max_length=100,null=True,blank=True)
    training_mode_choice = (('Online','Online'),('Offline','Offline'),('Hybrid','Hybrid'))
    training_mode=models.CharField(max_length=50,blank=True,null=True,choices=training_mode_choice)
    office_location_preference_choice = (('Pune','Pune'),('Nashik','Nashik'))
    office_location_preference=models.CharField(max_length=10,null=True,blank=True,choices=office_location_preference_choice)
    STATUS = (
        ('Finalized', 'Finalized'),
        ('Pending', 'Pending'),
        ('Informed On whatsapp','Informed on whatsapp')
        
    )
    enquiry_Status = models.TextField(max_length=20, choices=STATUS, default="Pending")
    
    def __str__(self):
        return f"Name:{self.full_name} , Selected Course:{self.seleted_course.course_name}"
    
class FollowUpReason(models.Model):
    reason=models.CharField(max_length=100)
    def __str__(self):
        return self.reason
    
class FollowUp(models.Model):
    enquiry=models.ForeignKey(Enquiry,on_delete=models.CASCADE)
    reason =models.ForeignKey(FollowUpReason,on_delete=models.RESTRICT)
    follow_up_date = models.DateField(blank=True,default=datetime.datetime.today)   
    follow_up_time = models.TimeField(blank=True,default=datetime.datetime.now())
    remark = models.CharField(max_length=200)
    status = (
        ('Follow Up Done', 'Follow Up Done'),
        ('Pending', 'Pending'),
        )
    followup_status = models.CharField(max_length=50,choices=status,default="Pending")
    enroll_flag=models.BooleanField(default=False)

    def __str__(self):
        return f"Name:{self.enquiry.full_name} | Course:{self.enquiry.seleted_course} | Status:{self.followup_status}"
    

class PaymentDiscusion(models.Model):
    enquiry=models.ForeignKey(Enquiry,on_delete=models.CASCADE)
    total_no_of_installments=models.IntegerField()
    payment_mode_choice = (('Debit Card','Debit Card'),('Credit Card','Credit Card'),('UPI','UPI'),('Cash','Cash'),('QR Code','QR Code'))
    payment_mode=models.CharField(max_length=50,choices=payment_mode_choice,default='Cash')
    first_installment=models.FloatField(default=0)
    first_installment_date=models.DateField(default=datetime.datetime.today() + datetime.timedelta(days=1))
    second_installment=models.FloatField(blank=True,null=True)
    second_installment_date=models.DateField(blank=True,null=True)
    third_installment=models.FloatField(blank=True,null=True)
    third_installment_date=models.DateField(blank=True,null=True)
    four_installment=models.FloatField(blank=True,null=True)
    four_installment_date=models.DateField(blank=True,null=True)
    STATUS=(
        ('Pending','Pending'),
        ('First Installment Done','First Installment Done'),
        ('Second Installment Done','Second Installment Done'),
        ('Third Installment Done','Third Installment Done'),
        ('Fouth Installment Done','Fouth Installment Done'),
        ('All Installments Completed','All Installments Completed')
    )
    payment_status= models.CharField(max_length=100, choices=STATUS, default="Pending")
    discount_amount=models.FloatField(blank=True,null=True)
    final_amount = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        course_fee = self.enquiry.seleted_course.course_fee
        if self.discount_amount is not None:
            self.final_amount = course_fee - self.discount_amount
        else:
            self.final_amount = course_fee
        super(PaymentDiscusion, self).save(*args, **kwargs)
    # account_remark=models.CharField(max_length=100,null=True,blank=True)
    # amount=models.IntegerField(blank=True,null=True,default=0)
    # amount_date=models.DateField(default=datetime.date.today)
    # amount_remaining = models.PositiveIntegerField(blank=True,null=True)
    # total_amount=models.FloatField(blank=True,null=True)
    

    def __str__(self):
        return f"Name:{self.enquiry.full_name} Installments:{self.total_no_of_installments} "




