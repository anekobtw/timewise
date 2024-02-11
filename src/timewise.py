import os
import threading
import time
import webbrowser

import customtkinter as ctk
from playsound import playsound


class App(ctk.CTk):
    def __init__(self, timer):
        super().__init__()
        self.timer = timer
        self.title('TimeWise')
        self.create_widgets()

    def create_widgets(self) -> None:
        self.info_label = ctk.CTkLabel(self, text='v0.4 beta\nby anekobtw', text_color='lightblue')
        self.info_label.bind('<Button-1>', lambda e: webbrowser.open_new_tab('https://github.com/anekobtw'))
        self.info_label.grid(row=0, column=5, padx=5, pady=5)

        self.time_label = ctk.CTkLabel(self, text='00:00:00', font=('digital-7', 22))
        self.time_label.grid(row=0, column=1, padx=5, pady=5)

        self.hours_entry = ctk.CTkEntry(self, placeholder_text='Hour', justify='center')
        self.hours_entry.grid(row=1, column=0, padx=5, pady=5)

        self.mins_entry = ctk.CTkEntry(self, placeholder_text='Minute', justify='center')
        self.mins_entry.grid(row=1, column=1, padx=5, pady=5)

        self.secs_entry = ctk.CTkEntry(self, placeholder_text='Second', justify='center')
        self.secs_entry.grid(row=1, column=2, padx=5, pady=5)

        self.start_button = ctk.CTkButton(self, text='Start', fg_color='green', command=lambda: start_timer_thread(self.timer, self))
        self.start_button.grid(row=2, column=1, padx=5, pady=5)

        self.reset_button = ctk.CTkButton(self, text='Reset', fg_color='red', command=self.timer.reset_timer)
        self.reset_button.grid(row=2, column=0, padx=5, pady=5)

        self.choose_alarm_option = ctk.CTkOptionMenu(self, values=list(os.listdir('sounds')))
        self.choose_alarm_option.grid(row=2, column=2, padx=5, pady=5)


class Timer:
    def __init__(self):
        self.full_seconds = 0
        self.pause_event = False

    def set_app(self, app: App) -> None:
        self.app = app

    def start_timer(self, hours: int, minutes: int, seconds: int) -> None:
        """Start the timer countdown with the given time in hours, minutes, and seconds."""
        self.full_seconds = hours * 3600 + minutes * 60 + seconds

        while self.full_seconds > 0:
            if self.pause_event:
                pass

            self.full_seconds -= 1
            minutes, seconds = divmod(self.full_seconds, 60)
            hours, minutes = divmod(minutes, 60)
            self.app.time_label.configure(text=f'{hours:02d}:{minutes:02d}:{seconds:02d}')

            if self.full_seconds == 0:
                sound_file = os.path.join('sounds', self.app.choose_alarm_option.get())
                playsound(sound_file)

            time.sleep(1)

        self.reset_timer()

    def pause_timer(self) -> None:
        """Pause or continue the timer countdown."""
        self.pause_event = True if not self.pause_event else False
        self.start_button.configure(text='Pause') if self.pause_event else self.start_button.configure(text='Continue')

    def reset_timer(self) -> None:
        """Reset the timer to 00:00:00."""
        self.full_seconds = 0
        self.pause_event = False
        self.app.time_label.configure(text='00:00:00', text_color='white')
        self.app.start_button.configure(text='Start', fg_color='green', command=lambda: start_timer_thread(self, self.app))


def start_timer_thread(timer: Timer, app: App) -> None:
    """Start the timer countdown."""
    timer.reset_timer()
    threading.Thread(target=lambda: timer.start_timer(int(app.hours_entry.get() or 0), int(app.mins_entry.get() or 0), int(app.secs_entry.get() or 0))).start()


def main():
    timer = Timer()
    app = App(timer)
    timer.set_app(app)
    app.mainloop()


if __name__ == '__main__':
    main()
