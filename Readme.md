nmap scanme.nmap.org

nmap -sV scanme.nmap.org

#nmap -sV --version-intensity 9 scanme.nmap.org

#nmap -A scanme.nmap.org or #nmap -sC -sV -O scanme.nmap.org

nmap -sP network/netmask

nmap --traceroute scanme.nmap.org

nmap -e interface scanme.nmap.org


port rage scan

#nmap -p80,443,22 scanme.nmap.org

#nmap -p1-100 scanme.nmap.org

#nmap -pT:22,U:53 scanme.nmap.org

#nmap -p http scanme.nmap.org

#nmap -p http* scanme.nmap.org

#nmap -p[1-65535] scanme.nmap.org


NSE

nmap -sV --script  scanme.nmap.org

nmap -sV --script http-title scanme.nmap.org

nmap -sv --script http-title, http-headers, scanme.nmap.org

nmap -sV --script vuln scanme.nmap.org

nmap -sV --script="version,discovery" scanme.nmap.org

nmap -sV --script "not exploit" scanme.nmap.org

nmap -sV --script "(http*)" and not (http-brute) scanme.nmap.org

nmap -sV --script exploit -d3 --script-trace scanme.nmap.org

nmap -sV --script http-title --script-args http.useragent="Mozilla 999"

nmap --script-updatedb

nmap -p"http*" --script http-methods --script-args http-merthods.retest scanme.nmap.org

nmap --script http-enum -p80 scanme.nmap.org

nmap -p80 --script http-userdir-enum

nmap -p80 --script http-unsafe-output-escaping  scanme.nmap.org

