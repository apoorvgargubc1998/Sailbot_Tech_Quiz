import unittest
class AngleCalc:
    def boundTo180(self,angle):
        angle = angle%360 if angle >=0 else angle%-360
        if (angle <= -180): angle += 360
        elif (angle > 180): angle -= 360
        return angle    
    def IsAngleBetween(self,first_angle,middle_angle,second_angle):
        angle_diff1 = middle_angle - first_angle
        angle_diff2 =  second_angle - middle_angle
        if (angle_diff1 > 180):
            angle_diff1 -=360
        if (angle_diff1 < -180):
            angle_diff1 +=360
        if (angle_diff2 > 180):
            angle_diff2 -=360
        if (angle_diff2 < -180):
            angle_diff2 +=360
        if (abs(angle_diff1 + angle_diff2) >= 180): 
            return False
        else: 
            return((angle_diff1 < 0 and angle_diff2 < 0) or (angle_diff1 > 0 and angle_diff2 > 0))

class TestAngleCalc(unittest.TestCase):
    def test_boundTo180_1(self):
        myobj = AngleCalc()
        angle = 360
        self.assertEqual(myobj.boundTo180(angle),0,"should be 0")
    def test_boundTo180_2(self):
        myobj = AngleCalc()
        angle = 270
        self.assertEqual(myobj.boundTo180(angle),-90,"should be -90")
    def test_boundTo180_3(self):
        myobj = AngleCalc()
        angle = -450
        self.assertEqual(myobj.boundTo180(angle),-90,"should be -90")
    def test_IsAngleBetween_1(self):
        myobj = AngleCalc()
        self.assertEqual(myobj.IsAngleBetween(-90,-180,110),True,"should be True")
    def test_IsAngleBetween_2(self):
        myobj = AngleCalc()
        self.assertEqual(myobj.IsAngleBetween(-90,-180,80),False,"should be False")


if __name__ == '__main__':
    unittest.main()

## it has been setup in a way that you just have to run this python file from the terminal "python <path>sailbot_AG.py"