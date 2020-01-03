#!/usr/bin/env python
# encoding: utf-8

from cortexutils.responder import Responder
import requests

class Netcraft(Responder):
    def __init__(self):
        Responder.__init__(self)
        self.account_username = self.get_param('config.account_username', None, "Service account username missing")
        self.account_password = self.get_param('config.account_password', None, "Service account password missing")
        self.account_region = self.get_param('config.account_region', None, "Service account region missing")

    def run(self):
        Responder.run(self)

        if self.get_param('data.dataType') == 'url':

            url = self.get_param('data.data', None, 'No artifacts available')

            # URL API
            link = "https://takedown.netcraft.com/authorise.php"
            # Data for API requests
            data = {
            'attack': url,
            'region': self.account_region,
            'comment': 'Ticket report'
            }

            # API requests
            response = requests.post(link, data=data, auth=(self.account_username, self.account_password))

            if response.status_code == 200 :
                answer = response.text.split("\n")
                td_answer = answer[0]
                if(td_answer == "TD_OK"):
                    td_ticket = answer[1]
                    self.report({'message': 'URL reported. Ticket #'+str(answer[1])})
                elif(td_answer == "TD_EXISTS"):
                    td_ticket = answer[1]
                    self.report({'message': 'URL already reported. Ticket #'+str(answer[1])})
                elif(td_answer == "TD_VERIFY"):
                    self.report({'message': 'URL undergoing verification.'})
                elif(td_answer == "TD_WILDCARD"):
                    self.report({'message': 'Wilcard sub-domain already reported.'})
                else:
                    # No authorization / credits
                    self.error('Error')
            else:
                # Error
                self.error('Error')

	else:
	    self.error('Incorrect dataType. "URL" expexted.')

    def operations(self, raw):
        return [self.build_operation('AddTagToArtifact', tag='Netcraft:reported')]

if __name__ == '__main__':
        Netcraft().run()