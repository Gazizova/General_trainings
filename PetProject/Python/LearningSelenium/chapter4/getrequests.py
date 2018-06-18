import requests
from xml.etree import ElementTree
from xml import etree
# import xml.etree.ElementTree as ET

class Authenticate():
    token = 0
    def auth_as_superuser(self):
        headers = {'content-type': 'application/xml', 'Accept-Encoding': 'gzip,deflate', 'Content-Length': '201', 'Connection': 'Keep-Alive'}
        api_url = 'http://tetra-qa.strikersoft.com:8080'

        payload = """ 
        <dto:authTokenRequestDto xmlns:dto="dto.client.auth.tetra.strikersoft.com">
        <login>tetra-support@strikersoft.com</login>
        <password>Qqq!1234</password>
        <infinite>true</infinite>
        </dto:authTokenRequestDto>
        """

        r = requests.put('{}/tetra-auth/POPS/authenticate'.format(api_url), headers=headers, data=payload)
        # resp = r.content
        # print('>>>>>>>>>Response:{} {} {} {} \n{}'.format(r.url, r.status_code, r.reason, r.text, r.content)) #
        x = ElementTree.fromstring(r.content)
        find_token = x.find(".//tokenId")
        Authenticate.token = find_token.text
        print(Authenticate.token)
        return Authenticate.token


    def delete_project(self, projectCode=''):
        auth = Authenticate()
        auth.auth_as_superuser()
        newtoken = Authenticate.token
        headers = {'content-type': 'application/xml', 'Accept-Encoding': 'gzip,deflate', 'Content-Length': '0',
                   'Connection': 'Keep-Alive', 'tokenId': newtoken}
        api_url = 'http://tetra-qa.strikersoft.com:8080'

        r = requests.delete('{api_url}/pops/workflow/project/{pcode}'.format(api_url=api_url, pcode=projectCode), headers=headers)

        if r.status_code == 200:
            print("Success! status = " + str(r.status_code))
        else: print ("OOps! status = " + str(r.status_code))
        print(r.status_code)
        return r.status_code

auth = Authenticate().auth_as_superuser()

