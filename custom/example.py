""" this file is a custom topology using Python.
reference link:
https://blog.csdn.net/weixin_39616367/article/details/111450445
"""

from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI

net = Mininet(host=CPULimitedHost, link=TCLink)

#def addController( self, name='c0', controller=None, **params ):
c0 = net.addController()

# def addSwitch( self, name, cls=None, **params ):
s1 = net.addSwitch('s1')

#def addHost( self, name, cls=None, **params ):
h1 = net.addHost('h1')
h2 = net.addHost('h2', cpu=0.5)
h3 = net.addHost('h3', cpu=0.5)
h4 = net.addHost('h4', cpu=0.5)

#def addLink( self, node1, node2, port1=None, port2=None, cls=None, **params ):
net.addLink(s1, h1, bw=10, delay='5ms', max_queue_size=1000, loss=10, use_htb=True)
net.addLink(s1, h2)
net.addLink(s1, h3)
net.addLink(s1, h4)

#def ping( self, hosts=None, timeout=None ):
#net.pingAll()
print("here")
net.start()
net.pingAllFull()
net.pingAll()
CLI(net)    #Waiting for command
net.stop()
