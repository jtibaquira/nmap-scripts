import nmap

class NmapHost:
  def __init__(self):
    self.host = None
    self.state = None
    self.reason = None
    self.openPorts = []
    self.closedFilteredPorts = []

class NmapPort:
  def __init__(self):
    self.id = None
    self.host = None
    self.state = None
    self.reason = None
    self.port = None
    self.version = None
    self.scriptOutput = None

def parseNmapScan(scan):
  nmapHosts = []
  for host in scan.all_hosts():
    nmapHost = NmapHost()
    nmapHost.host = host
    if scan[host].has_key('status'):
      nmapHost.state = scan[host]['status']['state']
      nmapHost.reason = scan[host]['status']['reason']
      for protocol in ["tcp","udp","icmp"]:
        if scan[host].has_key(protocol):
          ports = scan[host][protocol].keys()
          for port in ports:
            nmapPort = NmapPort()
            nmapPort.port = port
            nmapPort.state = scan[host][protocol][port]['state']
            if scan[host][protocol][port].has_key('script'):
              nmapPort.scriptOutput = scan[host][protocol][port]['script']
            if scan[host][protocol][port].has_key('reason'):
              nmapPort.reason = scan[host][protocol][port]['reason']
            if scan[host][protocol][port].has_key('name'):
              nmapPort.name = scan[host][protocol][port]['name']
            if scan[host][protocol][port].has_key('version'):
              nmapPort.version = scan[host][protocol][port]['version']
            if 'open' in (scan[host][protocol][port]['state']):
              nmapHost.openPorts.append(nmapPort)
            else:
              nmapHost.closedFilteredPorts.append(nmapPort)
          nmapHosts.append(nmapHost)

          for nmapHost in nmapHosts:
            print "[+] Host: "+nmapHost.host
            for openPorts in nmapHost.openPorts:
              print "\t[++]"+str(openPorts.port), openPorts.state,  openPorts.version
              if not openPorts.scriptOutput == None:
                for k,v in openPorts.scriptOutput.iteritems():
                  print "\t\t[+++]"+k+"==> "+v
    else:
      print "[-] Resultados no encontrados en %s" %(protocol)
      return nmapHosts

if __name__ == '__main__':
  nm = nmap.PortScanner()
  nm.scan("192.168.1.7,19",arguments="-sC -sS -sV -p-")
  structureNmap = parseNmapScan(nm)
