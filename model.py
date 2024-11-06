
class WhatsApp_Template(models.Model):
    url = models.CharField(max_length=100,default='https://chat.imvickykumar999.com/api/whatsapp/send')
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100,unique=True)
    data=models.JSONField()
    class Meta:
        db_table = 'WhatsApp_Template'


class Notifications(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,to_field='id',db_column='user_id')
    icon = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)  
    redirect_link = models.CharField(max_length=150,null=True, blank=True)
    read = models.BooleanField(default=False)
    type = models.CharField(max_length=50,blank=True, null=True)

    class Meta:
        db_table = 'Notifications'
    
    def __str__(self):
        return str(self.user_id.username)


class EmailTemplate(models.Model):
    template_id = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    html_content = models.TextField()

    def __str__(self):
        return str(self.template_id)
