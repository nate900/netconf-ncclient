from ncclient import manager
import xml.dom.minidom
import net_devs
router = net_devs.get_homelab_4331()

with manager.connect(host=router['host'], port=router['port'], username=router['username'], password=router['password'], hostkey_verify=False) as m:
    schema = m.get_schema('Cisco-IOS-XE-native')
    print(schema)


    