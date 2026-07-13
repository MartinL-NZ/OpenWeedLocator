from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

class GimbalController:

    def point_to(self, angle):

        servo_angle = angle + 90

        kit.servo[0].angle = servo_angle
