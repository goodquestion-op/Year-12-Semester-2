from sshkeyboard import listen_keyboard 

def press(key):
    # print(f"'{key}' pressed")
    return

def release(key):
    # print(f"'{key}' released")
    return

listen_keyboard(
    on_press=press,
    on_release=release,
)