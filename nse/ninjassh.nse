description = [[
  Este script retorna un mensaje si el puerto 22 esta open,
  esta desarrollado como ejemplo para el curso de 0 a ninja con nmap
]]

---
-- @usage nmap --script mongodbtest <target>
-- @output undefine
-- @args <target>

author = "Jacobo Tiabquirá @jjtibaquira jko@dragonjar.org"

license = "Same as Nmap--See http://nmap.org/book/man-legal.html"

categories = {"safe", "discovery", "default"}


local stdnse = require "stdnse"
local shortport = require "shortport"

portrule = shortport.portnumber(22, "tcp", {"open", "open|filtered","closed","filtered"})

action = function(host, port)
  if port.number == 22 then
    return string.format("ohh! Posiblemente tienes SSH corriendo : %s , OS : %s ", host.ip, port.state)
  end

  return string.format("El script corrio")
end