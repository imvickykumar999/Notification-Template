
def Send_notification_template_to_whatsapp_user(template_name, mob, name, username=None, text1=None, text2=None, text3=None):
        template = WhatsApp_Template.objects.get(name=template_name)
        json_string = json.dumps(template.data) 
        replacements = {
            "{{ sender_number }}": settings.WHATSAPP_SENDER_NO,
            "{{ recipient_number }}": mob,
            "{{ name }}": name,
            "{{ username }}": username,  
            "{{ text1 }}": text1,  
            "{{ text2 }}": text2,  
            "{{ text3 }}": text3,  
        }
        for placeholder, value in replacements.items():
            if value is not None and placeholder in json_string:
                json_string = json_string.replace(placeholder, value)
        
        print(json_string)
        updated_json_data = json.loads(json_string)
        payload = json.dumps(updated_json_data)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(template.url, headers=headers, data=payload)
        if response.status_code == 200:
            print(f"Message sent successfully to {mob}. Response: {response.text}")
        else:
            print(f"Failed to send message. Status Code: {response.status_code}, Response: {response.text}")


def send_email(key=None, user_email=None, user=None, title=None, items=None, download_link=None, product_key = None, invoice_link = None, product_name=None, festival_name=None, order_id=None, item_category=None, expire_hours=None):
    if user_email:
        amazon_backend = EmailBackend(
            host='email-smtp.us-east-1.amazonaws.com',
            port=587,
            username=settings.SENDER_MAIL_USERNAME,
            password=settings.SENDER_MAIL_PASSWORD,
            use_tls=True)
        
        email_template = EmailTemplate.objects.get(template_id=key)
        subject = email_template.subject.format(
            product_name=product_name, 
            festival_name = festival_name,
            order_id=order_id,
        )

        body = email_template.html_content.format(
            customer_name = user, 
            product_name = product_name,
            link = download_link,
            festival_name = festival_name,
            unsubscribe = 'https://www.imvickykumar999.com/unsubscribe',
            download_link = download_link,
            product_key = product_key,
            invoice_link = invoice_link,
            order_id=order_id,
            item_category=item_category, 
            expire_hours=expire_hours,
        )

        template = render_to_string('notification-basic.html', {'body': body})
        from_email = 'no-reply@imvickykumar999.com'

        email = EmailMultiAlternatives(subject, template, from_email, user_email, connection=amazon_backend)
        email.attach_alternative(template, "text/html")
        email.send()
