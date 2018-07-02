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
    switch_suc1 = net.addSwitch('switch_suc1', cls=OVSKernelSwitch, failMode='standalone')
    switch_suc2 = net.addSwitch('switch_suc2', cls=OVSKernelSwitch, failMode='standalone')
    switch_suc3 = net.addSwitch('switch_suc3', cls=OVSKernelSwitch, failMode='standalone')
    switch_suc4 = net.addSwitch('switch_suc4', cls=OVSKernelSwitch, failMode='standalone')
    switch_suc5 = net.addSwitch('switch_suc5', cls=OVSKernelSwitch, failMode='standalone')
    switch_suc6 = net.addSwitch('switch_suc6', cls=OVSKernelSwitch, failMode='standalone')
    routerCentral = net.addHost('routerCentral', cls=Node, ip='')
    routerCentral.cmd('sysctl -w net.ipv4.ip_forward=1')
    router_suc1 = net.addHost('router_suc1', cls=Node, ip='')
    router_suc1.cmd('sysctl -w net.ipv4.ip_forward=1')
    router_suc2 = net.addHost('router_suc2', cls=Node, ip='')
    router_suc2.cmd('sysctl -w net.ipv4.ip_forward=1')
    router_suc3 = net.addHost('router_suc3', cls=Node, ip='')
    router_suc3.cmd('sysctl -w net.ipv4.ip_forward=1')
    router_suc4 = net.addHost('router_suc4', cls=Node, ip='')
    router_suc4.cmd('sysctl -w net.ipv4.ip_forward=1')
    router_suc5 = net.addHost('router_suc5', cls=Node, ip='')
    router_suc5.cmd('sysctl -w net.ipv4.ip_forward=1')
    router_suc6 = net.addHost('router_suc6', cls=Node, ip='')
    router_suc6.cmd('sysctl -w net.ipv4.ip_forward=1')
    switchLan_suc1 = net.addSwitch('switchLan_suc1', cls=OVSKernelSwitch, failMode='standalone')
    switchLan_suc2 = net.addSwitch('switchLan_suc2', cls=OVSKernelSwitch, failMode='standalone')
    switchLan_suc3 = net.addSwitch('switchLan_suc3', cls=OVSKernelSwitch, failMode='standalone')
    switchLan_suc4 = net.addSwitch('switchLan_suc4', cls=OVSKernelSwitch, failMode='standalone')
    switchLan_suc5 = net.addSwitch('switchLan_suc5', cls=OVSKernelSwitch, failMode='standalone')
    switchLan_suc6 = net.addSwitch('switchLan_suc6', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Add hosts\n')
    host_suc1 = net.addHost('host_suc1', cls=Host, ip='10.0.1.254/24', defaultRoute="via 10.0.1.1")
    host_suc2 = net.addHost('host_suc2', cls=Host, ip='10.0.2.254/24', defaultRoute="via 10.0.2.1")
    host_suc3 = net.addHost('host_suc3', cls=Host, ip='10.0.3.254/24', defaultRoute="via 10.0.3.1")
    host_suc4 = net.addHost('host_suc4', cls=Host, ip='10.0.4.254/24', defaultRoute="via 10.0.4.1")
    host_suc5 = net.addHost('host_suc5', cls=Host, ip='10.0.5.254/24', defaultRoute="via 10.0.5.1")
    host_suc6 = net.addHost('host_suc6', cls=Host, ip='10.0.6.254/24', defaultRoute="via 10.0.6.1")

    info( '*** Add links\n')
    #Una manera de ponerle ip a cada interfaz del link, es de la siguiente manera
    #net.addLink(routerCentral, switch_suc1, intfName1='routerCentral-eth0', params1={'ip' : '192.168.100.6/24})
    net.addLink(routerCentral, switch_suc1)
    net.addLink(routerCentral, switch_suc2)
    net.addLink(routerCentral, switch_suc3)
    net.addLink(routerCentral, switch_suc4)
    net.addLink(routerCentral, switch_suc5)
    net.addLink(routerCentral, switch_suc6)
    net.addLink(switch_suc1, router_suc1)
    net.addLink(switch_suc2, router_suc2)
    net.addLink(switch_suc3, router_suc3)
    net.addLink(switch_suc4, router_suc4)
    net.addLink(switch_suc5, router_suc5)
    net.addLink(switch_suc6, router_suc6)
    net.addLink(router_suc1, switchLan_suc1)
    net.addLink(router_suc2, switchLan_suc2)
    net.addLink(router_suc3, switchLan_suc3)
    net.addLink(router_suc4, switchLan_suc4)
    net.addLink(router_suc5, switchLan_suc5)
    net.addLink(router_suc6, switchLan_suc6)
    net.addLink(switchLan_suc1, host_suc1)
    net.addLink(switchLan_suc2, host_suc2)
    net.addLink(switchLan_suc3, host_suc3)
    net.addLink(switchLan_suc4, host_suc4)
    net.addLink(switchLan_suc5, host_suc5)
    net.addLink(switchLan_suc6, host_suc6)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('switch_suc1').start([])
    net.get('switch_suc2').start([])
    net.get('switch_suc3').start([])
    net.get('switch_suc4').start([])
    net.get('switch_suc5').start([])
    net.get('switch_suc6').start([])
    net.get('switchLan_suc1').start([])
    net.get('switchLan_suc2').start([])
    net.get('switchLan_suc3').start([])
    net.get('switchLan_suc4').start([])
    net.get('switchLan_suc5').start([])
    net.get('switchLan_suc6').start([])

    info( '*** Post configure switches and hosts\n')
    info( '*** Configuring routerCentral Interfaces\n' )
    routerCentral.cmd('ip addr add 192.168.100.06/29 dev routerCentral-eth0 brd +')
    routerCentral.cmd('ip addr add 192.168.100.14/29 dev routerCentral-eth1 brd +')
    routerCentral.cmd('ip addr add 192.168.100.22/29 dev routerCentral-eth2 brd +')
    routerCentral.cmd('ip addr add 192.168.100.30/29 dev routerCentral-eth3 brd +')
    routerCentral.cmd('ip addr add 192.168.100.38/29 dev routerCentral-eth4 brd +')
    routerCentral.cmd('ip addr add 192.168.100.46/29 dev routerCentral-eth5 brd +')
    result = routerCentral.cmd('ip a')
    print result

    info( '*** Configuring RSuc Interfaces\n' )
    router_suc1.cmd('ip addr add 192.168.100.1/29 dev router_suc1-eth0 brd +')
    router_suc2.cmd('ip addr add 192.168.100.9/29 dev router_suc2-eth0 brd +')
    router_suc3.cmd('ip addr add 192.168.100.17/29 dev router_suc3-eth0 brd +')
    router_suc4.cmd('ip addr add 192.168.100.25/29 dev router_suc4-eth0 brd +')
    router_suc5.cmd('ip addr add 192.168.100.33/29 dev router_suc5-eth0 brd +')
    router_suc6.cmd('ip addr add 192.168.100.41/29 dev router_suc6-eth0 brd +')
    router_suc1.cmd('ip addr add 10.0.1.1/24 dev router_suc1-eth1 brd +')
    router_suc2.cmd('ip addr add 10.0.2.1/24 dev router_suc2-eth1 brd +')
    router_suc3.cmd('ip addr add 10.0.3.1/24 dev router_suc3-eth1 brd +')
    router_suc4.cmd('ip addr add 10.0.4.1/24 dev router_suc4-eth1 brd +')
    router_suc5.cmd('ip addr add 10.0.5.1/24 dev router_suc5-eth1 brd +')
    router_suc6.cmd('ip addr add 10.0.6.1/24 dev router_suc6-eth1 brd +')
    result = router_suc1.cmd('ip a')
    print result

    info( '*** Configuring routerCentral Routes\n' )
    routerCentral.cmd('ip route add 10.0.1.0/24 via 192.168.100.1')
    routerCentral.cmd('ip route add 10.0.2.0/24 via 192.168.100.9')
    routerCentral.cmd('ip route add 10.0.3.0/24 via 192.168.100.17')
    routerCentral.cmd('ip route add 10.0.4.0/24 via 192.168.100.25')
    routerCentral.cmd('ip route add 10.0.5.0/24 via 192.168.100.33')
    routerCentral.cmd('ip route add 10.0.6.0/24 via 192.168.100.41')
    result = routerCentral.cmd('ip ro')
    print result
	
    info( '*** Configuring RSuc Routes\n' )
    router_suc1.cmd('ip route add 10.0.0.0/21 via 192.168.100.6')
    router_suc2.cmd('ip route add 10.0.0.0/21 via 192.168.100.14')
    router_suc3.cmd('ip route add 10.0.0.0/21 via 192.168.100.22')
    router_suc4.cmd('ip route add 10.0.0.0/21 via 192.168.100.30')
    router_suc5.cmd('ip route add 10.0.0.0/21 via 192.168.100.38')
    router_suc6.cmd('ip route add 10.0.0.0/21 via 192.168.100.46')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()