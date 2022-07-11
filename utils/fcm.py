import firebase_admin
from firebase_admin import credentials, messaging
from django.conf import settings


class FCMManager:
  
    def __init__(self):
        cred = credentials.Certificate(settings.FCM_CREDENTIALS)
        if len(firebase_admin._apps) == 0:
            firebase_admin.initialize_app(cred, name="admin")

    @classmethod
    def send_push(cls, title, msg, registration_token, dataObject=None):
        message = messaging.MulticastMessage(
            notification=messaging.Notification(title=title,
                                                body=msg,
                                                ),
            data=dataObject,
            tokens=[registration_token]
        )

        response = messaging.send(message)
        print('successfully sent message', response)

    @classmethod
    def send_push_to_all(cls, title, msg, dataObject=None):
        message = messaging.Message(
            notification=messaging.Notification(title=title,
                                                body=msg,
                                                ),
            data=dataObject
        )

        response = messaging.send(message)
        print('successfully sent message', response)

    @classmethod
    def send_push_to_topic(cls, title, msg, topic):
        message = messaging.Message(
            notification=messaging.Notification(title=title,
                                                body=msg,
                                                ),
            topic=topic
        )

        response = messaging.send(message)
        print('successfully sent message', response)

    @classmethod
    def send_push_to_condition(cls, title, msg, condition):
        message = messaging.Message(
            notification=messaging.Notification(title=title,
                                                body=msg,
                                                ),
            condition=condition
        )

        response = messaging.send(message)
        print('successfully sent message', response)

    @classmethod
    def send_push_to_token(cls, title, msg, registration_token):
        message = messaging.Message(
            notification=messaging.Notification(title=title,
                                                body=msg,
                                                ),
            token=registration_token
        )

        response = messaging.send(message)
        print('successfully sent message', response)

    @classmethod
    def send_push_to_token_with_data(cls, title, msg, registration_token, dataObject):
        message = messaging.Message(
            notification=messaging.Notification(title=title,
                                                body=msg,
                                                ),
            token=registration_token,
            data=dataObject
        )

        response = messaging.send(message)
        print('successfully sent message', response)

    @classmethod
    def send_push_to_token_with_condition(cls, title, msg, registration_token, condition):
        message = messaging.Message(
            notification=messaging.Notification(title=title,
                                                body=msg,
                                                ),
            token=registration_token,
            condition=condition
        )

        response = messaging.send(message)
        print('successfully sent message', response)

    # Ios specific
    @classmethod
    def send_push_to_token_with_ios_data(cls, title, msg, registration_token, dataObject):
        message = messaging.Message(
            notification=messaging.Notification(title=title,
                                                body=msg,
                                                ),
            token=registration_token,
            data=dataObject,
            apns_options=messaging.APNSFCMOptions(
                headers={
                    'apns-priority': '10'
                }
            )
        )

        response = messaging.send(message)
        print('successfully sent message', response)


    # android specific
    @classmethod
    def send_push_to_token_with_android_data(cls, title, msg, registration_token, dataObject):
        message = messaging.Message(
            notification=messaging.Notification(title=title,
                                                body=msg,
                                                ),
            token=registration_token,
            data=dataObject,
            android_options=messaging.AndroidNotification(
                priority='high'
            )
        )

        response = messaging.send(message)
        print('successfully sent message', response)



        