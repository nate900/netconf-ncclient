from ncclient import manager
import xml.dom.minidom
router = {'host':'devnetsandboxiosxe.cisco.com', 'port': '830', 'username':'admin','password':'C1sco12345'}

netconf_filter = """
    <filter>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
    </filter>
"""

with manager.connect(host=router['host'], port=router['port'], username=router['username'], password=router['password'], hostkey_verify=False) as m:
    #for capability in m.server_capabilities:
        #print('*' * 50)
        #print(capability)
    #xml_data = m.get_config('running')
    xml_data = m.get(netconf_filter)

    xmlDom = xml.dom.minidom.parseString(str(xml_data))
    print(xmlDom.toprettyxml(indent='   '))
    #interfaces_netconf = m.dispatch(netconf_filter)

    
    
    

        