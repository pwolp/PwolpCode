#!/usr/bin/python
# 2019年9月10日 11:20:01
import os
import wx
import cv2
import glob
import time
import datetime
import numpy as np


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "图片批处理", size=(590, 550))
        self.rb = "无"
        self.size = "256,256"
        self.SNR = 1
        self.input_path = None
        self.output_path = None
        self.image_path = None
        self.InitUI()

    def InitUI(self):
        pikachu = '''\n
                 へ　　　　　／|
            　　/＼7　　　 ∠＿/
            　 /　│　　 ／　／
            　│　Z ＿,＜　／　　 /`ヽ
            　│　　　　　ヽ　　 /　　〉
            　 Y　　　　　`　 /　　/
            　ｲ●　､　●　　⊂⊃〈　　/
            　()　 へ　　　　|　＼〈
            　　>ｰ ､_　 ィ　 │ ／／
            　 / へ　　 /　ﾉ＜| ＼＼
            　 ヽ_ﾉ　　(_／　 │／／
            　　7　　　　　　　|／
            　　＞―r￣￣`ｰ―＿
            \n
                  '''
        self.FunPanel = wx.Panel(self)
        self.DisPanel = wx.Panel(self)
        self.LogPanel = wx.Panel(self)

        self.HBoxPanel = wx.BoxSizer(wx.HORIZONTAL)  # 设置整体布局
        self.HBoxPanel.Add(self.FunPanel, 0, flag=wx.ALL|wx.EXPAND, border=5)
        self.HBoxPanel.Add(self.DisPanel, 0, flag=wx.ALL|wx.EXPAND, border=5)
        self.HBoxPanel.Add(self.LogPanel, 0, flag=wx.ALL|wx.EXPAND, border=5)
        self.SetSizer(self.HBoxPanel)

        font1 = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        vbox = wx.BoxSizer(wx.VERTICAL) # 设置功能区
        menu = wx.StaticText(self.FunPanel, -1, label="菜单", style=wx.ALIGN_CENTER, )
        menu.SetFont(font=font1)
        vbox.Add(menu, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 20)

        bt_open = wx.Button(self.FunPanel, -1, label="输入图片", style=wx.ALIGN_LEFT)
        bt_open.Bind(wx.EVT_BUTTON, self.OnclickOpen)
        vbox.Add(bt_open, 0, wx.ALIGN_LEFT, 20)

        lbList = ["无", "设置大小", "高斯模糊", "椒盐噪声", "运动模糊", "马赛克", "加国旗"]
        rb_chose = wx.RadioBox(self.FunPanel, -1, label="选择功能",
                               style=wx.RA_SPECIFY_ROWS, choices=lbList, )
        rb_chose.Bind(wx.EVT_RADIOBOX, self.OnRadioBox)
        vbox.Add(rb_chose, 0, wx.ALIGN_LEFT, 20)

        imgsize = wx.StaticText(self.FunPanel, -1, label="设置图片高宽", style=wx.ALIGN_CENTER)
        imgsize.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        vbox.Add(imgsize, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        attHW = wx.TextCtrl(self.FunPanel, -1, "256,256", size=(80, 25))
        attHW.Bind(wx.EVT_TEXT, self.OnTextHW)
        vbox.Add(attHW, 0, wx.ALIGN_CENTER_HORIZONTAL, 30)

        attribute = wx.StaticText(self.FunPanel, -1, label="参数：\n"
                                                           "椒盐(0~1)\n"
                                                           "其他(>=1)", style=wx.ALIGN_CENTER)
        attribute.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL,wx.NORMAL))
        vbox.Add(attribute, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5)

        attSNR = wx.TextCtrl(self.FunPanel, -1, "1", size=(80, 25))
        attSNR.Bind(wx.EVT_TEXT, self.OnTextSNR)
        vbox.Add(attSNR, 0, wx.ALIGN_CENTER_HORIZONTAL, 30)

        bt_start = wx.Button(self.FunPanel, -1, label="预览", style=wx.ALIGN_LEFT)
        bt_start.Bind(wx.EVT_BUTTON, self.OnclickStart)
        vbox.Add(bt_start, 0, wx.ALIGN_LEFT, 20)

        bt_save = wx.Button(self.FunPanel, -1, label="保存", style=wx.ALIGN_LEFT)
        bt_save.Bind(wx.EVT_BUTTON, self.OnclickSave)
        vbox.Add(bt_save, 0, wx.ALIGN_LEFT, 20)

        bt_ok = wx.Button(self.FunPanel, -1, label="执行", style=wx.ALIGN_LEFT)
        bt_ok.Bind(wx.EVT_BUTTON, self.OnclickOK)
        vbox.Add(bt_ok, 0, wx.ALIGN_LEFT, 20)

        bt_close = wx.Button(self.FunPanel, -1, label="关闭", style=wx.ALIGN_LEFT)
        bt_close.SetBackgroundColour("#ff0000")
        bt_close.SetForegroundColour("#ffffff")
        bt_close.Bind(wx.EVT_BUTTON, self.OnclickClose)
        vbox.Add(bt_close, 0, wx.ALIGN_LEFT, 20)
        self.FunPanel.SetSizer(vbox)

        # dbox = wx.FlexGridSizer(2, 2, 10, 10)   # 设置显示区
        # original_title = wx.StaticText(self.DisPanel, label="原图", style=wx.ALIGN_CENTER)
        # change_title = wx.StaticText(self.DisPanel, label="修改后的图片", style=wx.ALIGN_CENTER)
        # image1 = wx.Image("./lena.jpg", wx.BITMAP_TYPE_JPEG)
        # self.original_image = wx.StaticBitmap(self.DisPanel, -1, image1.ConvertToBitmap())
        # image2 = wx.Image("./smiley.jpg", wx.BITMAP_TYPE_JPEG)
        # self.changed_image = wx.StaticBitmap(self.DisPanel, -1, image2.ConvertToBitmap())
        # dbox.AddMany([(original_title, 0, wx.ALIGN_CENTER), (change_title, 0, wx.ALIGN_CENTER),
        #               (self.original_image, 0, wx.ALIGN_CENTER),(self.changed_image, 0, wx.ALIGN_CENTER)])
        # dbox.AddGrowableRow(1)
        # dbox.AddGrowableCol(1)
        # self.DisPanel.SetSizer(dbox)

        dbox = wx.BoxSizer(wx.VERTICAL)     # 设置显示区域
        original_title = wx.StaticText(self.DisPanel, -1, label="原图", style=wx.ALIGN_CENTER_HORIZONTAL)
        original_title.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        dbox.Add(original_title, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 10)

        image1 = wx.Image("./lena.jpg", wx.BITMAP_TYPE_JPEG)
        self.original_image = wx.StaticBitmap(self.DisPanel, -1, image1.ConvertToBitmap())
        dbox.Add(self.original_image, 0, wx.ALIGN_CENTER_HORIZONTAL)

        change_title = wx.StaticText(self.DisPanel, -1, label="修改后的图片", style=wx.ALIGN_CENTER_HORIZONTAL)
        change_title.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        dbox.Add(change_title, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 10)

        image2 = wx.Image("./smiley.jpg", wx.BITMAP_TYPE_JPEG)
        self.changed_image = wx.StaticBitmap(self.DisPanel, -1, image2.ConvertToBitmap())
        dbox.Add(self.changed_image, 0, wx.ALIGN_CENTER_HORIZONTAL)
        self.DisPanel.SetSizer(dbox)


        lbox = wx.BoxSizer(wx.VERTICAL)   # 设置日志
        self.log = wx.TextCtrl(self.LogPanel, -1, pikachu, size=(250, 500),style=wx.TE_MULTILINE|wx.TE_READONLY)
        lbox.Add(self.log, 0, wx.ALL|wx.EXPAND|wx.ALIGN_LEFT)
        self.LogPanel.SetSizer(lbox)

        self.log.AppendText("\n*************************\n"
                            "2019年9月完成。\n"
                            "用于图片批处理。\n"
                            "*************************\n")
        self.log.AppendText(datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
        self.log.AppendText("\n\n下面显示处理日志：\n\n")

    def OnclickOpen(self, event):
        # wildcard = "Image File *.jpg|(*.png)"
        dlg = wx.DirDialog(self, "选择输入图片目录", os.getcwd(), style=wx.DD_DEFAULT_STYLE|wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            self.input_path = dlg.GetPath()
        dlg.Destroy()
        if self.input_path is None:
            self.log.AppendText("错误！没有选择输入目录！！\n")
            self.log.AppendText("请选择输入目录！\n\n")
        else:
            JPGimage = glob.glob(os.path.join(self.input_path, "*.jpg"))
            PNGimage = glob.glob(os.path.join(self.input_path, "*.png"))
            # cv2 读取图片透明度有问题，所以去掉BMP格式图片
            # BMPimage = glob.glob(os.path.join(self.input_path, "*.bmp"))
            # self.image_path = JPGimage + PNGimage + BMPimage
            self.image_path = JPGimage + PNGimage
            self.log.AppendText("选择文件目录：\n")
            self.log.AppendText(self.input_path + "\n")
            if len(self.image_path) == 0:
                self.log.AppendText("该目录下没有JPG或PNG格式图片！！\n")
                self.log.AppendText("请重新选择目录！\n")
            else:
                self.log.AppendText("该目录下一共有图片："+str(len(self.image_path))+"\n")
                self.log.AppendText("--->其中JPG图片："+str(len(JPGimage))+"\n")
                self.log.AppendText("--->其中PNG图片：" + str(len(PNGimage)) + "\n")
                # self.log.AppendText("--->其中BMP图片：" + str(len(BMPimage)) + "\n\n")

    def OnclickStart(self, event):
        self.log.AppendText("--**处理首张图片预览**--\n")
        if self.image_path is None:
            self.log.AppendText("错误！没有选择输入文件！！\n")
            self.log.AppendText("请先选择输入文件，然后浏览！\n")
        else:
            image_path = self.image_path
            image = cv2.imread(image_path[0], cv2.IMREAD_COLOR)
            H, W = image.shape[0], image.shape[1]
            image = cv2.resize(image, (200, 200))
            height = image.shape[0]
            width = image.shape[1]
            image = cv2.cvtColor(np.uint8(image), cv2.COLOR_BGR2RGB)
            pic = wx.Bitmap.FromBuffer(width, height, image)

            self.original_image.SetBitmap(pic)
            input_name = os.path.basename(image_path[0])

            if self.rb == "无":
                self.log.AppendText("->首张图片<-\n图片大小：(%d,%d)\n\n" % (H, W))
                self.changed_image.SetBitmap(pic)
            elif self.rb == "设置大小":
                try:
                    height = int(self.size.split(',')[0])
                    width = int(self.size.split(',')[1])
                    if height == 0 or width == 0:
                        self.log.AppendText("错误！输入大于0的数字！\n\n")
                    else:
                        # image = self.resize(image)
                        # self.changed_image.SetBitmap(wx.Bitmap.FromBuffer(width, height, image))
                        self.changed_image.SetBitmap(pic)
                        self.log.AppendText("->设置图片大小：(%d,%d)\n\n" % (height, width))
                except ValueError:
                    self.log.AppendText("错误！输入正确的格式：256,256\n\n")
            elif self.rb == "高斯模糊":
                try:
                    scale = int(float(self.SNR))
                    if scale < 1:
                        self.log.AppendText("错误！请输入大于0的数！\n\n")
                    else:
                        image = self.blur(image, scale)
                        self.log.AppendText("->添加高斯模糊\n->像素块为：%d\n\n" % (scale))
                        self.changed_image.SetBitmap(wx.Bitmap.FromBuffer(width, height, image))
                except ValueError:
                    self.log.AppendText("错误！请输入大于0的数！\n\n")
            elif self.rb == "椒盐噪声":
                try:
                    SNR = float(self.SNR)
                    if SNR > 1 or SNR <= 0:
                        self.log.AppendText("错误！请输入0-1之间的数！\n\n")
                    else:
                        image = self.salt_pepper(image, SNR)
                        self.log.AppendText("->添加椒盐噪声\n->信噪比为：%.2f\n\n" % (SNR))
                        self.changed_image.SetBitmap(wx.Bitmap.FromBuffer(width, height, image))
                except ValueError:
                    self.log.AppendText("错误！请输入0-1之间的数！\n\n")
            elif self.rb == "运动模糊":
                try:
                    degree = int(float(self.SNR))
                    if degree < 1:
                        self.log.AppendText("错误！请输入大于0的数！\n\n")
                    else:
                        image = self.motion(image, degree)
                        self.log.AppendText("->添加运动模糊\n->重叠像素为：%d\n\n" % (degree))
                        self.changed_image.SetBitmap(wx.Bitmap.FromBuffer(width, height, image))
                except ValueError:
                    self.log.AppendText("错误！请输入大于0的数！\n\n")
            elif self.rb == "马赛克":
                try:
                    pixel = int(float(self.SNR))
                    if pixel < 1:
                        self.log.AppendText("错误！请输入大于0的数！\n\n")
                    else:
                        image = self.masic(image, pixel)
                        self.log.AppendText("->添加马赛克\n->像素块为：%d\n\n" % (pixel))
                        self.changed_image.SetBitmap(wx.Bitmap.FromBuffer(width, height, image))
                except ValueError:
                    self.log.AppendText("错误！请输入大于0的数！\n\n")
            elif self.rb == "加国旗":
                image = self.AddFlag(image)
                self.log.AppendText("->添加国旗，显示为蓝色，保存为红色\n\n")
                self.changed_image.SetBitmap(wx.Bitmap.FromBuffer(width, height, image))

            # cv2.imwrite(os.path.join(self.output_path, input_name), image)

    def OnRadioBox(self, event):
        self.rb = event.GetString()

    def OnTextHW(self, event):
        self.size = event.GetString()

    def OnTextSNR(self, event):
        self.SNR = event.GetString()

    def OnclickSave(self, event):
        self.log.AppendText("--**处理图片输出**--\n")
        if self.image_path is None:
            self.log.AppendText("错误！没有选择输入文件！！\n")
            self.log.AppendText("请先选择输入文件！\n\n")
        else:
            dlg = wx.DirDialog(self, "选择输出图片目录", os.getcwd(), style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
            if dlg.ShowModal() == wx.ID_OK:
                self.output_path = dlg.GetPath()
            dlg.Destroy()
            if self.output_path is None:
                self.log.AppendText("错误！没有选择输出目录！！\n")
                self.log.AppendText("请选择输出目录！\n\n")
            else:
                self.log.AppendText("选择输出目录：" + self.output_path + "\n")

    def OnclickOK(self, event):
        if self.output_path == None:
            self.log.AppendText("没有选择输出目录！！\n请重新选择！！\n\n")
        else:
            self.log.AppendText("--**开始执行处理**--\n")
            self.log.AppendText("将文件保存在目录：" + self.output_path + "\n")
            image_path = self.image_path
            start = time.time()
            for i in range(len(image_path)):
                image = cv2.imread(image_path[i], cv2.IMREAD_COLOR)
                input_name = os.path.basename(image_path[i])
                if self.rb == "无":
                    self.log.AppendText("->图片未做任何处理\n复制图片：%d/%d\n" % (i+1, len(image_path)))
                elif self.rb == "设置大小":
                    try:
                        height = int(self.size.split(',')[0])
                        width = int(self.size.split(',')[1])
                        if height == 0 or width == 0:
                            self.log.AppendText("错误！输入大于0的数字！\n\n")
                            break
                        else:
                            image = self.resize(image, size=(height, width))
                            self.log.AppendText("->设置图片大小：%d/%d\n" % (i + 1, len(image_path)))
                    except ValueError:
                        self.log.AppendText("错误！输入正确的格式：256,256\n\n")
                        break
                elif self.rb == "高斯模糊":
                    try:
                        scale = int(float(self.SNR))
                        if scale < 1:
                            self.log.AppendText("错误！请输入大于0的数！\n\n")
                            break
                        else:
                            image = self.blur(image, scale)
                            self.log.AppendText("->添加高斯模糊：%d/%d\n" % (i + 1, len(image_path)))
                    except ValueError:
                        self.log.AppendText("错误！请输入大于0的数！\n\n")
                        break
                elif self.rb == "椒盐噪声":
                    try:
                        SNR = float(self.SNR)
                        if SNR > 1 or SNR <= 0:
                            self.log.AppendText("错误！请输入0-1之间的数！\n\n")
                            break
                        else:
                            image = self.salt_pepper(image, SNR)
                            self.log.AppendText("->添加椒盐噪声：%d/%d\n" % (i + 1, len(image_path)))
                    except ValueError:
                        self.log.AppendText("错误！请输入0-1之间的数！\n\n")
                        break
                elif self.rb == "运动模糊":
                    try:
                        degree = int(float(self.SNR))
                        if degree < 1:
                            self.log.AppendText("错误！请输入大于0的数！\n\n")
                            break
                        else:
                            image = self.motion(image, degree)
                            self.log.AppendText("->添加运动模糊：%d/%d\n" % (i + 1, len(image_path)))
                    except ValueError:
                        self.log.AppendText("错误！请输入大于0的数！\n\n")
                        break
                elif self.rb == "马赛克":
                    try:
                        pixel = int(float(self.SNR))
                        if pixel < 1:
                            self.log.AppendText("错误！请输入大于0的数！\n\n")
                            break
                        else:
                            image = self.masic(image, pixel)
                            self.log.AppendText("->添加马赛克：%d/%d\n" % (i + 1, len(image_path)))
                    except ValueError:
                        self.log.AppendText("错误！请输入大于0的数！\n\n")
                        break
                elif self.rb == "加国旗":
                    image = self.AddFlag(image)
                    self.log.AppendText("->添加国旗：%d/%d\n" % (i+1, len(image_path)))
                cv2.imwrite(os.path.join(self.output_path, input_name), image)
            end = time.time()
            self.log.AppendText("**->处理完成<-**\n->共花费时间：%.2fs\n\n" % (end - start))

    def OnclickClose(self, event):
        massage = wx.MessageBox("确认退出？", "请确认", wx.CANCEL | wx.OK | wx.ICON_QUESTION)
        if massage == wx.OK:
            self.Destroy()

    def AddFlag(self, image):
        img_flag = cv2.imread('./map2.png', cv2.IMREAD_UNCHANGED)
        # b, g, r, a = img_flag[:, :, 0], img_flag[:, :, 1], img_flag[:, :, 2], img_flag[:, :, 3]
        # img_flag[:, :, 0] = r
        # img_flag[:, :, 1] = g
        # img_flag[:, :, 2] = b

        # 获取头像和国旗图案宽度
        w_head, h_head = image.shape[:2]
        w_flag, h_flag = img_flag.shape[:2]
        # 计算图案缩放比例
        scale = w_head / w_flag / 2
        # 缩放图案
        img_flag = cv2.resize(img_flag, (0, 0), fx=scale, fy=scale)
        # 获取缩放后新宽度
        w_flag, h_flag = img_flag.shape[:2]
        # 透明度
        alpha_h = img_flag[:, :, 3] / 255
        alpha = 1 - alpha_h
        # 按3个通道合并图片
        for c in range(0, 3):
            image[0:w_head - w_flag, h_head - h_flag:, c] = \
                (alpha_h * img_flag[:, :, c] + alpha * image[0:w_head - w_flag, h_head - h_flag:, c])

        return image
    # def resize(self, image, hw):
    #     if hw == '':
    #         hw = '256,256'
    #     if ',' not in hw:
    #         self.log.AppendText("错误！请输入正确的大小格式！\n")
    #     else:
    #         h = hw.split(',')[0]
    #         w = hw.split(',')[1]
    #         if h == '' or w == '':
    #             self.log.AppendText("错误！高度或宽度为空！\n")
    #         elif not str.isdigit(h) or not str.isdigit(w):
    #             self.log.AppendText("错误！请输入正确的整数大小！\n")
    #         else:
    #             return cv2.resize(image, (int(h), int(w))), int(h), int(w)
    def resize(self, image, size=(256, 256)):
        return cv2.resize(image, size)

    def blur(self, image, scale=4):
        return cv2.blur(image, (scale, scale), 0)

    def salt_pepper(self, image, snr=0.9):
        dst = image.copy().transpose(2, 1, 0)
        channel, height, width = dst.shape
        mask = np.random.choice((0, 1, 2), size=(1, height, width), p=[snr, (1 - snr) / 2., (1 - snr) / 2.])
        mask = np.repeat(mask, channel, axis=0)
        dst[mask == 1] = 255
        dst[mask == 2] = 0
        dst = dst.transpose(2, 1, 0)
        return dst

    def motion(self, image, degree=7, angle=0):
        M = cv2.getRotationMatrix2D((degree / 2, degree / 2), angle, 1)
        motion_blur_kernel = np.diag(np.ones(degree))
        motion_blur_kernel = cv2.warpAffine(motion_blur_kernel, M, (degree, degree))
        motion_blur_kernel = motion_blur_kernel / degree
        dst = cv2.filter2D(image, -1, motion_blur_kernel)
        return dst

    def masic(self, image, pixel=4):
        height, width = image.shape[:2]
        for y in range(0, height, pixel):  # y轴
            for x in range(0, width, pixel):  # x轴
                # 通过中间值的RGB，对所选范围块的RGB进行重新赋值，设置的单位像素块(Pixel数值)越小， 生成的像素图越精确
                ky = y + pixel
                ky1 = y + (pixel // 2)
                kx = x + pixel
                kx1 = x + (pixel // 2)
                if ky >= height:
                    ky = height - 1
                if kx >= width:
                    kx = width - 1
                if ky1 >= height:
                    ky1 = y
                if kx1 >= width:
                    kx1 = x
                image[y:ky, x:kx] = image[ky1][kx1]
        return image



if __name__ == '__main__':
    app = wx.App()                      # 初始化
    frame = MyFrame(parent=None, id=-1)  # 实例MyFrame类，并传递参数
    frame.Show()                        # 显示窗口
    app.MainLoop()                      # 调用主循环方法

