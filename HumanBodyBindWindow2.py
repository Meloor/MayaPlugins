import maya.cmds as cmds
import os
#help窗口类
class HelpDialog(object):
    """A class for a window to create a cone pointing in a direciton"""
    ## reference to the most recent instance
    use = None#类属性，临时存储调用它的__init__()方法时所创建的实例
    @classmethod
    def showUI(cls, uiFile):
        """A function to instantiate the window"""
        win = cls(uiFile)
        win.create()
        return win
    def __init__(self, filePath):#filePath指定.ui文件在磁盘上的位置
        """Initialize data attributes"""
        ## allow controls to initialize using class attribute
        HelpDialog.use = self#类属性，临时存储调用它的__init__()方法时所创建的实例
        ## unique window handle
        self.window = 'help_dialog'#实例属性，
        ## the path to the .ui file
        self.uiFile = filePath
    def create(self, verbose=False):#verbose=True时，输出GUI中可用的小组件的信息
        self.window = cmds.loadUI(#将.ui文件转换成maya可识别的控件
            uiFile=self.uiFile,
            verbose=verbose
        )
        cmds.showWindow(self.window)

#关于窗口
class AboutDialog(object):
    """A class for a window to create a cone pointing in a direciton"""
    ## reference to the most recent instance
    use = None#类属性，临时存储调用它的__init__()方法时所创建的实例
    @classmethod
    def showUI(cls, uiFile):
        """A function to instantiate the window"""
        win = cls(uiFile)
        win.create()
        return win
    def __init__(self, filePath):#filePath指定.ui文件在磁盘上的位置
        """Initialize data attributes"""
        ## allow controls to initialize using class attribute
        AboutDialog.use = self#类属性，临时存储调用它的__init__()方法时所创建的实例
        ## unique window handle
        self.window = 'about_dialog'#实例属性，
        ## the path to the .ui file
        self.uiFile = filePath
    def create(self, verbose=False):#verbose=True时，输出GUI中可用的小组件的信息
        self.window = cmds.loadUI(#将.ui文件转换成maya可识别的控件
            uiFile=self.uiFile,
            verbose=verbose
        )
        cmds.showWindow(self.window)
           
#主窗口类        
class HumanBodyBindWindow(object):
    """A class for a window to create a cone pointing in a direciton"""
    ## reference to the most recent instance
    use = None#类属性，临时存储调用它的__init__()方法时所创建的实例
    @classmethod
    def showUI(cls, uiFile):
        """A function to instantiate the window"""
        win = cls(uiFile)
        win.create()
        return win
    def __init__(self, filePath):#filePath指定.ui文件在磁盘上的位置
        """Initialize data attributes"""
        ## allow controls to initialize using class attribute
        HumanBodyBindWindow.use = self#类属性，临时存储调用它的__init__()方法时所创建的实例
        ## unique window handle
        self.window = 'human_bone_bind_window'#实例属性，
        ## name of rotation input field
        self.jnt_num = 'jnt_num_2'
        self.ctrl_jnt_num = 'ctrl_jnt_num'
        try:
            ctrlPath = '|'.join(
                [self.window,'centralwidget','body_tbx','waist','waist_tbx','w_bone',self.jnt_num]
            )
            rotation = float(
                #0.0
                #cmds.textField(ctrlPath, e=True, text=True,enterCommand=('7'))
            )
        except: raise
        ## the path to the .ui file
        self.uiFile = filePath
    def create(self, verbose=False):#verbose=True时，输出GUI中可用的小组件的信息
        """Draw the window"""
        # delete the window if its handle exists
        #if cmds.window(self.window, exists=True):
         #   cmds.deleteUI(self.window)
         #上面这两行可以不要，不同于windows命令，如果存在冲突，loadUI命令将自动
         #递增所创建的窗口的名称，这非常类似于transform节点的命名
        # initialize the window
        self.window = cmds.loadUI(#将.ui文件转换成maya可识别的控件
            uiFile=self.uiFile,
            verbose=verbose
        )
        cmds.showWindow(self.window)

    #创建头部     
    def createHeadBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('创建头部') 
    #创建腰部(一键)     
    def createWaistBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('创建腰部(一键)') 
        self.createBoneCurveBtnCmd()     
        self.createBoneBtnCmd()
        self.connectHeadBtnCmd()
        self.adjustAxisBtnCmd()
        self.createIKBtnCmd()
        self.rebuildSplineBtnCmd()
        self.createCtrlBtnCmd()
        self.adjustCtrlBtnCmd()
        self.ctrlBindSkinBtnCmd()
        self.setRotBtnCmd()
        self.getSplineLengthBtnCmd()
        self.connectJointBtnCmd() 
    #创建骨骼曲线     
    def createBoneCurveBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('创建骨骼曲线') 
    #创建骨骼
    def createBoneBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""
        print('创建骨骼')
        self.jnts  = []
        #n=jnt_num
        n=7
        y=13.5
        x=0
        z=0
        for i in range(n):
            jntname= 'trunk_joint'+chr(i+ord('1'))
            cmds.joint(p=(x,y,z),n=jntname,co=False,a=True)
            self.jnts.append(jntname)
            y+=1.4
            z-=0.2
        y+=1.4
        z+=2.0
        jntname= 'trunk_joint'+chr(7+ord('1'))
        cmds.joint(p=(x,y,z),n=jntname,co=False,a=True)
        cmds.setAttr(jntname+'.rotateAxis',90,0,0)
        cmds.setAttr('trunk_joint8.rotateAxis',90,0,0)
        jntname= 'trunk_joint'+chr(8+ord('1'))
        cmds.joint(p=(x,y,z+2),n=jntname,co=False,a=True)
        cmds.setAttr(jntname+'.rotateAxis',90,0,0)
        print(self.jnts)
    #连接头部     
    def connectHeadBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('连接头部')      
    #调整轴向
    def adjustAxisBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        # obtain input as a float
        print('调整轴向')
    #创建IK
    def createIKBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        # obtain input as a float
        print('创建IK')
        print(self.jnts)
        self.ik_names = cmds.ikHandle( sj= self.jnts[0], ee= self.jnts[-1],sol='ikSplineSolver',scv=False)
        print(self.ik_names)
    #重建spine      
    def rebuildSplineBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        # obtain input as a float
        print('重建spine') 
        cmds.rebuildCurve('curve1',s=2)
    #创建控制器   
    def createCtrlBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('创建控制器')  
        self.c_jnts = []
        self.c_jnt_grps = []
        for i in range(3):
            jntname = 'joint_'+chr(ord('A')+i)
            cmds.joint(p=(0,0,0),n=jntname,rad=1.5) 
            self.c_jnts.append(jntname)
            if i>0 :
                cmds.parent(self.c_jnts[i-1]+'|'+self.c_jnts[i],world=True) 
        for i in range(3):
            self.c_jnt_grps.append(self.c_jnts[i]+'_grp')
            cmds.group(self.c_jnts[i],name=self.c_jnt_grps[i])   
    #调整控制器位置 
    def adjustCtrlBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('调整控制器位置')              
        for i in range(3):
            print(self.jnts[i*3])
            #这个是局部坐标
            tr = cmds.getAttr(self.jnts[i*3]+'.translate')[0]#返回的是一个列表[(0.0, 13.50000000000002, 0.0)]                  
            w_tr = list(tr)
            for j in range(i*3):
                l_tr = list(cmds.getAttr(self.jnts[j]+'.translate')[0])#祖先节点的局部坐标       
                for k in range(3):                   
                    w_tr[k] += l_tr[k]                 
            print(w_tr)       
            cmds.move(w_tr[0],w_tr[1],w_tr[2],self.c_jnt_grps[i],wd=True)
    #给控制器蒙皮(ikspline)     
    def ctrlBindSkinBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('给控制器蒙皮(ikspline)')
        b_curve = cmds.ls('curve1')
        obj_ls= self.c_jnts+ b_curve
        print(obj_ls)
        cmds.select(obj_ls)
        cmds.SmoothBindSkin(tsb=True)   
    #设置旋转      
    def setRotBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('设置旋转')
        cmds.setAttr(self.ik_names[0]+'.dTwistControlEnable',1)
        cmds.setAttr(self.ik_names[0]+'.dWorldUpType',4)
        cmds.setAttr(self.ik_names[0]+'.dForwardAxis',2)
        cmds.setAttr(self.ik_names[0]+'.dWorldUpAxis',3)
        
        cmds.setAttr(self.ik_names[0]+'.dWorldUpVector',0,0,1)
        cmds.setAttr(self.ik_names[0]+'.dWorldUpVectorEnd',0,0,1)
        
        print(cmds.ls(self.ik_names[0]+'.dWorldUpMatrix'))
        #下面应该是属性连接   
        cmds.connectAttr(self.c_jnts[0]+'.worldMatrix',self.ik_names[0]+'.dWorldUpMatrix')
        cmds.connectAttr(self.c_jnts[2]+'.worldMatrix',self.ik_names[0]+'.dWorldUpMatrixEnd')                 
    #获取splineIK长度    
    def getSplineLengthBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('获取splineIK长度')
        self.curveinfo=cmds.arclen(self.ik_names[2],ch=True)
    #属性链接    
    def connectJointBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('属性链接')
        #创建乘除节点
        multiply_divide=cmds.createNode('multiplyDivide')
        cmds.setAttr(multiply_divide+'.operation',2)
        #cmds.setAttr(multiply_divide+'.input2X',self.curveinfo+'.arcLength')#出错
        cmds.setAttr(multiply_divide+'.input2X',cmds.arclen(self.ik_names[2]))
        #连接
        cmds.connectAttr(self.curveinfo+'.arcLength',multiply_divide+'.input1X')
        for i in range(7):
            cmds.connectAttr(multiply_divide+'.outputX',self.jnts[i]+'.scaleY')

    #帮助   
    def helpBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('帮助')
        win = HelpDialog(
            os.path.join(
                os.getenv('HOME'),
                'help.ui'
            )    
        )
        win.create(verbose=True)
    #关于     
    def aboutBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('关于')
        win = HelpDialog(
            os.path.join(
                os.getenv('HOME'),
                'about.ui'
            )    
        )
        win.create(verbose=True)
    #开始    
    def startBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('开始')
        #delete self.jnts
        #delete self.ik_names
        #delete self.c_jnts
        #delete self.c_jnt_grps
        
win = HumanBodyBindWindow(
    os.path.join(
        os.getenv('HOME'),
        'human_bone_bind2.0.ui'
    )    
)
win.create(verbose=True)
       