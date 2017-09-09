import blinkpy, pdb
blink = blinkpy.Blink(username=UNAME, password=PASS)
blink.setup_system()

for name, camera in blink.cameras.items():
    pdb.set_trace()
    print(name)                  # Name of the camera
    print(camera.id)             # Integer id of the camera (assigned by Blink)
    print(camera.armed)          # Whether the device is armed/disarmed (ie. detecting motion)
    print(camera.clip)           # Link to last motion clip captured
    print(camera.thumbnail)      # Link to current camera thumbnail
    print(camera.temperature)    # Current camera temperature (not super accurate, but might be useful for someone)
    print(camera.battery)        # Current battery level... I think the value ranges from 0-3, but not quite sure yet.
    print(camera.battery_string) # Gives battery level as a string ("OK" or "Low").  Returns "Unknown" if value is... well, unknown
    print(camera.notifications)  # Number of unread notifications (ie. motion alerts that haven't been viewed)
    print(camera.motion)         # Dictionary containing values for keys ['video', 'image', 'time']
    print(camera.image_link)     #
    print(camera.video_link)     #
                                 #   which corresponds to last motion recorded, thumbnail of last motion, and timestamp of last motion

