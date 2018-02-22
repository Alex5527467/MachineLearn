# -*- coding: utf-8 -*-
from graphviz import Digraph

dot = Digraph(comment='The Round Table')

#添加圆点 A, A的标签是 King Arthur
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')
print dot.source
dot.view()  #后面这句就注释了，也可以使用这个命令查看效果
