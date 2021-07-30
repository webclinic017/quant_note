Linux作为一个开源的操作系统，目前在很多行业有着广泛的应用。本篇主要介绍Linux的常见命令，读完后可以直接快速上手，大大提高开发速度和效率，本文保持长期更新。
Windows下Windows Terminal也能够使用大部分shell命令，所以对于提升代码效率来说很有帮助。

这里以ubuntu系统为例，总结一些常用软件和命令。ubuntu系统可以通过虚拟机、双系统、云服务器等途径获取，这里比较推荐虚拟机安装官方镜像，等熟悉系统后再尝试（折腾）。虚拟机软件可以使用VMware，[ubuntu镜像下载](https://cn.ubuntu.com/download/desktop)，安装好镜像后，启动系统。
在ubuntu系统下使用快捷键Ctrl+Alt+T即可唤出终端。

![1](pic\1.png)



#### 日常使用
**使用小技巧**：涉及到已经存在的文件信息时，可以使用Tab键进行补全。比如在输入下面Desktop时，只需要输入前几个字母，在shell中输入cd De，再按Tab键即可完成自动补全。(**多敲Tab键**）

##### 创建/删除文件/文件夹等文件操作
~~~shell
cd Desktop	#进入Desktop目录
ls	#显示当前目录下的文件
ls -l #显示当前目录下所有文件的详细属性
touch test	#创建一个名为test的空文件
rm test	#删除刚刚创建的test文件
mkdir test	#创建一个名为test的文件夹
rm -rf test	#删除刚刚创建的test文件夹及内部所有文件,-rf是添加的参数，r表示递归删除文件夹，f表示需要删除的为文件夹(folder缩写)
~~~
以上展示了最为常用的一些命令，其中cd、ls、touch、rm均为脚本命令。如果对于这些命令有使用上的困惑，可以在shell中直接输入命令 --help，如下所示
~~~shell
cd --help
~~~
![2](pic\2.png)

##### 更改文件权限
~~~shell
chmod 777 test	#test可以是文件或者是文件夹，但是只会修改test一个文件或文件夹
chmod -R 777 test	#test为文件夹时会修改所有文件夹下的文件权限
~~~
这里7代表具有读、写、可执行三种权限，在使用ls -l命令查看文件详细信息时，可以得到如下结果：
~~~shell
-rwxrwxrwx 1 root root 0 Jul 28 20:38 test1
-rw-r--r-- 1 root root 0 Jul 28 20:38 test2
-rw-r--r-- 1 root root 0 Jul 28 20:38 test3
~~~
这里三个重复的rwx分别代表了文件拥有者，文件所属组，其他用户拥有的权限，采用二进制表示4+2+1即为7。
##### 文件移动
~~~shell
mv test1 test2 #将当前目录下test1文件（夹）移动至test2文件（夹）
cp test1 test2 #将当前目录下test1文件复制到test2文件
cp -r test_dir new_dir #将当前目录下的test_dir文件夹复制到new_dir文件夹
~~~

##### 文件查找
用于查找的命令主要有find和grep。find是文件级别的查找，比如要在当前目录下查找文件名中含有csv的文件，就需要使用find；而grep是对于文件内容的查找，比如需要查找某个文件中包含指定字符串的行。
~~~shell
find . -name "*.csv"	#在当前目录下(.表示当前目录)查找所有文件名中符合"*.csv"的文件并输出
~~~

~~~shell
grep test 1.csv	#在当前目录下的1.csv文件中查找包含“test”的行并输出
grep -r test .	#在当前目录下(.表示当前目录)查找所有包含“test”的文件并输出
~~~
#### 磁盘管理
