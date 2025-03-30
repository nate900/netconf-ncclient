# imports
from ncclient import manager
import xml.dom.minidom
import net_devs
router = net_devs.get_homelab_4331()

# this filter specifies a specific interface using the ietf-interfaces model
# yang models/capabilities
#http://cisco.com/ns/yang/Cisco-IOS-XE-native
#?module=Cisco-IOS-XE-native&revision=2018-02-01
#urn:ietf:params:xml:ns:yang:ietf-interfaces

# this filter fets all interfaces
netconf_filter_interfaces="""
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    </interfaces>
</filter>
"""

with manager.connect(host=router['host'], port=router['port'], username=router['username'], password=router['password'], hostkey_verify=False) as m:
    response = m.get(netconf_filter_interfaces)
    xmlDom = xml.dom.minidom.parseString(str(response))
    print(xmlDom.toprettyxml(indent='   '))

    
    