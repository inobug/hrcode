import  xml.dom.minidom

class MyObj():
        #读取xml内容
        dom = xml.dom.minidom.parse('data.xml')
        data = dom.documentElement
        def __init__(self,tagname,action,index):
                """

                :param tagname: 获取的标签
                :param action: 获取的属性
                :param index: 获取的位置
                """
                self.tagname=tagname
                self.action=action
                self.index=index
        @property
        def name(self):
                un=''
                if  self.data.getElementsByTagName(self.tagname):
                        try:
                                item = self.data.getElementsByTagName('p')[self.index]
                                un = item.getAttribute(self.action)
                        except :
                                un='未找到标签，超出范围'

                return un
a=MyObj('p','name',1)
print(a.name)