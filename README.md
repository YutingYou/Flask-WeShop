## 项目说明：
基于Python Flask、wechatpy开发的简单商城项目。

已实现功能：
- [x] 快速购买界面
- [x] 微信支付

 
待实现功能：
- [ ] 订单管理
- [ ] 订单推送通知
- [ ] 购物车
- [ ] 活动运营
- [ ] 其他...

## 界面截图

## 远程开发配置
以阿里云服务器为例，开发工具使用PyCharm

1. 在服务器端安装python3环境，记下python解释器地址，建议使用virtualenv。
2. 配置PyCharm SFTP
 - 配置菜单路径：Tools -> Deployment -> Configuration
 - 点击添加按钮，类型选择`SFTP`，分别按下图配置`connection`、`mappings`选项卡
![connection标签卡.png](http://upload-images.jianshu.io/upload_images/3156309-fbbc9467e8057042.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![mapping选项卡.png](http://upload-images.jianshu.io/upload_images/3156309-c4b08538aaf37675.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
3. 配置远程解释器
 - Settings -> Project: xxxxx -> project interpreter -> 小齿轮图标 -> add remote，解释器路径自己改为virtualenv中，下图只是示例。
![interpreter.png](http://upload-images.jianshu.io/upload_images/3156309-6bcb5ed009dacda7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

4. 配置每次修改源码自动上传源码到服务器，Tools -> Deployment -> option，`upload changed files automatically to the default server`
![sftp_option.png](http://upload-images.jianshu.io/upload_images/3156309-b2d9b60a36a523bc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

5. 运行调试配置
![运行调试配置.png](http://upload-images.jianshu.io/upload_images/3156309-5b1ba27432794ff0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

