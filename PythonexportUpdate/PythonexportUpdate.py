#从s中搜寻需要的源文件。将其编译文件从c里面复制到t里面
s = "C:/Users/Administrator/Desktop/update/代码/csrcHonesty" #源代码
c = "D:/tomcat/tomcat7_csrcHonesty/webapps/csrcHonesty" #源编译文件
t = "C:/Users/Administrator/Desktop/update/编译文件/csrcHonesty" #目标编译文件

import os,shutil
def findfiles(file_dir):
    list = []
    for root,dirs,files in os.walk(file_dir):
        if len(files)>0:
            for filename in files:
                list.append(root+"/"+filename)
    return list

def copycompile(s,c,t):
    list1 = findfiles(s)
    for sf in list1:
        tf = sf.replace(s,t)
        cf = sf.replace(s,c)
        if sf.endswith(".java"):
            cf = cf.replace(".java",".class")
            tf = tf.replace(".java",".class")            
        tpath,tname = os.path.split(tf)
        if not os.path.exists(tpath):
            os.makedirs(tpath)
        shutil.copyfile(cf,tf)
        print(" copy "+cf+" to "+tf)

if __name__ =='__main__':
    copycompile(s+"/WebRoot",c,t)
    copycompile(s+"/src",c+"/WEB-INF/classes",t+"/WEB-INF/classes")
    print("execute success")