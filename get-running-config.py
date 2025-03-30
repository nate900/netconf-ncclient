from ncclient import manager
import xml.dom.minidom
#router = {'host':'devnetsandboxiosxe.cisco.com', 'port': '830', 'username':'admin','password':'C1sco12345'}
from router import router

with manager.connect(host=router['host'], port=router['port'], username=router['username'], password=router['password'], hostkey_verify=False) as m:
    xml_data = m.get_config('running')

    xmlDom = xml.dom.minidom.parseString(str(xml_data))
    print(xmlDom.toprettyxml(indent='   '))

