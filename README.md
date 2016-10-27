# crosswall
:heart: 翻墙小工具，适合学术粉使用

更多细节，可以参考下面的文章链接 http://blog.csdn.net/marksinoberg/article/details/52934770

---

![Google](https://camo.githubusercontent.com/6f787bdcb60b630c8cb9dd463ffe73b3bcacba70/68747470733a2f2f7777772e676f6f676c652e636f6d2f6c6f676f732f646f6f646c65732f323031362f676f6f676c65732d313874682d62697274686461792d353636313533353637393534353334342d687032782e676966)


先说说这个小工具的原理吧，就是替换hosts文件。然后其依赖于GitHub上一个维护小组（https://github.com/racaljk/hosts）的hosts更新文件。

然后这个工具在每次运行的时候，都会自动的下载最新的hosts文件，并在备份当前的hosts文件为hosts_bak后自动的完成替换工作。

由于是系统盘内的文件操作，所以需要有复制和替换的权限，请右键以管理员的权限运行。祝您使用愉快:-)

![示意](http://img.blog.csdn.net/20161026151543539)


