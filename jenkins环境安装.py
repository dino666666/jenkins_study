'''
0.安装Java
    -sudo apt install openjdk-11-jdk

1.导入密钥： 使用wget导入jenkins存储库密钥GPG
    -wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -

2.添加存储库： 将jenkins存储库添加到系统中
    -sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

3.安装
    -sudo apt update
    -sudo apt install jenkins

4.检查Jenkins运行状态
    -sudo systemctl status jenkins

5.Jenkins配置
    - [可选]开放端口： sudo ufw allow 8080
    - [可选]修改端口： vi /etc/default/jenkins  修改HTTP_PORT
    -[可选]修改jenkins工作目录：
        -修改：vi /var/lib/jenkins/config.xml  修改workspaceDir
        -工作目录：ls -l /var/lib/jenkins/workspace/
    -[可选]JENKINS_HOME在哪里：/var/lib/jenkins
    -[可选]jenkins日志文件： cat /var/log/jenkins/
    -[可选]jenkins配置文件：/etc/default/jenkins


问题一：sudo apt update时报 “由于没有公钥，无法验证下列签名： NO_PUBKEY 5BA31D57EF5975CA” 错误
解决：sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 5BA31D57EF5975CA（密钥需要按照问题的提示更换一样的）

问题二：sudo apt install jenkins报“Sub-process /usr/bin/dpkg returned an error code (1)”错误
解决：
    cd /var/lib/dpkg/
    sudo mv info/ info_bak          # 现将info文件夹更名
    sudo mkdir info                 # 再新建一个新的info文件夹
    sudo apt-get update             # 更新
    sudo apt-get -f install         # 修复
    sudo mv info/* info_bak/        # 执行完上一步操作后会在新的info文件夹下生成一些文件，现将这些文件全部移到info_bak文件夹下
    sudo rm -rf info                # 把自己新建的info文件夹删掉
    sudo mv info_bak info           # 把以前的info文件夹重新改回名

问题三：sudo systemctl start jenkins.service 提示启动失败
解决：
    -vi /etc/default/jenkins  ,修改以下配置
        JENKINS_USER=root
        JENKINS_GROUP=root
    -修改权限
        chown -R jenkins:jenkins /var/lib/jenkins
        chown -R jenkins:jenkins /var/cache/jenkins
        chown -R jenkins:jenkins /var/log/jenkins
        sudo systemctl start jenkins.service
'''