from playsound import playsound
import customtkinter as ctk
from time import sleep
import webbrowser
import threading
import os


class Timer:
    def __init__(self):
        self.full_seconds = 0
        self.pause_event = threading.Event()

    def start_timer(self, hours: int, minutes: int, seconds: int):
        """Start the timer countdown with the given time in hours, minutes, and seconds."""
        self.full_seconds = hours * 3600 + minutes * 60 + seconds
        self.full_seconds1 = hours * 3600 + minutes * 60 + seconds

        while self.full_seconds > 0:
            if not self.pause_event.is_set():
                self.full_seconds -= 1
                minutes, seconds = divmod(self.full_seconds, 60)
                hours, minutes = divmod(minutes, 60)
                time_label.configure(text=f'{hours:02d}:{minutes:02d}:{seconds:02d}')
                self.update_progressbar()
            
            # Play a sound when the timer reaches 0 (end of countdown).
            if self.full_seconds == 0:
                playsound(rf'sounds/{choose_alarm_option.get()}') # TODO: Add more sounds later.

            sleep(1)

        self.reset_timer()

    def update_progressbar(self):
        progressbar.set(1 - self.full_seconds / self.full_seconds1)
        
    def pause_timer(self):
        """Pause or continue the timer countdown."""
        if self.pause_event.is_set():
            self.pause_event.clear()
            start_button.configure(text='Pause')
        else:
            self.pause_event.set()
            start_button.configure(text='Continue')

    def reset_timer(self):
        """Reset the timer to 00:00:00."""
        self.full_seconds = 0
        self.pause_event.clear()
        time_label.configure(text='00:00:00', text_color='white')
        start_button.configure(text='Start', fg_color='green', command=start_timer_thread)
        progressbar.set(0)


def start_timer_thread():
    """Start the timer countdown."""
    timer.full_seconds = 0
    timer.pause_event.clear()
    start_button.configure(text='Pause', fg_color='blue', command=timer.pause_timer)
    
    # Start the timer in a separate thread to avoid freezing the GUI.
    threading.Thread(target=lambda: timer.start_timer(int(hours_entry.get() or 0), int(mins_entry.get() or 0), int(secs_entry.get() or 0))).start()

def open_github_link(e):
    """Open the GitHub link when the info_label is clicked."""
    webbrowser.open_new_tab('https://github.com/anekobtw')

# Create an instances classes.
timer = Timer()

# Create the main application window using customtkinter.
root = ctk.CTk()
root.title('TimeWise')
root._set_appearance_mode('dark')

# Create widgets for the application window.
info_label = ctk.CTkLabel(root, text='v0.3 beta\nby anekobtw', text_color='lightblue')
info_label.bind('<Button-1>', open_github_link)  # Bind the GitHub link opening function to the info_label click event.
info_label.grid(row=0, column=5, padx=5, pady=5)

progressbar = ctk.CTkProgressBar(root)
progressbar.set(0)
progressbar.grid(row=0, column=1)

time_label = ctk.CTkLabel(root, text='00:00:00', font=('digital-7', 22))
time_label.grid(row=1, column=1, padx=5, pady=5)

hours_entry = ctk.CTkEntry(root, placeholder_text='Hour', justify='center')
hours_entry.grid(row=2, column=0, padx=5, pady=5)

mins_entry = ctk.CTkEntry(root, placeholder_text='Minute', justify='center')
mins_entry.grid(row=2, column=1, padx=5, pady=5)

secs_entry = ctk.CTkEntry(root, placeholder_text='Second', justify='center')
secs_entry.grid(row=2, column=2, padx=5, pady=5)

start_button = ctk.CTkButton(root, text='Start', fg_color='green', command=start_timer_thread)
start_button.grid(row=3, column=1, padx=5, pady=5)

reset_button = ctk.CTkButton(root, text='Reset', fg_color='red', command=timer.reset_timer)
reset_button.grid(row=3, column=0, padx=5, pady=5)

choose_alarm_option = ctk.CTkOptionMenu(root, values=list(os.listdir('sounds')))
choose_alarm_option.grid(row=3, column=2, padx=5, pady=5)

root.mainloop()
