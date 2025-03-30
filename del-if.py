from ncclient import manager
import net_devs
router = net_devs.get_homelab_4331()

print("Enter the name of the loopback you want deleted: ")
interface = input()

netconf_snippet = f"""
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="delete">
            <name>{interface}</name>
        </interface>
    </interfaces>
</config>
"""

loopback = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="delete">
            <name>Loopback1000</name>
            <description>someting else</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
            <enabled>true</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>20.20.20.20</ip>
                    <netmask>255.255.255.255</netmask>
                </address>
            </ipv4>
            <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
        </interface>
    </interfaces>
</config>
"""

with manager.connect(host=router['host'], port=router['port'], username=router['username'], password=router['password'], hostkey_verify=False) as m:
    data = m.edit_config(netconf_snippet, target='running')
    print(data)