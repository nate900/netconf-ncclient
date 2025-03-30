# imports
from ncclient import manager
import xml.dom.minidom
#router = {'host':'devnetsandboxiosxe.cisco.com', 'port': '830', 'username':'admin','password':'C1sco12345'}
from router import router

# this filter specifies a specific interface using the ietf-interfaces model
# yang models/capabilities
#http://cisco.com/ns/yang/Cisco-IOS-XE-native
#?module=Cisco-IOS-XE-native&revision=2018-02-01
#urn:ietf:params:xml:ns:yang:ietf-interfaces
netconf_filter_if="""
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet0/0/0</name>
        </interface>
    </interfaces>
</filter>
"""

native_filter = """
<filter>
    <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
    <interface>
        <name>GigabitEthernet0/0/0</name>
    </interface>
    </interfaces>
</filter>
"""

with manager.connect(host=router['host'], port=router['port'], username=router['username'], password=router['password'], hostkey_verify=False) as m:
    response = m.get(native_filter)
    xmlDom = xml.dom.minidom.parseString(str(response))
    print(xmlDom.toprettyxml(indent='   '))

    
    