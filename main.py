# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from codrone_edu.drone import*

    # Use a breakpoint in the code line below to debug your script.
      # Press ⌘F8 to toggle the breakpoint.

dronebob = Drone()
# Press the green button in the gutter to run the script.
class tricks:
  def square(self):

      dronebob.pair()
      print("drone paired")
      dronebob.takeoff()
      power = 50
      dronebob.set_pitch(power)
      dronebob.move(.6)
      dronebob.set_pitch(0)
      dronebob.set_roll(power)
      dronebob.move(.6)
      dronebob.set_roll(0)
      dronebob.set_pitch(-power)
      dronebob.move(.6)
      dronebob.set_pitch(0)
      dronebob.set_roll(-power)
      dronebob.move(.6)
      dronebob.set_roll(0)
      dronebob.land()
      print("drone landed")
      dronebob.close()
  def square2(self):
    dronebob.pair()
    print("drone paired")
    dronebob.takeoff()
    power=43
    turn=50
    for i in range (4):
     dronebob.set_pitch(power)
     dronebob.move(.35)
     dronebob.set_pitch(0)
     dronebob.set_yaw(turn+8)
     dronebob.move(.7)
     dronebob.set_yaw(0)
    dronebob.land()
    print("drone landed")
    dronebob.close()
  def ellipse1(self):
    dronebob.pair()
    print("drone paired")
    dronebob.takeoff()
    power=100
    turn=100
    dronebob.set_pitch(power)
    dronebob.set_yaw(turn)
    dronebob.move(1.5)
    dronebob.land()
    print("drone landed")
    dronebob.close()
  def signwave(self):
    dronebob.pair()
    dronebob.takeoff()
    power=50
    dronebob.set_pitch(10)
    for i in range(3):
      dronebob.set_throttle(power)
      dronebob.move(.8)
      dronebob.set_throttle(-power)
      dronebob.move(.8)
    dronebob.land()
    dronebob.close()
  def spiral(self):
      dronebob.pair()
      dronebob.takeoff()
      power=50
      throttle=-60
      turn=110
      dronebob.set_throttle(40)
      dronebob.move(1.5)
      dronebob.set_throttle(0)
      for i in range(4):
        dronebob.set_pitch(power)
        dronebob.set_yaw(turn)
        dronebob.set_throttle(throttle)
        dronebob.move(.6)
        power-=3
        turn-=3
        throttle-=3

      dronebob.land()
      dronebob.close()

  def tri(self):
         power=50
         duration=.8
         turn=20
         dronebob.pair()
         dronebob.takeoff()
         dronebob.set_yaw(turn)
         dronebob.move(duration)
         dronebob.set_yaw(0)
         dronebob.set_pitch(power)
         dronebob.move(duration)
         dronebob.set_pitch(0)
         dronebob.set_yaw(-45)
         dronebob.move(duration)
         dronebob.set_yaw(0)
         dronebob.set_pitch(-power)
         dronebob.move(duration)
         dronebob.set_pitch(0)
         dronebob.set_yaw(turn)
         dronebob.move(duration)
         dronebob.set_yaw(0)
         dronebob.set_roll(-power)
         dronebob.move(duration)
         dronebob.set_roll(0)
         dronebob.land()
         dronebob.close()

  def obcourse(self):
      power = 50
      duration=.6
      dronebob.pair()
      dronebob.takeoff()
      dronebob.set_throttle(-35)
      dronebob.move(1.1)
      dronebob.set_throttle(0)
      dronebob.hover(1)
      dronebob.set_roll(power)
      dronebob.move(duration)
      dronebob.set_roll(0)
      dronebob.set_pitch(power)
      dronebob.move(duration+.3)
      dronebob.set_pitch(0)
      dronebob.set_roll(-power-.5)
      dronebob.move(duration+.6)
      dronebob.set_roll(0)
      dronebob.set_pitch(power)
      dronebob.move(duration+.1)
      dronebob.set_pitch(0)
      dronebob.set_roll(power)
      dronebob.move(duration)
      dronebob.set_roll(0)
      dronebob.set_pitch(power)
      dronebob.move(duration*2)
      dronebob.set_pitch(0)
      dronebob.land()
      dronebob.close()


dronetricks=tricks()






if __name__ == '__main__':
    #dronetricks.square()
    #dronetricks.square2()
    #dronetricks.ellipse1()
    #dronetricks.signwave()
    #dronetricks.spiral()
    #dronetricks.tri()
    dronetricks.obcourse()

















  # turn=50
 #for i in range (4):
 # dronebob.set_pitch(power)
  #dronebob.move(.6)
  #dronebob.set_pitch(0)
  #dronebob.set_yaw(turn+8)
 # dronebob.move(.6)
 # dronebob.set_yaw(0)
















# dronebob.set_pitch(power)
 #dronebob.move(.6)
 #dronebob.set_pitch(0)
 #dronebob.set_roll(power)
 #dronebob.move(.6)
 #dronebob.set_roll(0)
 #dronebob.set_pitch(-power)
 #dronebob.move(.6)
 #dronebob.set_pitch(0)
 #dronebob.set_roll(-power)
# dronebob.move(.6)
 #dronebob.set_roll(0)









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
