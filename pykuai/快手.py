import json
import random
import time

import uiautomator2 as u2

d = u2.connect("VBJDU18813002392")
d.app_start("com.kuaishou.nebula", stop=True)

time.sleep(1)
# 先进入到我的页面
print("成功进入了界面")

#com.kuaishou.nebula:id/open_long_atlas
def sleeps(param):
    time.sleep(param)


i = 0
while True:
    d.swipe(0.45, 0.82, 0.512, 0.154)
    rantime = random.randint(6, 20)
    print("打印时间%s" % rantime)
    i = i + 1

    # 点赞
    if rantime == 6 or rantime == 11 or rantime == 18:
        print('点赞')
        sleeps(2)
        d(resourceId="com.kuaishou.nebula:id/like_button").click_exists(2)
    time.sleep(rantime)
    # 添加评论
    if rantime == 8 or rantime == 12 or rantime == 15:

        ex = d(resourceId="com.kuaishou.nebula:id/comment_icon").exists
        if ex:
            d(resourceId="com.kuaishou.nebula:id/comment_icon").click_exists(2)
            sleeps(3)
            d(resourceId="com.kuaishou.nebula:id/comment_editor_holder_text").click_exists(2)
            sleeps(3)
            print('发起评论')
            with open('kuai.json', 'r') as f:
                data = json.load(f)
                i = random.randint(0, len(data)-1)
                str = data[i]
                sleeps(3)
                d(resourceId="com.kuaishou.nebula:id/editor").set_text(str, 2)
                # print(i)
                # print(data[i])
            sleeps(1)
            d(resourceId="com.kuaishou.nebula:id/finish_button").click_exists(2)
            sleeps(2)
            d(resourceId="com.kuaishou.nebula:id/photo_detail_panel_close").click_exists(2)
            sleeps(3)

