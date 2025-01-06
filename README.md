This Python script gets all zones and writes the DNS Records into json files for ALL zones the specified Cloudflare account. You need to get Beaarer Token ID to retrieve the records.
- cloudflare_all_zones_records-export-"+datetimenow+".json file contains all zone records
- cloudflare_dns_records-export-"+zone_name+"-"+datetimenow+".json file contains all DNS records for zone_name
