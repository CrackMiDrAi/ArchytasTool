import os
import sys

def adv():
    global choiceadv
    choiceadv = input("A.安装自定义应用为系统应用（priv-app）\nB.安装自定义应用为系统应用（app）\nC.卸载系统应用（priv-app）\nD.卸载系统应用（app）\nE.推送指定文件到 /sdcard（内部储存根目录）\n0.返回主页\n------------------------\n请输入序号（不区分大小写，可多选）：")
    choiceadv = choiceadv.lower()
        
    if "a" in choiceadv:
        print("\n安装自定义应用为系统应用（priv-app）")
        apkpath = input("请拖入需要安装的 apk：")
        os.system("adb push " + apkpath + "/system/priv-app")

    if "b" in choiceadv:
        print("\n安装自定义应用为系统应用（app）")
        apkpath = input("请拖入需要安装的 apk：")
        os.system("adb push " + apkpath + "/system/app")

    if "c" in choiceadv:
        print("\n卸载系统应用（priv-app）")
        os.system("adb shell")
        os.system("cd /system/priv-app")
        os.system("ls")
        apkpath = input("请输入需要删除的文件/文件夹名：")
        os.system("rm -r " + apkpath)
        os.system("exit")

    if "d" in choiceadv:
        print("\n卸载系统应用（app）")
        os.system("adb shell")
        os.system("cd /system/app")
        os.system("ls")
        apkpath = input("请输入需要删除的文件/文件夹名：")
        os.system("rm -r " + apkpath)
        os.system("exit")

    if "e" in choiceadv:
        print("\n推送指定文件到 /sdcard")
        filepath = input("请输入需要推送文件的路径（可拖动）并回车：")
        os.system("adb push " + filepath + " /sdcard")

    print ("------------------------")

def doAgain(mode):
    doAgainChoice = input("执行完成，您是否需要再次执行？（y/n）：")
    doAgainChoice = doAgainChoice.lower()
    if doAgainChoice == "y":
        print ("------------------------")
        if mode == 0:
            adv()
        else:
            main()
    elif doAgainChoice == "n":
        main()
    else:
        print("输入错误！")
        doAgain(mode)

def Store():
    print("正在替换应用商店..")
    os.system("adb push files/MiStore.apk /system/priv-app/MiStore")
    print("完成\n")

def delUpdator():
    print("正在删除更新程序...")
    os.system("adb shell rm -r /system/priv-app/MiSysUpdator")
    print("完成\n")

def pushUpdator():
    print("正在推送更新程序...")
    os.system("adb push files/MiSysUpdator.apk /system/priv-app")
    print("完成\n")

def installPackage():
    print("正在安装原生软件包安装程序...")
    os.system("adb push files/MiPackageInstaller.apk /system/priv-app/MiPackageInstaller")
    print("完成\n")

def installSetting():
    print("正在安装旧版设置...")
    os.system("adb push files/MiSettings.apk /system/priv-app/MiSettings")
    print("完成\n")

def lowRam():
    print("正在替换 build.prop...")
    os.system("adb push files/build.prop /system")
    print("完成\n")
    
def delLauncher():
    print("正在卸载默认桌面...")
    os.system("adb shell rm -r /system/priv-app/MiLauncher")
    print("完成\n")

def installLauncher():
    print("正在安装默认桌面...")
    os.system("adb push files/MiLauncher.apk /system/priv-app")
    print("完成\n")

def installVia():
    print("正在安装 Via 浏览器...")
    os.system("adb push files/via.apk /system/priv-app")
    print("完成\n")

def enableWallpaper():
    print("正在启用壁纸服务...")
    os.system("adb push files/framework-res.apk /system/framework")
    os.system("adb shell chmod 644 /system/framework/framework-res.apk")
    print("完成\n")

def flashMagisk():
    input ("请进入 高级 -> Adb Sideload -> 滑动滑块，完成后回车...")
    print("正在刷入...")
    os.system("adb sideload files/Magisk-Canary-23016.zip")
    print("完成\n")

print ("Tool by @rpone\n------------------------")

if not os.path.exists("adb.exe"):
    print("请解压后运行！\n------------------------")
    os.system("pause")
    sys.exit()

print ("请在关机后按住 电源键+复读键+红键+音量上键 以进入 TWRP Recovery 并挂载 System 分区")
print ("检查连接状态...\n------------------------\n")
f = os.popen(r"adb devices", "r")
output = f.read()
f.close()
s = output.split("\n")
new = [x for x in s if x != ''] 
devices = []
for i in new:
    dev = i.split('\tdevice')
    if len(dev)>=2:
        devices.append(dev[0])
if not devices:
    print("设备未连接！\n\n------------------------")
    os.system("pause")
    sys.exit()
else:
    print("当前连接设备:%s"%str(devices)+"\n")
print ("------------------------")

def main():
    choice = input("A.替换应用商店（可防止第三方 app 被删除，由 @xluzo 修改）\nB.关闭系统更新\nC.启用系统更新\nD.安装原生软件包安装程序（可直接安装第三方 app）\nE.安装旧版设置（支持开发者选项）\nF.关闭 lowram 模式（可获取通知使用权、修改堆叠后台）\nG.卸载默认桌面（请确定已安装可使用的第三方桌面）\nH.恢复默认桌面并启用负一屏\nI.安装 Via 浏览器\nJ.启用壁纸服务（不稳定且有变砖风险，可使用第三方启动器）\nK.刷入 Magisk\n0.一键执行首次破解的推荐操作\n1.高级选项\n2.退出程序\n------------------------\n请输入序号（不区分大小写，可多选）：")
    choice = choice.lower()
    print ("------------------------")

    if "2" in choice:
        return 0
    if "1" in choice:
        print ("高级选项（不建议小白使用，变砖不负责）")
        adv()
        if "0" not in choiceadv:
            doAgain(0)
    if "0" in choice:
        choice = "adefik"
        print("正在执行推荐操作...\n")
    if "a" in choice:
        Store()
    if "b" in choice:
        delUpdator()
    if "c" in choice:
        pushUpdator()
    if "d" in choice:
        installPackage()
    if "e" in choice:
        installSetting()
    if "f" in choice:
        lowRam()
    if "g" in choice:
        delLauncher()
    if "h" in choice:
        installLauncher()
    if "i" in choice:
        installVia()
    if "j" in choice:
        enableWallpaper()
    if "k" in choice:
        flashMagisk()
    print ("------------------------")
    if "0" in choiceadv:
        main()
    else:
        doAgain(1)

main()
