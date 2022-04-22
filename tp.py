#!/usr/bin/python

from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch
from mininet.topo import Topo

class test_topo(Topo):



    def __init__(self):


        Topo.__init__(self)

         #Add hosts
        h1 = self.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
        h2 = self.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
        h3 = self.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
        h4 = self.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)

        #Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
	s3 = self.addSwitch('s3')

        #Add links
	self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s3, s2)

        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)

topos = { 'mytopo': (lambda: test_topo() ) }