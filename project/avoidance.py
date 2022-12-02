import RPi.GPIO as GPIO
import time


class Avoidance:
    # distance: distance from obstacle to stop at
    def __init__(self, car, distance=40):
        self.car = car
        self.distance = distance
        
        #Set the GPIO port to BIARD encoding mode
        GPIO.setmode(GPIO.BOARD)

        #Ignore the warning message
        GPIO.setwarnings(False)

        self.AvoidSensorLeft = 21     #Left infrared obstacle avoidance sensor pin
        self.AvoidSensorRight = 19    #Right infrared obstacle avoidance sensor pin
        Avoid_ON = 22   #Infrared obstacle avoidance sensor switch pin

        #Define the pins of the ultrasonic module
        self.EchoPin = 18
        self.TrigPin = 16

        #Set pin mode
        GPIO.setup(self.AvoidSensorLeft,GPIO.IN)
        GPIO.setup(self.AvoidSensorRight,GPIO.IN)
        GPIO.setup(Avoid_ON,GPIO.OUT)
        GPIO.setup(self.EchoPin,GPIO.IN)
        GPIO.setup(self.TrigPin,GPIO.OUT)
        GPIO.output(Avoid_ON,GPIO.HIGH)
        
    
    #Ultrasonic function
    def Distance(self):
        GPIO.output(self.TrigPin,GPIO.LOW)
        time.sleep(0.000002)
        GPIO.output(self.TrigPin,GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output(self.TrigPin,GPIO.LOW)

        t3 = time.time()

        while not GPIO.input(self.EchoPin):
            t4 = time.time()
            if (t4 - t3) > 0.03 :
                return -1
        t1 = time.time()
        while GPIO.input(self.EchoPin):
            t5 = time.time()
            if(t5 - t1) > 0.03 :
                return -1

        t2 = time.time()
        #time.sleep(0.01)
        #print ("distance_1 is %d " % (((t2 - t1)* 340 / 2) * 100))
        return ((t2 - t1)* 340 / 2) * 100


    def Distance_test(self):
        num = 0
        ultrasonic = []
        while num < 5:
                distance = self.Distance()
                #print("distance is %f"%(distance) )
                while int(distance) == -1 :
                    distance = self.Distance()
                    #print("Tdistance is %f"%(distance) )
                while (int(distance) >= 500 or int(distance) == 0) :
                    distance = self.Distance()
                    #print("Edistance is %f"%(distance) )
                ultrasonic.append(distance)
                num = num + 1
                #time.sleep(0.01)
        #print ('ultrasonic')
        distance = (ultrasonic[1] + ultrasonic[2] + ultrasonic[3])/3
        #print("distance is %f"%(distance) ) 
        return distance


    def avoid(self):
        distance = self.Distance_test()
        LeftSensorValue  = GPIO.input(self.AvoidSensorLeft);
        RightSensorValue = GPIO.input(self.AvoidSensorRight);
        # On the current robot, the left one doesn't work. The right one works if kept out of sunlight.
        if distance < self.distance:# or RightSensorValue == False or LeftSensorValue == False:
            self.car.Car_Stop()
            print("Something is in my way!")
            time.sleep(1)
            print("Trying again . . . ")
            self.avoid()
            