import maya.cmds as cmds
import os
#help������
class HelpDialog(object):
    """A class for a window to create a cone pointing in a direciton"""
    ## reference to the most recent instance
    use = None#�����ԣ���ʱ�洢��������__init__()����ʱ��������ʵ��
    @classmethod
    def showUI(cls, uiFile):
        """A function to instantiate the window"""
        win = cls(uiFile)
        win.create()
        return win
    def __init__(self, filePath):#filePathָ��.ui�ļ��ڴ����ϵ�λ��
        """Initialize data attributes"""
        ## allow controls to initialize using class attribute
        HelpDialog.use = self#�����ԣ���ʱ�洢��������__init__()����ʱ��������ʵ��
        ## unique window handle
        self.window = 'help_dialog'#ʵ�����ԣ�
        ## the path to the .ui file
        self.uiFile = filePath
    def create(self, verbose=False):#verbose=Trueʱ�����GUI�п��õ�С�������Ϣ
        self.window = cmds.loadUI(#��.ui�ļ�ת����maya��ʶ��Ŀؼ�
            uiFile=self.uiFile,
            verbose=verbose
        )
        cmds.showWindow(self.window)

#���ڴ���
class AboutDialog(object):
    """A class for a window to create a cone pointing in a direciton"""
    ## reference to the most recent instance
    use = None#�����ԣ���ʱ�洢��������__init__()����ʱ��������ʵ��
    @classmethod
    def showUI(cls, uiFile):
        """A function to instantiate the window"""
        win = cls(uiFile)
        win.create()
        return win
    def __init__(self, filePath):#filePathָ��.ui�ļ��ڴ����ϵ�λ��
        """Initialize data attributes"""
        ## allow controls to initialize using class attribute
        AboutDialog.use = self#�����ԣ���ʱ�洢��������__init__()����ʱ��������ʵ��
        ## unique window handle
        self.window = 'about_dialog'#ʵ�����ԣ�
        ## the path to the .ui file
        self.uiFile = filePath
    def create(self, verbose=False):#verbose=Trueʱ�����GUI�п��õ�С�������Ϣ
        self.window = cmds.loadUI(#��.ui�ļ�ת����maya��ʶ��Ŀؼ�
            uiFile=self.uiFile,
            verbose=verbose
        )
        cmds.showWindow(self.window)
           
#��������        
class HumanBodyBindWindow(object):
    """A class for a window to create a cone pointing in a direciton"""
    ## reference to the most recent instance
    use = None#�����ԣ���ʱ�洢��������__init__()����ʱ��������ʵ��
    @classmethod
    def showUI(cls, uiFile):
        """A function to instantiate the window"""
        win = cls(uiFile)
        win.create()
        return win
    def __init__(self, filePath):#filePathָ��.ui�ļ��ڴ����ϵ�λ��
        """Initialize data attributes"""
        ## allow controls to initialize using class attribute
        HumanBodyBindWindow.use = self#�����ԣ���ʱ�洢��������__init__()����ʱ��������ʵ��
        ## unique window handle
        self.window = 'human_bone_bind_window'#ʵ�����ԣ�
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
    def create(self, verbose=False):#verbose=Trueʱ�����GUI�п��õ�С�������Ϣ
        """Draw the window"""
        # delete the window if its handle exists
        #if cmds.window(self.window, exists=True):
         #   cmds.deleteUI(self.window)
         #���������п��Բ�Ҫ����ͬ��windows���������ڳ�ͻ��loadUI����Զ�
         #�����������Ĵ��ڵ����ƣ���ǳ�������transform�ڵ������
        # initialize the window
        self.window = cmds.loadUI(#��.ui�ļ�ת����maya��ʶ��Ŀؼ�
            uiFile=self.uiFile,
            verbose=verbose
        )
        cmds.showWindow(self.window)

    #����ͷ��     
    def createHeadBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('����ͷ��') 
    #��������(һ��)     
    def createWaistBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('��������(һ��)') 
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
    #������������     
    def createBoneCurveBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('������������') 
    #��������
    def createBoneBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""
        print('��������')
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
    #����ͷ��     
    def connectHeadBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('����ͷ��')      
    #��������
    def adjustAxisBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        # obtain input as a float
        print('��������')
    #����IK
    def createIKBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        # obtain input as a float
        print('����IK')
        print(self.jnts)
        self.ik_names = cmds.ikHandle( sj= self.jnts[0], ee= self.jnts[-1],sol='ikSplineSolver',scv=False)
        print(self.ik_names)
    #�ؽ�spine      
    def rebuildSplineBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        # obtain input as a float
        print('�ؽ�spine') 
        cmds.rebuildCurve('curve1',s=2)
    #����������   
    def createCtrlBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('����������')  
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
    #����������λ�� 
    def adjustCtrlBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('����������λ��')              
        for i in range(3):
            print(self.jnts[i*3])
            #����Ǿֲ�����
            tr = cmds.getAttr(self.jnts[i*3]+'.translate')[0]#���ص���һ���б�[(0.0, 13.50000000000002, 0.0)]                  
            w_tr = list(tr)
            for j in range(i*3):
                l_tr = list(cmds.getAttr(self.jnts[j]+'.translate')[0])#���Ƚڵ�ľֲ�����       
                for k in range(3):                   
                    w_tr[k] += l_tr[k]                 
            print(w_tr)       
            cmds.move(w_tr[0],w_tr[1],w_tr[2],self.c_jnt_grps[i],wd=True)
    #����������Ƥ(ikspline)     
    def ctrlBindSkinBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('����������Ƥ(ikspline)')
        b_curve = cmds.ls('curve1')
        obj_ls= self.c_jnts+ b_curve
        print(obj_ls)
        cmds.select(obj_ls)
        cmds.SmoothBindSkin(tsb=True)   
    #������ת      
    def setRotBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('������ת')
        cmds.setAttr(self.ik_names[0]+'.dTwistControlEnable',1)
        cmds.setAttr(self.ik_names[0]+'.dWorldUpType',4)
        cmds.setAttr(self.ik_names[0]+'.dForwardAxis',2)
        cmds.setAttr(self.ik_names[0]+'.dWorldUpAxis',3)
        
        cmds.setAttr(self.ik_names[0]+'.dWorldUpVector',0,0,1)
        cmds.setAttr(self.ik_names[0]+'.dWorldUpVectorEnd',0,0,1)
        
        print(cmds.ls(self.ik_names[0]+'.dWorldUpMatrix'))
        #����Ӧ������������   
        cmds.connectAttr(self.c_jnts[0]+'.worldMatrix',self.ik_names[0]+'.dWorldUpMatrix')
        cmds.connectAttr(self.c_jnts[2]+'.worldMatrix',self.ik_names[0]+'.dWorldUpMatrixEnd')                 
    #��ȡsplineIK����    
    def getSplineLengthBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('��ȡsplineIK����')
        self.curveinfo=cmds.arclen(self.ik_names[2],ch=True)
    #��������    
    def connectJointBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('��������')
        #�����˳��ڵ�
        multiply_divide=cmds.createNode('multiplyDivide')
        cmds.setAttr(multiply_divide+'.operation',2)
        #cmds.setAttr(multiply_divide+'.input2X',self.curveinfo+'.arcLength')#����
        cmds.setAttr(multiply_divide+'.input2X',cmds.arclen(self.ik_names[2]))
        #����
        cmds.connectAttr(self.curveinfo+'.arcLength',multiply_divide+'.input1X')
        for i in range(7):
            cmds.connectAttr(multiply_divide+'.outputX',self.jnts[i]+'.scaleY')

    #����   
    def helpBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('����')
        win = HelpDialog(
            os.path.join(
                os.getenv('HOME'),
                'help.ui'
            )    
        )
        win.create(verbose=True)
    #����     
    def aboutBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('����')
        win = HelpDialog(
            os.path.join(
                os.getenv('HOME'),
                'about.ui'
            )    
        )
        win.create(verbose=True)
    #��ʼ    
    def startBtnCmd(self, *args):
        """Function to execute when Create button is pressed"""       
        print('��ʼ')
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
       