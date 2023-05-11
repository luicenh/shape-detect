#基于的基础镜像
FROM python:3.8.2
#代码添加到code文件夹
ADD . /app
# 设置code文件夹是工作目录
WORKDIR /app
# 安装支持
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip uninstall -y opencv-python
RUN pip install opencv-python-headless -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD ["python", "/app/main.py"]

EXPOSE 7001