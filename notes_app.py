import tkinter as tk
from tkinter import messagebox, filedialog
import os

class NotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Notes App")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Title label and entry
        self.title_label = tk.Label(root, text="Title:", font=("Arial", 12))
        self.title_label.pack(anchor='nw', padx=10, pady=(10, 0))
        self.title_entry = tk.Entry(root, font=("Arial", 12), width=40)
        self.title_entry.pack(anchor='nw', padx=10)

        # Text area for note content
        self.text_area = tk.Text(root, font=("Arial", 12), wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Button frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.save_button = tk.Button(self.button_frame, text="💾 Save", command=self.save_note)
        self.save_button.grid(row=0, column=0, padx=5)

        self.load_button = tk.Button(self.button_frame, text="📂 Load", command=self.load_note)
        self.load_button.grid(row=0, column=1, padx=5)

        self.clear_button = tk.Button(self.button_frame, text="🧹 Clear", command=self.clear_note)
        self.clear_button.grid(row=0, column=2, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="🗑️ Delete", command=self.delete_note)
        self.delete_button.grid(row=0, column=3, padx=5)

    def save_note(self):
        title = self.title_entry.get().strip()
        content = self.text_area.get("1.0", tk.END).strip()

        if not title:
            messagebox.showwarning("Missing Title", "Please enter a title.")
            return

        filename = f"{title}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

        messagebox.showinfo("Saved", f"Note '{title}' saved successfully.")

    def load_note(self):
        filename = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt")])
        if filename:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()

            title = os.path.basename(filename).replace(".txt", "")
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, title)
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", content)

    def clear_note(self):
        self.title_entry.delete(0, tk.END)
        self.text_area.delete("1.0", tk.END)

    def delete_note(self):
        title = self.title_entry.get().strip()
        if not title:
            messagebox.showwarning("Missing Title", "Please enter the note title to delete.")
            return

        filename = f"{title}.txt"
        if os.path.exists(filename):
            os.remove(filename)
            messagebox.showinfo("Deleted", f"Note '{title}' deleted successfully.")
            self.clear_note()
        else:
            messagebox.showerror("Not Found", f"No note found with the title '{title}'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()
