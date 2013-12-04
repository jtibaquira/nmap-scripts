description = [[
  Este script retorna un mensaje si el puerto 27017 esta open
]]

---
-- @usage nmap --script hellomongodb <target>
-- @output undefine
-- @args <target>

author = "Juan Jacobo Tiabquirá M @j_k0"

license = "Same as Nmap--See http://nmap.org/book/man-legal.html"

categories = {"safe", "discovery", "default"}


local stdnse = require "stdnse"
local shortport = require "shortport"

portrule = shortport.portnumber({27017, 28017}, "tcp", {"open", "open|filtered"})

action = function(host, port)
  if port.number == 27017 then
     return string.format("ohh! Posiblemente tienes Mongodb corriendo en : %s , OS : %s ", host.ip, port.state)
  end

  if port.number == 28017 then
    return string.format(":P, Tienes una interface web para mongodb en  el puerto : %s", port.number)
  end

  return string.format("El script corrio")
end
