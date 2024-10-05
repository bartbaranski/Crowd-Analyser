import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import Label
from PIL import Image, ImageTk
import cv2
from video_processing import process_video
from yolo_detection import detect_people
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class VideoAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crowd Analysis")

        # Pobranie rozmiaru ekranu i ustawienie okna na pełen ekran w trybie okienkowym
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")  # Ustawienie rozmiaru na pełen ekran

        # Reszta kodu bez zmian...
        
        # Podział okna na lewą i prawą stronę (dwa główne panele)
        self.left_frame = tk.Frame(root)
        self.left_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)

        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)

        # Podział lewego panelu na górny i dolny panel
        self.left_upper_frame = tk.Frame(self.left_frame)
        self.left_upper_frame.pack(fill='both', expand=True)

        self.left_lower_frame = tk.Frame(self.left_frame)
        self.left_lower_frame.pack(fill='both', expand=True)

        # Podział prawego panelu na górny i dolny panel
        self.right_upper_frame = tk.Frame(self.right_frame)
        self.right_upper_frame.pack(fill='both', expand=True)

        self.right_lower_frame = tk.Frame(self.right_frame)
        self.right_lower_frame.pack(fill='both', expand=True)

        # --- Lewa strona ---
        # Wykres w górnej części lewego panelu
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.ax.set_title("People Count Over Time")
        self.ax.set_xlabel("Frame")
        self.ax.set_ylabel("People Count")
        self.line, = self.ax.plot([], [], 'r-')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.left_upper_frame)
        self.canvas.get_tk_widget().pack(pady=20, expand=True, fill='both')

        # Dolna część lewego panelu (możesz tu dodać inne statystyki w przyszłości)
        self.left_lower_label = tk.Label(self.left_lower_frame, text="Additional Info (Placeholder)", font=("Arial", 14))
        self.left_lower_label.pack(pady=20, expand=True)

        # --- Prawa strona ---
        # Przycisk do otwierania plików wideo (umieszczony w górnym panelu, nad wideo)
        self.open_button = tk.Button(self.right_upper_frame, text="Open Video", command=self.open_file)
        self.open_button.pack(pady=10, anchor="n")

        # Etykieta do wyświetlania klatek wideo (okno wideo pod przyciskiem)
        self.video_label = Label(self.right_upper_frame)
        self.video_label.pack()

        # Licznik klatek w dolnym panelu (z napisem "Frames:")
        self.frame_counter_label = Label(self.right_lower_frame, text="Frames: 0/0", font=("Arial", 14))
        self.frame_counter_label.pack(pady=20)

        # Inicjalizacja zmiennych
        self.video_path = None
        self.frames = None
        self.current_frame = 0
        self.skip_frames = 2
        self.total_people = 0
        self.fps = 30  # Domyślna liczba klatek na sekundę w wideo
        self.people_count_over_time = []  # Lista do przechowywania liczby osób w czasie

    def open_file(self):
        # Umożliwienie użytkownikowi wyboru pliku wideo
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi")])

        if file_path:
            self.video_path = file_path
            self.frames = process_video(self.video_path)
            self.current_frame = 0
            self.total_people = 0
            self.people_count_over_time = []  # Zresetowanie wykresu
            self.play_video()

    def update_gui_with_frame(self, frame):
        # Przetwarzanie obrazu z OpenCV do tkinter (PIL -> ImageTk)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        img_tk = ImageTk.PhotoImage(image=img)

        # Aktualizacja etykiety z obrazem
        self.video_label.imgtk = img_tk
        self.video_label.configure(image=img_tk)

    def update_frame_counter(self):
        # Aktualizacja licznika klatek w formacie xxx/yyy
        total_frames = len(self.frames)
        self.frame_counter_label.config(text=f"Frames: {self.current_frame}/{total_frames}")

    def update_plot(self):
        # Aktualizacja wykresu
        self.line.set_data(range(len(self.people_count_over_time)), self.people_count_over_time)
        self.ax.set_xlim(0, len(self.people_count_over_time))
        self.ax.set_ylim(0, max(self.people_count_over_time) if self.people_count_over_time else 1)
        self.canvas.draw()

    def play_video(self):
        if self.frames and self.current_frame < len(self.frames):
            if self.current_frame % self.skip_frames == 0 or self.current_frame == len(self.frames) - 1:
                # Wykrywanie osób w bieżącej klatce
                people_count, processed_frame = detect_people(self.frames[self.current_frame])

                # Aktualizacja liczby osób
                self.total_people += people_count
                self.people_count_over_time.append(self.total_people)

                # Aktualizacja interfejsu graficznego (klatka + licznik)
                self.update_gui_with_frame(processed_frame)
                self.update_frame_counter()

                # Aktualizacja wykresu
                self.update_plot()

            self.current_frame += 1

            # Odświeżenie co 30 ms (33 klatki na sekundę)
            self.root.after(30, self.play_video)
        else:
            # Zakończenie analizy
            self.show_results()

    def show_results(self):
        # Obliczenie średniej liczby osób na minutę
        video_duration_minutes = len(self.frames) / (self.fps * 60)
        avg_people_per_minute = self.total_people / video_duration_minutes

        # Wyświetlenie wyników w oknie dialogowym
        messagebox.showinfo("Results", f"Total People: {self.total_people}\nAverage People per Minute: {avg_people_per_minute:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoAnalyzerApp(root)
    root.mainloop()
