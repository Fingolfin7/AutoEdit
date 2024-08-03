import os
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from AutoEdit import AutoEdit
from PIL import ImageTk
from tkinter.filedialog import askopenfilenames


class GUI:
    def __init__(self, tk_root: Tk):
        self.images = []
        self.auto_edit = AutoEdit()
        self.frame = Frame(tk_root)
        self.body = LabelFrame(self.frame)
        self.preview = LabelFrame(self.frame)

        self.out_dir = StringVar()
        self.out_dir.set("Output")

        self.images_count = IntVar()

        self.brightness_factor = DoubleVar()
        self.brightness_factor.set(1.0)

        self.contrast_factor = DoubleVar()
        self.contrast_factor.set(1.0)

        self.sharpness_factor = DoubleVar()
        self.sharpness_factor.set(1.0)

        self.rotate_angle = IntVar()
        self.rotate_angle.set(0)

        self.filter_effects = ["BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE", "EMBOSS", "FIND_EDGES",
                               "SHARPEN", "SMOOTH", "SMOOTH_MORE"]
        self.selected_filter = StringVar()

        # design stuff
        Label(self.body, text="Output Folder: ").grid(row=0, column=0, sticky=W, pady=2)
        self.output_folder_entry = Entry(self.body, textvariable=self.out_dir, width=25, borderwidth=2, relief="groove")
        self.output_folder_entry.grid(row=0, column=1, sticky=W, pady=2)
        self.output_folder_entry.focus_set()

        self.images_files = Button(self.body, text="Select Images")
        self.images_files.bind("<Button-1>", self.get_images)
        self.images_files.grid(row=2, column=0, sticky=W, pady=6)

        # reset all
        self.reset_button = Button(self.body, text="Reset", command=self.reset)
        self.reset_button.grid(row=2, column=1, sticky=W, pady=6)

        Label(self.body, text="Image count: ").grid(row=3, column=0, sticky=W, pady=2)
        self.chosen_images_count = Label(self.body, textvariable=self.images_count, background="light grey", width=21,
                                         justify="left", anchor="w")
        self.chosen_images_count.grid(row=3, column=1, sticky=W, pady=2)
        self.images_count.set(0)  # default

        # key bindings
        tk_root.bind("<Return>", self.apply_edits)
        tk_root.bind("<Escape>", self.close_application)

        # adjustments
        self.brightness_label = Label(self.body, text="Brightness: ")
        self.brightness_label.grid(row=4, column=0, sticky=W, pady=2)
        self.brightness_entry = Entry(self.body, textvariable=self.brightness_factor, width=25, borderwidth=2, relief="groove")
        self.brightness_entry.grid(row=4, column=1, sticky=W, pady=2)

        self.contrast_label = Label(self.body, text="Contrast: ")
        self.contrast_label.grid(row=5, column=0, sticky=W, pady=2)
        self.contrast_entry = Entry(self.body, textvariable=self.contrast_factor, width=25, borderwidth=2, relief="groove")
        self.contrast_entry.grid(row=5, column=1, sticky=W, pady=2)

        self.sharpness_label = Label(self.body, text="Sharpness: ")
        self.sharpness_label.grid(row=6, column=0, sticky=W, pady=2)
        self.sharpness_entry = Entry(self.body, textvariable=self.sharpness_factor, width=25, borderwidth=2, relief="groove")
        self.sharpness_entry.grid(row=6, column=1, sticky=W, pady=2)

        self.rotate_label = Label(self.body, text="Rotate Angle: ")
        self.rotate_label.grid(row=7, column=0, sticky=W, pady=2)
        self.rotate_entry = Entry(self.body, textvariable=self.rotate_angle, width=25, borderwidth=2, relief="groove")
        self.rotate_entry.grid(row=7, column=1, sticky=W, pady=2)

        Label(self.body, text="Filters: ").grid(row=8, column=0, sticky=W, pady=2)
        self.filter_menu = OptionMenu(self.body, self.selected_filter, *self.filter_effects)
        self.filter_menu.grid(row=8, column=1, sticky=W, pady=2)

        self.apply_filter_button = Button(self.body, text="Apply Edits", command=self.apply_edits)
        self.apply_filter_button.grid(row=9, column=0, sticky=W, pady=6)

        self.progress = ttk.Progressbar(self.body, orient=HORIZONTAL, length=240, mode='determinate')
        self.progress.grid(row=11, column=0, columnspan=2, pady=10)

        self.frame.pack()
        self.body.pack()
        self.preview.pack()


    def get_images(self, event=None):
        self.images = askopenfilenames(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.webp *.bmp *.tiff")])
        self.images_count.set(len(self.images))
        self.auto_edit.set_images(list(self.images))

    def close_application(self, event=None):
        self.frame.quit()

    def apply_edits(self, event=None):
        if len(self.images) == 0:
            messagebox.showinfo("No images selected", "Please select images.")
            return

        if not self.out_dir.get():
            messagebox.showinfo("No output directory", "Please specify an output directory.")
            return

        edits_confirmed = messagebox.askyesno("Confirm Edits",
                                              "Are you sure you want to apply these edits?")
        if not edits_confirmed:
            return

        edits_list = []

        total_steps = 6  # Number of steps to complete
        self.progress['maximum'] = total_steps
        current_step = 0

        # Adjust brightness
        if self.brightness_factor.get() != 1.0:
            self.auto_edit.adjust_brightness(self.brightness_factor.get())
            edits_list.append("Brightness")
        current_step += 1
        self.progress['value'] = current_step
        self.frame.update_idletasks()

        # Adjust contrast
        if self.contrast_factor.get() != 1.0:
            self.auto_edit.adjust_contrast(self.contrast_factor.get())
            edits_list.append("Contrast")
        current_step += 1
        self.progress['value'] = current_step
        self.frame.update_idletasks()

        # Adjust sharpness
        if self.sharpness_factor.get() != 1.0:
            self.auto_edit.adjust_sharpness(self.sharpness_factor.get())
            edits_list.append("Sharpness")
        current_step += 1
        self.progress['value'] = current_step
        self.frame.update_idletasks()

        # Rotate images
        if self.rotate_angle.get() != 0:
            self.auto_edit.rotate_images(self.rotate_angle.get())
            edits_list.append(f"Rotate {self.rotate_angle.get()} degrees")
        current_step += 1
        self.progress['value'] = current_step
        self.frame.update_idletasks()

        # Apply filter
        if self.selected_filter.get():
            self.auto_edit.apply_filter(self.selected_filter.get())
            edits_list.append(f"Filter: {self.selected_filter.get()}")
        current_step += 1
        self.progress['value'] = current_step
        self.frame.update_idletasks()

        # Save images to output directory
        self.auto_edit.save_images(self.out_dir.get())
        self.auto_edit.clear_images()
        current_step += 1
        self.progress['value'] = current_step
        self.frame.update_idletasks()


        if edits_list:
            formated_edits = '\n-'.join(edits_list)
            success_message = f"Images edited successfully. Edits applied: {formated_edits}"
        else:
            success_message = "No edits applied."


        messagebox.showinfo("Success", success_message)
        self.progress['value'] = 0  # Reset progress bar

        # open the output directory
        os.system(f"explorer /select, {self.out_dir.get()}")

    def reset(self, event=None):
        self.images = []
        self.images_count.set(0)
        self.auto_edit.clear_images()
        self.out_dir.set("")
        self.brightness_factor.set(1.0)
        self.contrast_factor.set(1.0)
        self.sharpness_factor.set(1.0)
        self.rotate_angle.set(0)
        self.selected_filter = ""


def resource_path(relative_path):
    """ Get absolute path to resource, needed for pyinstaller to correctly add resource files to the executable """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    root = Tk()
    root.title("AutoEdit v1.0")
    root.resizable(width=False, height=False)
    root.iconphoto(True, ImageTk.PhotoImage(file=resource_path('wand-icon.png')))
    gui = GUI(root)
    root.mainloop()
