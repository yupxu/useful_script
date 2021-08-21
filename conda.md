1. 查看安装了哪些包  
conda list


2. 检查更新当前conda  
conda update conda

3. Python创建虚拟环境  
conda create -n your_env_name python=x.x

4. 激活/退出虚拟环境  
source activate ENV_NAME 激活虚拟环境  
source deactivate 退出虚拟环境

5. 查看当前存在哪些虚拟环境  
conda env list   
conda info -e



### 更改 conda 镜像
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --set show_channel_urls yes
```

