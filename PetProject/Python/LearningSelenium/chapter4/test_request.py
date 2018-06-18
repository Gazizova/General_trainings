import requests
from xml.etree import ElementTree

class Test():
    def auth_as_superuser(self):
        headers = {'content-type': 'application/xml', 'Accept-Encoding': 'gzip,deflate', 'Content-Length': '201',
                   'Connection': 'Keep-Alive'}
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
        token = find_token.text
        print(token)
        return token

auth = Test().auth_as_superuser()