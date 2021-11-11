# Overview

overview


# Install Guide

### 安装顺序

#### 1. 基础库依赖

**按表格从上到下顺序**安装：进入对应目录：

```bash
rez-build --install
```



|   库    |  版本  |                            结果                            |
| :-----: | :----: | :--------------------------------------------------------: |
| openssl | 1.1.1  | <img src="https://github.com/Kazen-Renderer/rez-packages/blob/main/doc/img/openssl.png" style="zoom:50%;" /> |
|  cmake  | 3.20.4 |  <img src="https://github.com/Kazen-Renderer/rez-packages/blob/main/doc/img/cmake.png" style="zoom:50%;" />  |
|  zlib   | 1.2.11 |  <img src="https://github.com/Kazen-Renderer/rez-packages/blob/main/doc/img/zlib.png" style="zoom:50%;" />   |
| python  | 2.7.18 |  <img src="https://github.com/Kazen-Renderer/rez-packages/blob/main/doc/img/py_27.png" style="zoom:50%;" />  |
|         | 3.7.10 |  <img src="https://github.com/Kazen-Renderer/rez-packages/blob/main/doc/img/py_37.png" style="zoom:50%;" />  |



#### 2. 其它库

其它库找到packages中的`build_requires`，依次编译即可
