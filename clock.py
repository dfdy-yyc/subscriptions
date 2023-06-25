import time

def focus_timer(duration):
    print("开始专注时钟，持续时间：{}秒".format(duration))

    while duration > 0:
        # 计算剩余的分钟和秒数
        minutes, seconds = divmod(duration, 60)
        time_remaining = "{:02d}:{:02d}".format(minutes, seconds)

        print("\r剩余时间：{}".format(time_remaining), end="")
        time.sleep(1)
        duration -= 1

    print("\n专注时钟结束。")
