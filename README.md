Python tool to analyse apache2 logs. Works best when combined with <a href="https://github.com/PadiBo/apache2_ip_blocking">apache2_ip_blocking</a>

1. Download repository as zip and unzip or clone to a place you want.
2. Edit lines 197-199 in /overview/update_overview.py, add your server settings.
3. Open overview.xslx and add IPs that should be excluded from the overview file -> your private IPs (ranges doesn't work)
4. Run update_overview.py.

tools in this repository:<br>
<p><b>asn_ranges</b> -> downloads asn database from https://iptoasn.com/ and formats it in csv file</p>
<p><b>geo_locate</b> -> gets IP's in overview.xlsx from sheet IPs</p>
<p><b>overview</b> -> Excel sheet to analyse the apache logs</p>
<p><b>search_ip_in_range</b> -> check if all IPs in ip.txt are in the ranges from ranges.txt (I use this tool to check if all IPs that sould be blocked by ip blocker, are really blocked)</p>

Needed python libs:
paramiko, time, os, gzip, re, pandas, shutil, datetime, openpyxl, requests, csv

To install all libs run:
```
pip install time os gzip re pandas shutil datetime openpyxl reqests csv
```
