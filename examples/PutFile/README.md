### 1. 使用python3虚拟环境
> 	  source build/bin/py3_venv/bin/activate
> 	  (py3_venv) [root@5f9c57269bd3 gateway]#
    
在该环境下安装oss2服务

### 2. 安装oss2服务

通过pip安装，执行命令如下：

>	pip install oss2

验证安装状况
在命令行输入python并回车，进入Python环境。
执行以下命令检查SDK版本：
>     >>>import oss2
>     >>>oss2.__version__
>     >>>'2.0.0'

上面的输出表明您已经成功安装了Python SDK 2.0.0

### 3. 创建函数

参考oss2相关SDK API或者index.py，index.py是利用oss API上传一个文件
[https://help.aliyun.com/document_detail/52834.html](https://help.aliyun.com/document_detail/52834.html)
