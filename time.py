import time

while True:
    # 获取当前时间
    current_time = time.strftime("%H:%M:%S", time.localtime())
    
    # 在控制台中打印当前时间
    print(current_time, end="\r")
    
    # 暂停一秒钟
    time.sleep(1)
