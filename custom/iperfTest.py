# -*- coding: UTF-8 -*-
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


def IperfTest():
    net = Mininet(host=CPULimitedHost, link=TCLink)  # 如不限制性能，参数为空
    # 创建网络节点
    c0 = net.addController()
    h1 = net.addHost('h1', cpu=0.5)
    h2 = net.addHost('h2', cpu=0.5)
    h3 = net.addHost('h3')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    # 创建节点间的链路
    net.addLink(h1, s1, bw=10, delay='5ms', max_queue_size=1000, loss=10, use_htb=True)
    net.addLink(h3, s3, bw=10, delay='5ms', max_queue_size=1000, loss=10, use_htb=True)
    net.addLink(h2, s2, bw=10, delay='5ms', max_queue_size=1000, loss=10, use_htb=True)
    net.addLink(s1, s2)
    net.addLink(s3, s2)
    # 配置主机 ip
    h1.setIP('10.0.0.1', 24)
    h2.setIP('10.0.0.2', 24)
    h3.setIP('10.0.0.3', 24)
    net.start()
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    print("Testing network connectivity")
    net.pingAll()
    h1, h2, h3 = net.get('h1', 'h2', 'h3')
    net.iperf((h1, h3))
    net.iperf((h2, h1))
    net.iperf((h2, h3))
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')  # print the log when Configuring hosts, starting switches and controller
    IperfTest()
    #代码来自 https://www.cnblogs.com/robinxlh/p/2net.html
