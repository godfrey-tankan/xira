from django.shortcuts import render
import logging
from datetime import datetime
import json
import time
import random
from django.conf import settings
import requests as requests
from .accept_ticket import *


# curl -i -X POST `
#   https://graph.facebook.com/v20.0/339066582617708/messages `
#   -H 'Authorization: Bearer EAAMarOkeZCq4BOyJvORfv7dZAQFz3IQfft5pBnyPPwZCHCYN0jajF2ZCpIe6QAIGRACBqjOC77oUTscRQltXMmxlXiyaiPAoxNLqwWrBjV3MT79C4EtpSZBXwBs3vV6gB2vLiXIWTZBzH3Tt0zgit4PdaGTiOifq2ZB6MwMbgqeRwGHUMVnZACRKX8g2OMqdEq0mNIIsQWt6DBPCVYBShUCNayDZBXB7N9jEmMkcZD' `
#   -H 'Content-Type: application/json' `
#   -d '{ \"messaging_product\": \"whatsapp\", \"to\": \"263779586059\", \"type\": \"template\", \"template\": { \"name\": \"hello_world\", \"language\": { \"code\": \"en_US\" } } }'
# Create your views here.

def generate_response(response, wa_id, name):
    if response in ["hi", "hello", "hey","hie"]:
        return f"Hello {name}, how can I help you today?"
    if len(response) > 10:
        response =handle_inquiry(wa_id, response, name)
        return response
    if wa_id[0] == "263779586059":
        response=accept_ticket(wa_id,name, 1)
        return response
    return f"Hello {name}, you said: {response}"    


def get_text_message_input(recipient, text,media,template=False):
    if media:
        return json.dumps(
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": recipient,
                "type": "document",
                # "type": "document",
                "document": {
                    "link": media,
                    "filename": text
                },
            }
        )
    if template:
        return json.dumps(
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": recipient,
                "type": "template",
                "template": {
                    "name": "clava_welcome",
                    "language": {"code": "en-GB"},
                },
            }
        )
    return json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient,
            "type": "text",
            "text": {"preview_url": False, "body": text},
        }
    )
    
def send_message(data,template=False):
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {settings.ACCESS_TOKEN}",
    }
    url = f"https://graph.facebook.com/{settings.VERSION}/{settings.PHONE_NUMBER_ID}/messages"
    try:
        response = requests.post(
            url, data=data, headers=headers, timeout=30
        )  
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.Timeout:
        pass
        # logging.error("Timeout occurred while sending message")
        # return jsonify({"status": "error", "message": "Request timed out"}), 408
    except (    
        requests.RequestException
    ) as e:  # This will catch any general request exception
        pass
        # logging.error(f"Request failed due to: {e}")
        # return jsonify({"status": "error", "message": "Failed to send message"}), 500
    else:
        # Process the response as normal
        return response

def process_whatsapp_message(body):
    data = body
    try:
        # phone_number_id = data['entry'][0]['changes'][0]['value']['metadata']['phone_number_id']
        phone_number_id =  [contact['wa_id'] for contact in data['entry'][0]['changes'][0]['value']['contacts']]
    except Exception as e:
        phone_number_id = ""

    try:
        profile_name = data['entry'][0]['changes'][0]['value']['contacts'][0]['profile']['name']
    except Exception as e:
        profile_name = "User"
    try:
        message = body["entry"][0]["changes"][0]["value"]["messages"][0]
        message_body = message["text"]["body"]
    except Exception as e:
        message_body = "hello there, how can i help you today?"
    try:
        response = generate_response(message_body, phone_number_id, profile_name)
        data = get_text_message_input(phone_number_id, response,None,False)
        send_message(data)
    except Exception as e:
        ...

def send_message_template(recepient):
    return json.dumps(
    {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": f"{recepient}",
        "type": "template",
        "template": {
            "namespace": "7a757027_47cc_4bb8_997e_e1fdb0600675",
            "name": "clava_home2",
            "language": {
                "code": "en",
            }
        }
    }
)

def is_valid_whatsapp_message(body):
    """
    Check if the incoming webhook event has a valid WhatsApp message structure.
    """
    return (
        body.get("object")
        and body.get("entry")
        and body["entry"][0].get("changes")
        and body["entry"][0]["changes"][0].get("value")
        and body["entry"][0]["changes"][0]["value"].get("messages")
        and body["entry"][0]["changes"][0]["value"]["messages"][0]
    )