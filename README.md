# Notification-Template

Fetching Notification Template from Django Admin Database

```json
{
    "to": "{{ recipient_number }}",
    "data": {
        "name": "{{ name }}",
        "language": {
            "code": "en"
        },
        "components": [
            {
                "type": "body",
                "parameters": [
                    {
                        "text": "{{ text1 }}",
                        "type": "text"
                    },
                    {
                        "text": "{{ text2 }}",
                        "type": "text"
                    }
                ]
            }
        ]
    },
    "type": "marketing",
    "sender": "{{ sender_number }}"
}
```
