from datetime import datetime as dt


class JimClientMessage:
    def auth(self, username, password):

        data = {
            "action": "authenticate",
            "time": dt.now().timestamp(),
            "user": {
                "account_name": username,
                "password": password
            }
        }

        return data

    def presence(self, sender, status="Yep, I am here!"):

        data = {
            "action": "presence",
            "time": dt.now().timestamp(),
            "type": "status",
            "user": {
                "account_name": sender,
                "status": status
            }
        }
        return data

    def quit(self, sender, status="disconnect"):

        data = {
            "action": "quit",
            "time": dt.now().timestamp(),
            "type": "status",
            "user": {
                "account_name": sender,
                "status": status
            }
        }
        return data

    def list_(self, sender, status="show", person=''):

        data = {
            "action": "list",
            "time": dt.now().timestamp(),
            "type": "status",
            "contact_list": 'No contacts yet',
            "user": {
                "account_name": sender,
                "status": status,
                "contact": person
            }
        }
        return data

    def message(self, sender, receiver='user1', text='some msg text'):

        data = {
            "action": "msg",
            "time": dt.now().timestamp(),
            "to": receiver,
            "from": sender,
            "encoding": 'utf-8',
            "message": text
        }

        return data

