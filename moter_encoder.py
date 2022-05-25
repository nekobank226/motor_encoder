
import pigpio
import time
import Adafruit_PCA9685
import rotary_encoder

# 設定周波数
SET_FREQ = 50

# ピンの設定
pi = pigpio.pi()
pi.set_mode(14, pigpio.OUTPUT)
pi.set_mode(15, pigpio.OUTPUT)
pi.set_mode(17, pigpio.INPUT)
pi.set_mode(27, pigpio.INPUT)

# PCA9685の初期化
PCA9685 = Adafruit_PCA9685.PCA9685()
PCA9685.set_pwm_freq(SET_FREQ)

motor_count = 0
gear_ratio = 171.79
encoder_count = 48

def motor_angle(angle:float):
    if angle == 0:
        pi.write(14, 0)
        pi.write(15, 0)
        PCA9685.set_pwm(0, 0, 0)
        return
    
    rotation_count = int(angle * 360 / gear_ratio * encoder_count)
    print("回転開始")
    pi.write(14, 1)
    pi.write(15, 0)
    PCA9685.set_pwm(0, 0, 2000)
    
