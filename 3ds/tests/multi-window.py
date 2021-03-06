from citrus import *

gfx.init_default()

left  = console.PrintConsole(gfx.SCREEN_TOP, window_x=1, window_y=1, window_width=23, window_height=28)
right = console.PrintConsole(gfx.SCREEN_TOP)
bot   = console.PrintConsole(gfx.SCREEN_BOTTOM)

left.set_color(bg=console.COLOR_BLUE)
right.set_window(26, 1, 23, 28)

left.select()
print('This text is in the left window!')
print('3DS rocks!!!')
print('x: %d\ny: %d\nw: %d\nh: %d\nfg: %d\nbg: %d' %
    (left.window_x, left.window_y, left.window_width, left.window_height, left.fg, left.bg))
left.set_color()
print('Color reset!')

right.select()
print('This text is in the right window!')
print('This thing works pretty well!')
print('x: %d\ny: %d\nw: %d\nh: %d\nfg: %d\nbg: %d' %
    (right.window_x, right.window_y, right.window_width, right.window_height, right.fg, right.bg))

bot.select()
bot.set_position(x=10, y=29)
print('Press Start to exit.', end_data='')

while apt.main_loop():
    hid.scan_input()

    if hid.keys_down() & hid.KEY_START:
        break

    gfx.flush_buffers()
    gfx.swap_buffers()

    gsp.wait_for_vblank()

gfx.exit()
