# -*- coding: UTF-8 -*-
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):
    def __init__(self, n=2, **opts):
        Topo.__init__(self, **opts) # 初始化拓扑以及默认的option
        switch = self.addSwitch('s1') # 添加一个名为s1的交换机
        for h in range(n):
            host = self.addHost('h%s' % (h + 1)) #添加主机
            self.addLink(host, switch) #添加双向连接
    def simpleTest(self):
        topo = SingleSwitchTopo(n=4)
        net = Mininet(topo) #用Main Class来创建拓扑
        net.start() #启动网络
        print("Dumping host connections")
        dumpNodeConnections(net.hosts) #显示拓扑内所有节点（host）的connection信息
        print("Testing network connectivity")
        net.pingAll() #所有host相互ping对方，用来测试网络连接性
        net.stop()


if __name__ == '__main__':
    setLogLevel('info') # 设置 Mininet 默认输出级别为info
    simpletest = SingleSwitchTopo()
    simpletest.simpleTest()
