#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    swSuc1 = net.addSwitch('swSuc1', cls=OVSKernelSwitch, failMode='standalone')
    swSuc2 = net.addSwitch('swSuc2', cls=OVSKernelSwitch, failMode='standalone')
    swSuc3 = net.addSwitch('swSuc3', cls=OVSKernelSwitch, failMode='standalone')
    swSuc4 = net.addSwitch('swSuc4', cls=OVSKernelSwitch, failMode='standalone')
    swSuc5 = net.addSwitch('swSuc5', cls=OVSKernelSwitch, failMode='standalone')
    swSuc6 = net.addSwitch('swSuc6', cls=OVSKernelSwitch, failMode='standalone')
    rPrincipal = net.addHost('rPrincipal', cls=Node, ip='')
    rPrincipal.cmd('sysctl -w net.ipv4.ip_forward=1')
    roSuc1 = net.addHost('roSuc1', cls=Node, ip='')
    roSuc1.cmd('sysctl -w net.ipv4.ip_forward=1')
    roSuc2 = net.addHost('roSuc2', cls=Node, ip='')
    roSuc2.cmd('sysctl -w net.ipv4.ip_forward=1')
    roSuc3 = net.addHost('roSuc3', cls=Node, ip='')
    roSuc3.cmd('sysctl -w net.ipv4.ip_forward=1')
    roSuc4 = net.addHost('roSuc4', cls=Node, ip='')
    roSuc4.cmd('sysctl -w net.ipv4.ip_forward=1')
    roSuc5 = net.addHost('roSuc5', cls=Node, ip='')
    roSuc5.cmd('sysctl -w net.ipv4.ip_forward=1')
    roSuc6 = net.addHost('roSuc6', cls=Node, ip='')
    roSuc6.cmd('sysctl -w net.ipv4.ip_forward=1')
    slSuc1 = net.addSwitch('slSuc1', cls=OVSKernelSwitch, failMode='standalone')
    slSuc2 = net.addSwitch('slSuc2', cls=OVSKernelSwitch, failMode='standalone')
    slSuc3 = net.addSwitch('slSuc3', cls=OVSKernelSwitch, failMode='standalone')
    slSuc4 = net.addSwitch('slSuc4', cls=OVSKernelSwitch, failMode='standalone')
    slSuc5 = net.addSwitch('slSuc5', cls=OVSKernelSwitch, failMode='standalone')
    slSuc6 = net.addSwitch('slSuc6', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Add hosts\n')
    host_suc1 = net.addHost('host_suc1', cls=Host, ip='10.0.1.254/24', defaultRoute="via 10.0.1.1")
    host_suc2 = net.addHost('host_suc2', cls=Host, ip='10.0.2.254/24', defaultRoute="via 10.0.2.1")
    host_suc3 = net.addHost('host_suc3', cls=Host, ip='10.0.3.254/24', defaultRoute="via 10.0.3.1")
    host_suc4 = net.addHost('host_suc4', cls=Host, ip='10.0.4.254/24', defaultRoute="via 10.0.4.1")
    host_suc5 = net.addHost('host_suc5', cls=Host, ip='10.0.5.254/24', defaultRoute="via 10.0.5.1")
    host_suc6 = net.addHost('host_suc6', cls=Host, ip='10.0.6.254/24', defaultRoute="via 10.0.6.1")

    info( '*** Add links\n')
    #Una manera de ponerle ip a cada interfaz del link, es de la siguiente manera
    #net.addLink(rPrincipal, swSuc1, intfName1='rPrincipal-eth0', params1={'ip' : '192.168.100.6/24})
    net.addLink(rPrincipal, swSuc1)
    net.addLink(rPrincipal, swSuc2)
    net.addLink(rPrincipal, swSuc3)
    net.addLink(rPrincipal, swSuc4)
    net.addLink(rPrincipal, swSuc5)
    net.addLink(rPrincipal, swSuc6)
    net.addLink(swSuc1, roSuc1)
    net.addLink(swSuc2, roSuc2)
    net.addLink(swSuc3, roSuc3)
    net.addLink(swSuc4, roSuc4)
    net.addLink(swSuc5, roSuc5)
    net.addLink(swSuc6, roSuc6)
    net.addLink(roSuc1, slSuc1)
    net.addLink(roSuc2, slSuc2)
    net.addLink(roSuc3, slSuc3)
    net.addLink(roSuc4, slSuc4)
    net.addLink(roSuc5, slSuc5)
    net.addLink(roSuc6, slSuc6)
    net.addLink(slSuc1, host_suc1)
    net.addLink(slSuc2, host_suc2)
    net.addLink(slSuc3, host_suc3)
    net.addLink(slSuc4, host_suc4)
    net.addLink(slSuc5, host_suc5)
    net.addLink(slSuc6, host_suc6)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('swSuc1').start([])
    net.get('swSuc2').start([])
    net.get('swSuc3').start([])
    net.get('swSuc4').start([])
    net.get('swSuc5').start([])
    net.get('swSuc6').start([])
    net.get('slSuc1').start([])
    net.get('slSuc2').start([])
    net.get('slSuc3').start([])
    net.get('slSuc4').start([])
    net.get('slSuc5').start([])
    net.get('slSuc6').start([])

    info( '*** Post configure switches and hosts\n')
    info( '*** Configuring rPrincipal Interfaces\n' )
    rPrincipal.cmd('ip addr add 192.168.100.06/29 dev rPrincipal-eth0 brd +')
    rPrincipal.cmd('ip addr add 192.168.100.14/29 dev rPrincipal-eth1 brd +')
    rPrincipal.cmd('ip addr add 192.168.100.22/29 dev rPrincipal-eth2 brd +')
    rPrincipal.cmd('ip addr add 192.168.100.30/29 dev rPrincipal-eth3 brd +')
    rPrincipal.cmd('ip addr add 192.168.100.38/29 dev rPrincipal-eth4 brd +')
    rPrincipal.cmd('ip addr add 192.168.100.46/29 dev rPrincipal-eth5 brd +')
    result = rPrincipal.cmd('ip a')
    print result

    info( '*** Configuring RSuc Interfaces\n' )
    roSuc1.cmd('ip addr add 192.168.100.1/29 dev roSuc1-eth0 brd +')
    roSuc2.cmd('ip addr add 192.168.100.9/29 dev roSuc2-eth0 brd +')
    roSuc3.cmd('ip addr add 192.168.100.17/29 dev roSuc3-eth0 brd +')
    roSuc4.cmd('ip addr add 192.168.100.25/29 dev roSuc4-eth0 brd +')
    roSuc5.cmd('ip addr add 192.168.100.33/29 dev roSuc5-eth0 brd +')
    roSuc6.cmd('ip addr add 192.168.100.41/29 dev roSuc6-eth0 brd +')
    roSuc1.cmd('ip addr add 10.0.1.1/24 dev roSuc1-eth1 brd +')
    roSuc2.cmd('ip addr add 10.0.2.1/24 dev roSuc2-eth1 brd +')
    roSuc3.cmd('ip addr add 10.0.3.1/24 dev roSuc3-eth1 brd +')
    roSuc4.cmd('ip addr add 10.0.4.1/24 dev roSuc4-eth1 brd +')
    roSuc5.cmd('ip addr add 10.0.5.1/24 dev roSuc5-eth1 brd +')
    roSuc6.cmd('ip addr add 10.0.6.1/24 dev roSuc6-eth1 brd +')
    result = roSuc1.cmd('ip a')
    print result

    info( '*** Configuring rPrincipal Routes\n' )
    rPrincipal.cmd('ip route add 10.0.1.0/24 via 192.168.100.1')
    rPrincipal.cmd('ip route add 10.0.2.0/24 via 192.168.100.9')
    rPrincipal.cmd('ip route add 10.0.3.0/24 via 192.168.100.17')
    rPrincipal.cmd('ip route add 10.0.4.0/24 via 192.168.100.25')
    rPrincipal.cmd('ip route add 10.0.5.0/24 via 192.168.100.33')
    rPrincipal.cmd('ip route add 10.0.6.0/24 via 192.168.100.41')
    result = rPrincipal.cmd('ip ro')
    print result
	
    info( '*** Configuring RSuc Routes\n' )
    roSuc1.cmd('ip route add 10.0.0.0/21 via 192.168.100.6')
    roSuc2.cmd('ip route add 10.0.0.0/21 via 192.168.100.14')
    roSuc3.cmd('ip route add 10.0.0.0/21 via 192.168.100.22')
    roSuc4.cmd('ip route add 10.0.0.0/21 via 192.168.100.30')
    roSuc5.cmd('ip route add 10.0.0.0/21 via 192.168.100.38')
    roSuc6.cmd('ip route add 10.0.0.0/21 via 192.168.100.46')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()