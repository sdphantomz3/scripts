import subprocess
import webbrowser
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from threading import Thread
from tkinter import font
from django.core.management import call_command

class DjangoLauncherApp:
    def __init__(self, master):
        self.master = master
        master.title("Django Launcher")
        master.geometry("400x400")
        master.configure(bg="#f0f0f0")

        # Custom font
        custom_font = font.Font(family="Helvetica", size=12)

        # Create a Launch button
        self.launch_button = tk.Button(master, text="Launch Django", command=self.launch_django, bg="#007bff", fg="white", font=custom_font, padx=10, pady=5)
        self.launch_button.pack(pady=20)

        # Create a console widget
        self.console = scrolledtext.ScrolledText(master, height=10, bg="black", fg="white", font=custom_font)
        self.console.pack(expand=True, fill="both", padx=10, pady=10)

    def run_django_server(self):
        try:
            # Migrate the database
            self.append_to_console("Running migrations...")
            subprocess.run(["python", "manage.py", "migrate"], check=True)

            # Collect static files
            self.append_to_console("Collecting static files...")
            subprocess.run(["python", "manage.py", "collectstatic", "--noinput"], check=True)

            # Run the Django development server on port 3000
            self.append_to_console("Starting Django server...")
            server_process = subprocess.Popen(["python", "manage.py", "runserver", "3000"])

            # Open browser and link to the server
            self.append_to_console("Opening browser...")
            webbrowser.open("http://127.0.0.1:3000/")

            # Wait for the server process to finish
            server_process.wait()
        except subprocess.CalledProcessError as e:
            self.append_to_console(f"Error: {e}")
        except Exception as e:
            self.append_to_console(f"An unexpected error occurred: {e}")

    def open_admin_panel(self):
        # Open browser and link to the admin panel
        self.append_to_console("Opening admin panel...")
        webbrowser.open("http://127.0.0.1:3000/admin/")

    def launch_django(self):
        # Clear console
        self.clear_console()

        # Start Django server and open admin panel in separate threads
        django_thread = Thread(target=self.run_django_server)
        django_thread.start()

        admin_thread = Thread(target=self.open_admin_panel)
        admin_thread.start()

    def append_to_console(self, message):
        self.console.insert(tk.END, message + "\n")
        self.console.see(tk.END)

    def clear_console(self):
        self.console.delete(1.0, tk.END)

# Create the Tkinter window
root = tk.Tk()
app = DjangoLauncherApp(root)

# Run the Tkinter event loop
root.mainloop()
