from ncclient import manager
import xml.dom.minidom
import net_devs
router = net_devs.get_homelab_4331()

with manager.connect(host=router['host'], port=router['port'], username=router['username'], password=router['password'], hostkey_verify=False) as m:
    xml_data = m.get_config('running')

    xmlDom = xml.dom.minidom.parseString(str(xml_data))
    print(xmlDom.toprettyxml(indent='   '))

