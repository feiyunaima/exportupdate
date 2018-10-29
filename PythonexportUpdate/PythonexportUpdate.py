import os,shutil
import configparser

def getconfig():
    cur_path=os.path.dirname(os.path.realpath(__file__))
    config_path=os.path.join(cur_path,'config.ini')
    conf=configparser.ConfigParser()
    conf.read(config_path)
    return conf

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
def main():
    try:
        config = getconfig()
    except BaseException as e:
        print(e)
        print("read config.ini failed")
        return
    try:
        s = config.get('path', 's_dir')
        c = config.get('path', 'c_dir')
        t = config.get('path', 't_dir')
        WebRoot = config.get('path', 'WebRoot')
        copycompile(s+"/"+WebRoot,c,t)
        copycompile(s+"/src",c+"/WEB-INF/classes",t+"/WEB-INF/classes")
        print("execute success")
    except BaseException as e:
        print(e)
        return   
    
if __name__ =='__main__':
    try:
        main()
    finally:
        input()
