import json
import requests
import pprint
from datetime import datetime

cloudflare_api = "https://api.cloudflare.com/client/v4/"

api_token = "Bearer XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
headers = {'Authorization': api_token, 'Content-Type':'application/json'}

today = datetime.now()
datetimenow = today.strftime('%Y-%m-%d-%H%M%S')
export_filename = "./cloudflare_all_zones_records-export-"+datetimenow+".json"

cloudflare_dns = cloudflare_api + "zones?page=1&per_page=500"
cloudflare_dns_response = requests.get(cloudflare_dns, headers=headers, )

if cloudflare_dns_response.status_code == 200:
    dns_data = json.loads(cloudflare_dns_response.text)

    with open(export_filename, 'w') as json_file:
        json.dump(dns_data, json_file, indent=1)
#    pprint.pprint(dns_data["result"])

    for zones in dns_data["result"]:
        zone_name = zones["name"]
        zone_id = zones["id"]
        export_filename = "./cloudflare_dns_records-export-"+zone_name+"-"+datetimenow+".json"
        cloudflare_dns = cloudflare_api + "zones/" + zone_id + "/dns_records"
        cloudflare_dns_response = requests.get(cloudflare_dns, headers=headers)

        if cloudflare_dns_response.status_code == 200:
            dns_data = json.loads(cloudflare_dns_response.text)
            #pprint.pprint(dns_data)

            with open(export_filename, 'w') as json_file:
                json.dump(dns_data, json_file, indent=1)
            pprint.pprint("Zone "+zone_name+" "+zone_id+" Exported to "+export_filename)
        else:
            print(cloudflare_dns_response.status_code)
else:
    print(cloudflare_dns_response.status_code)

