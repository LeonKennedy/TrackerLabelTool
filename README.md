# TrackerLabelTool
tennes game tracker label tool

# 步骤
1. 将视频切割成多帧图片
```shell
python split_video.py
```

2. 启动标注软件
```shell
bash label.sh <images>
```


# 标注
1. 从视频网站上下载视频https://replayervar/com/admin/index.html   
    账号 (admin, 12345678)
    主意需要下载成对视频，并且主意修改视频名字
   下载到指定位置<videos>
2. 通过脚本讲视频拆分成图片
3. 通过脚本启动标注工具
