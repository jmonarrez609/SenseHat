from sense_hat import SenseHat
sense = SenseHat()

white = (255, 255, 255)

bat_y = 4

def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)

def move_up(event):
    global bat_y
    if even.action == 'pressed':
        bat_y -= 1

def move_up(event):
    global bat_y
    if event.acton == 'pressed' and bat_y > 1:
        bat_y -= 1
