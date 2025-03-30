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
print("Enter the name of the interface you want: ")
interface = input()
netconf_filter_if=f"""
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>{interface}</name>
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
    response = m.get(netconf_filter_if)
    xmlDom = xml.dom.minidom.parseString(str(response))
    print(xmlDom.toprettyxml(indent='   '))

    
    