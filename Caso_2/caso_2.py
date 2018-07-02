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
    switch_suc5 = net.addSwitch('switch_suc5', cls=OVSKernelSwitch, failMode='standalone')
    switch_suc6 = net.addSwitch('switch_suc6', cls=OVSKernelSwitch, failMode='standalone')
    switch_suc2 = net.addSwitch('switch_suc2', cls=OVSKernelSwitch, failMode='standalone')
    switchLan_suc3 = net.addSwitch('switchLan_suc3', cls=OVSKernelSwitch, failMode='standalone')
    switch_suc3 = net.addSwitch('switch_suc3', cls=OVSKernelSwitch, failMode='standalone')
    switchLan_suc5 = net.addSwitch('switchLan_suc5', cls=OVSKernelSwitch, failMode='standalone')
    router_suc4 = net.addHost('router_suc4', cls=Node, ip='0.0.0.0')
    router_suc4.cmd('sysctl -w net.ipv4.ip_forward=1')
    switch_suc1 = net.addSwitch('switch_suc1', cls=OVSKernelSwitch, failMode='standalone')
    routerCentral = net.addHost('routerCentral', cls=Node, ip='0.0.0.0')
    routerCentral.cmd('sysctl -w net.ipv4.ip_forward=1')
    switchLan_suc4 = net.addSwitch('switchLan_suc4', cls=OVSKernelSwitch, failMode='standalone')
    switch_suc4 = net.addSwitch('switch_suc4', cls=OVSKernelSwitch, failMode='standalone')
    switchLan_suc1 = net.addSwitch('switchLan_suc1', cls=OVSKernelSwitch, failMode='standalone')
    router_suc6 = net.addHost('router_suc6', cls=Node, ip='0.0.0.0')
    router_suc6.cmd('sysctl -w net.ipv4.ip_forward=1')
    router_suc3 = net.addHost('router_suc3', cls=Node, ip='0.0.0.0')
    router_suc3.cmd('sysctl -w net.ipv4.ip_forward=1')
    router_suc5 = net.addHost('router_suc5', cls=Node, ip='0.0.0.0')
    router_suc5.cmd('sysctl -w net.ipv4.ip_forward=1')
    router_suc2 = net.addHost('router_suc2', cls=Node, ip='0.0.0.0')
    router_suc2.cmd('sysctl -w net.ipv4.ip_forward=1')
    switchLan_suc2 = net.addSwitch('switchLan_suc2', cls=OVSKernelSwitch, failMode='standalone')
    router_suc1 = net.addHost('router_suc1', cls=Node, ip='0.0.0.0')
    router_suc1.cmd('sysctl -w net.ipv4.ip_forward=1')
    switchLan_suc6 = net.addSwitch('switchLan_suc6', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Add hosts\n')
    hsuc1 = net.addHost('hsuc1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    hsuc2 = net.addHost('hsuc2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    hsuc5 = net.addHost('hsuc5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    hsuc6 = net.addHost('hsuc6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    hsuc3 = net.addHost('hsuc3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    hsuc4 = net.addHost('hsuc4', cls=Host, ip='10.0.0.4', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(switch_suc2, router_suc2)
    net.addLink(router_suc2, switchLan_suc2)
    net.addLink(switchLan_suc2, hsuc2)
    net.addLink(routerCentral, switch_suc3)
    net.addLink(switch_suc3, router_suc3)
    net.addLink(router_suc3, switchLan_suc3)
    net.addLink(switchLan_suc3, hsuc3)
    net.addLink(routerCentral, switch_suc5)
    net.addLink(switch_suc5, router_suc5)
    net.addLink(router_suc5, switchLan_suc5)
    net.addLink(switchLan_suc5, hsuc5)
    net.addLink(routerCentral, switch_suc6)
    net.addLink(switch_suc6, router_suc6)
    net.addLink(router_suc6, switchLan_suc6)
    net.addLink(switchLan_suc6, hsuc6)
    net.addLink(routerCentral, switch_suc1)
    net.addLink(switch_suc1, router_suc1)
    net.addLink(router_suc1, switchLan_suc1)
    net.addLink(switchLan_suc1, hsuc1)
    net.addLink(routerCentral, switch_suc2)
    net.addLink(routerCentral, switch_suc4)
    net.addLink(switch_suc4, router_suc4)
    net.addLink(router_suc4, switchLan_suc4)
    net.addLink(switchLan_suc4, hsuc4)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('switch_suc5').start([])
    net.get('switch_suc6').start([])
    net.get('switch_suc2').start([])
    net.get('switchLan_suc3').start([])
    net.get('switch_suc3').start([])
    net.get('switchLan_suc5').start([])
    net.get('switch_suc1').start([])
    net.get('switchLan_suc4').start([])
    net.get('switch_suc4').start([])
    net.get('switchLan_suc1').start([])
    net.get('switchLan_suc2').start([])
    net.get('switchLan_suc6').start([])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

