import os
import re
import tkinter as tk
from datetime import datetime
from tkinter import messagebox

from Generater.OTMailGenerator import generateLeaveMail
from Validate.FiledValidate import is_empty, is_numeric, is_valid_date, is_valid_time


class EmailGUI:
    g_dict = {}

    # g_entry_name = None
    # g_entry_staff_ID = None
    # g_entry_start_date = None
    # g_entry_start_time = None
    # g_entry_end_date = None
    # g_entry_end_time = None
    # g_text_detail = None

    g_value_name = ''
    g_value_staff_ID = ''
    g_value_start_date = ''
    g_value_start_time = ''
    g_value_end_date = ''
    g_value_end_time = ''
    g_value_detail = ''

    g_value_dict = {}

    def __init__(self):
        pass

    def generateGUIwithEmailInfo(self):
        root = tk.Tk()
        root.title("Email Generator")

        current_datetime = datetime.now()
        date_format = "%Y-%m-%d"
        time_format = "%H:%M:%S"

        self.generateEntry(root, "Name", 0, os.getlogin())
        self.generateEntry(root, "Staff ID", 1, '')
        self.generateEntry(root, "Start Date", 2, current_datetime.strftime(date_format))
        self.generateEntry(root, "Start Time", 3, current_datetime.strftime(time_format))
        self.generateEntry(root, "End Date", 4, current_datetime.strftime(date_format))
        self.generateEntry(root, "End Time", 5, current_datetime.strftime(time_format))
        self.generateText(root, "Detail", 6)
        self.generateButton(root, "Generate", 7)

        root.mainloop()

    def generateEntry(self, root, entryName, rowNum, defaultValue):
        label = tk.Label(root, text=entryName + ":")
        entryObj = tk.Entry(root, width=30)
        entryObj.insert(0, defaultValue)
        label.grid(row=rowNum, column=0, padx=10, pady=5, sticky="w")
        entryObj.grid(row=rowNum, column=1, padx=10, pady=5)
        self.g_dict[entryName] = entryObj

    def generateText(self, root, textName, ruwNum):
        label = tk.Label(root, text=textName + ":")
        label.grid(row=ruwNum, column=0, padx=10, pady=5, sticky="w")

        textObj = tk.Text(root, height=5, width=30)
        scrollbar = tk.Scrollbar(root, command=textObj.yview)
        textObj.config(yscrollcommand=scrollbar.set)

        textObj.grid(row=ruwNum, column=1, padx=10, pady=5, sticky="w")
        scrollbar.grid(row=ruwNum, column=1, padx=0, pady=5, sticky="nse")

        self.g_dict[textName] = textObj

    def generateButton(self, root, buttonName, rowNum):
        button = tk.Button(root, text=buttonName, command=self.captureValue)
        button.grid(row=rowNum, column=0, padx=10, pady=5, sticky="e")

    def captureValue(self):
        self.g_value_dict['Name'] = self.g_dict['Name'].get()
        self.g_value_dict['Staff ID'] = self.g_dict['Staff ID'].get()
        self.g_value_dict['Start Date'] = self.g_dict['Start Date'].get()
        self.g_value_dict['Start Time'] = self.g_dict['Start Time'].get()
        self.g_value_dict['End Date'] = self.g_dict['End Date'].get()
        self.g_value_dict['End Time'] = self.g_dict['End Time'].get()
        self.g_value_dict['Detail'] = self.g_dict['Detail'].get("1.0", "end-1c")
        errorInfo = self.validateValue()

        if errorInfo == "":
            generateLeaveMail(self.g_value_dict)

    def validateValue(self):
        errorInfo = ""
        if is_empty(self.g_value_dict['Name']):
            errorInfo = "Name cannot be empty!\r\n"

        if is_empty(self.g_value_dict['Staff ID']):
            errorInfo += "Staff ID cannot be empty!\r\n"
        if not is_numeric(self.g_value_dict['Staff ID']):
            errorInfo += "Staff ID should be numeric!\r\n"

        if not is_valid_date(self.g_value_dict['Start Date']):
            errorInfo += "Start date is not match format yyyy-mm-dd!\r\n"

        if not is_valid_time(self.g_value_dict['Start Time']):
            errorInfo += "Start time is not match format hh:mi:ss!\r\n"

        if not is_valid_date(self.g_value_dict['End Date']):
            errorInfo += "End date is not match format yyyy-mm-dd!\r\n"

        if not is_valid_time(self.g_value_dict['End Time']):
            errorInfo += "End time is not match format hh:mi:ss!\r\n"

        if is_empty(self.g_value_dict['Detail']):
            errorInfo += "Detail should not be empty!\r\n"

        if not is_empty(errorInfo):
            messagebox.showerror("Error", re.sub(r'\r\n$', '', errorInfo))
            return errorInfo

        return ""