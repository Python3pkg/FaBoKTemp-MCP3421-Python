# coding: utf-8
## @package FaBoKTemp_MCP3421
#  This is a library for the FaBo KTemp I2C Brick.
#
#  http://fabo.io/209.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBoKTemp_MCP3421
import time

mcp3421 = FaBoKTemp_MCP3421.MCP3421()

while True:
    temp = mcp3421.read()
    print "KTemp = ", (temp)
    print
    time.sleep(1)
