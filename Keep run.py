import threading
import subprocess
import datetime
import pytz
import time

def shutdown_at_specific_time(hour, minute, timezone):
    tz = pytz.timezone(timezone)
    current_time = datetime.datetime.now(tz)
    shutdown_time = current_time.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if current_time > shutdown_time:
        shutdown_time += datetime.timedelta(days=1)  # If the specified time is already passed, schedule for the next day
    time_diff = (shutdown_time - current_time).total_seconds()
    print(f"Device will shut down at {shutdown_time.strftime('%Y-%m-%d %H:%M:%S %Z')} (in {time_diff} seconds).")
    time.sleep(time_diff)
    print("Shutting down...")
    subprocess.call(["shutdown", "-h", "now"])

# Set the time at which you want to shut down the device (in Tashkent timezone)
shutdown_hour = 8
shutdown_minute = 30
tashkent_timezone = 'Asia/Tashkent'

# Create a daemon thread for the shutdown timer
shutdown_thread = threading.Thread(target=shutdown_at_specific_time, args=(shutdown_hour, shutdown_minute, tashkent_timezone))
shutdown_thread.daemon = True
shutdown_thread.start()

# Keep the main program running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting the program...")
