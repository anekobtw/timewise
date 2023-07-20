import customtkinter as ctk
import threading
import pygame
import time
import os

pause_event = threading.Event()
pygame.init()
os.system('cls')


class Timer:
    def __init__(self):
        self.full_seconds = 0

    def start_timer_thread(self):
        if start_button.text == 'Start':
            self.full_seconds = 0
            pause_event.clear()
            start_button.configure(text='Pause', fg_color='blue')
            threading.Thread(target=self.start_timer).start()
        else:
            self.pause_timer()

    def start_timer(self):
        hours = int(hours_entry.get()) if hours_entry.get().isdigit() else 0
        minutes = int(mins_entry.get()) if mins_entry.get().isdigit() else 0
        seconds = int(secs_entry.get()) if secs_entry.get().isdigit() else 0
        self.full_seconds = hours * 3600 + minutes * 60 + seconds

        while self.full_seconds > 0:
            if not pause_event.is_set():
                self.full_seconds -= 1

                minutes, seconds = divmod(self.full_seconds, 60)
                hours, minutes = divmod(minutes, 60)

                time_label.configure(text=f'{hours:02d}:{minutes:02d}:{seconds:02d}')
                if self.full_seconds <= 10:
                    time_label.configure(fg='red')
                if self.full_seconds == 0:
                    self.reset_timer()
                    pygame.mixer.Sound('sound_01.mp3').play()                     

                time.sleep(1)

    def pause_timer(self):
        if pause_event.is_set():
            pause_event.clear()
            start_button.configure(text='Pause')
        else:
            pause_event.set()
            start_button.configure(text='Continue')

    def reset_timer(self):
        self.full_seconds = 0
        time_label.configure(text='00:00:00', fg='white')
        start_button.configure(text='Start', fg_color='green')

timer = Timer()
root = ctk.CTk()
root.title('TimeWise')
root.set_appearance_mode('dark')

info_label = ctk.CTkLabel(root, text=f'v0.2 beta\nby anekobtw')
info_label.grid(row=0, column=5, padx=5, pady=5)

time_label = ctk.CTkLabel(root, text='00:00:00')
time_label.grid(row=0, column=1, padx=5, pady=5)

hours_entry = ctk.CTkEntry(root, placeholder_text='Hour', justify='center')
hours_entry.grid(row=1, column=0, padx=5, pady=5)

mins_entry = ctk.CTkEntry(root, placeholder_text='Minute', justify='center')
mins_entry.grid(row=1, column=1, padx=5, pady=5)

secs_entry = ctk.CTkEntry(root, placeholder_text='Second', justify='center')
secs_entry.grid(row=1, column=2, padx=5, pady=5)

start_button = ctk.CTkButton(root, text='Start', fg_color='green', command=timer.start_timer_thread)
start_button.grid(row=2, column=1, padx=5, pady=5)

reset_button = ctk.CTkButton(root, text='Reset', fg_color='red', command=timer.reset_timer)
reset_button.grid(row=2, column=0, padx=5, pady=5)

change_alarm_button = ctk.CTkButton(root, text='Change Alarm (In developing)', fg_color='grey', state='disabled')
change_alarm_button.grid(row=2, column=2, padx=5, pady=5)

root.mainloop()
