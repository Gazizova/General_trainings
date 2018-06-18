import csv
import requests
from xml.etree import ElementTree
from xml import etree


#
class A(object):
    def __init__(self):
        print("123")


#
class B(A):
    def __init__(self):
        print(u'123456')
        super(B, self).__init__()

# a = A()
b = B()
# data = []
# with open('project.csv') as csvfile:
#      reader = csv.DictReader(csvfile)
#      for row in reader:
#          # print row
#          print(row['Ref Num'], row['Stage'])
#          data.append(row['Ref Num'])
# print(data)

# def split_var(i):
#     return i.lstrip(' ')[0]
#
# print split_var('1 2 3')
#
#
# def lower(i):
#     return i.lower()
#
# print (lower("AaaAaaA"))
#
#
# def match(i, x):
#     return i.match( \w+, x)
#
# print (match("asd, asd, ert, sdf, ert, sd", "sd"))


# def auth_as_superuser(api_url='', projectCode=''):
#     headers = {'content-type': 'application/xml', 'Accept-Encoding': 'gzip,deflate', 'Content-Length': '201',
#                'Connection': 'Keep-Alive'}
#     # api_url = 'http://tetra-qa.strikersoft.com:8080'
#     payload = """
#     <dto:authTokenRequestDto xmlns:dto="dto.client.auth.tetra.strikersoft.com">
#     <login>tetra-support@strikersoft.com</login>
#     <password>Qqq!1234</password>
#     <infinite>true</infinite>
#     </dto:authTokenRequestDto>
#     """
#     r = requests.put('{}/tetra-auth/POPS/authenticate'.format(api_url), headers=headers, data=payload)
#     # resp = r.content
#     # print('>>>>>>>>>Response:{} {} {} {} \n{}'.format(r.url, r.status_code, r.reason, r.text, r.content)) #
#     x = ElementTree.fromstring(r.content)
#     find_token = x.find(".//tokenId")
#     token = find_token.text
#     print(token)
#     # return token
#
#     headers = {'content-type': 'application/xml', 'Accept-Encoding': 'gzip,deflate', 'Content-Length': '0',
#                'Connection': 'Keep-Alive', 'tokenId': token}
#     # api_url = 'http://tetra-qa.strikersoft.com:8080'
#     r = requests.delete('{api_url}/pops/workflow/project/{pcode}'.format(api_url=api_url, pcode=projectCode), headers=headers)
#
#     if r.status_code == 200:
#         print("Success! status = " + str(r.status_code))
#     else: print ("OOps! status = " + str(r.status_code))
#     print(r.status_code)
#     return r.status_code
#
# auth = auth_as_superuser('http://tetra-qa.strikersoft.com:8080', "TestQa-12102016" )