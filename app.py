import tkinter as tk
from tkinter import messagebox
#from storage import load_tasks, save_tasks
class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("менеджер задач")
        self.root.geometry("1000x500")

