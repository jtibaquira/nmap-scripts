import nmap

nma = nmap.PortScannerAsync()
def callback_result(host,result):
  print host, result

nma.scan('192.168.1.1/24',arguments="-sS -sV -p10-5000",callback=callback_result)

while nma.still_scanning():
  nma.wait(2)