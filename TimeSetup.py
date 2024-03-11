import requests
import subprocess

def set_system_time():
    try:
        # Fetch current time from an internet time server in Pakistan
        response = requests.get("http://worldtimeapi.org/api/timezone/Asia/Karachi")
        data = response.json()
        
        # Extract the current time
        current_time = data['datetime']
        
        # Extract date and time components
        date_components = current_time.split("T")[0].split("-")
        time_components = current_time.split("T")[1].split(":")
        
        # Set the system time using subprocess
        subprocess.run(["cmd", "/C", "time", "{}:{}".format(time_components[0], time_components[1])])
        subprocess.run(["cmd", "/C", "date", "{}/{}/{}".format(date_components[2], date_components[1], date_components[0])])
        
        print("System time has been set to the internet time of Pakistan.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    # Call the function to set system time
    set_system_time()
