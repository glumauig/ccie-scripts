#!/usr/bin/python3
from netmiko import ConnectHandler
from datetime import datetime

lab_ip={
'10.99.99.1',
'10.99.99.2',
'10.99.99.3',
'10.99.99.4',
'10.99.99.5',
'10.99.99.6',
'10.99.99.7',
'10.99.99.8',
'10.99.99.9',
'10.99.99.10',
'10.99.99.11',
'10.99.99.12',
'10.99.99.13',
'10.99.99.14'
}

for ip in lab_ip:
    net_connect = ConnectHandler(
            device_type="cisco_ios",
            host=ip,
            username="admin",
            password="P@ssw0rd",
    )
    output = net_connect.send_command('show run')
    datetoday = datetime.now()
    datetoday = datetoday.strftime("%m-%d-%Y_%H%M%S")
    filename = f"/root/git-folder/ccie-scripts/config_backup/"+datetoday+""+ip+".conf"
    with open(filename, 'w') as f:
        f.write(output)