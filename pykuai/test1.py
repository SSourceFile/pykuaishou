import json
import random
import time

import uiautomator2 as u2

# with open('kuai.json', 'r') as f:
#     data = json.load(f)
#     i = random.randint(0, len(data))
#     print(i)
#     print(data[i])

d = u2.connect("VBJDU18813002392")
d.app_start("com.kuaishou.nebula", stop=True)

time.sleep(5)
# 先进入到我的页面
print("成功进入了界面")
d(resourceId="com.kuaishou.nebula:id/circular_progress_bar").click_exists(2)
time.sleep(15)
d.swipe(0.45, 0.82, 0.512, 0.154)
time.sleep(3)
i = 0
while i<8:
    i= i+1
    # 福利
    d(index="23").click(20)
    time.sleep(35)
    d(resourceId="com.kuaishou.nebula:id/video_close_icon").click_exists(2)
    time.sleep(5)

#开宝箱

# d(index="44").click_exists(2)
# time.sleep(2)
# d.click(0.376, 0.579)
# time.sleep(15)
# d(resourceId="com.kuaishou.nebula:id/video_close_icon").click_exists(2)
# time.sleep(2)












