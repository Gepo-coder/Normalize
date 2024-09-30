import os
import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip, AudioFileClip
from pydub import AudioSegment

def normalize_audio(video_path, output_path, target_loudness):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio_path = "temp_audio.wav"
    audio.write_audiofile(audio_path)

    audio_segment = AudioSegment.from_wav(audio_path)
    gain = target_loudness - audio_segment.dBFS
    normalized_audio = audio_segment.apply_gain(gain)

    # Salvar o áudio normalizado
    normalized_audio.export("normalized_audio.wav", format="wav")

    # Carregar o áudio normalizado como um objeto do MoviePy
    normalized_audio_clip = AudioFileClip("normalized_audio.wav")

    # Substituir o áudio no vídeo
    video_with_normalized_audio = video.set_audio(normalized_audio_clip)
    video_with_normalized_audio.write_videofile(output_path, codec="libx264")

def process_videos(input_folder, output_folder, target_loudness):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"normalized_{filename}")
            normalize_audio(input_path, output_path, target_loudness)
            print(f"Processado: {filename}")

    messagebox.showinfo("Finalizado", "Processamento completo!")

def select_input_folder():
    folder = filedialog.askdirectory()
    input_folder_var.set(folder)

def select_output_folder():
    folder = filedialog.askdirectory()
    output_folder_var.set(folder)

def start_processing():
    input_folder = input_folder_var.get()
    target_loudness = float(target_loudness_var.get())

    if not input_folder:
        messagebox.showwarning("Aviso", "Por favor, selecione a pasta de entrada.")
        return

    # Criar a pasta de saída com o nome da pasta de entrada + "_Normalized"
    output_folder = os.path.join(os.path.dirname(input_folder), os.path.basename(input_folder) + "_Normalized")
    os.makedirs(output_folder, exist_ok=True)  # Criar a pasta se não existir

    process_videos(input_folder, output_folder, target_loudness)

# Configuração da interface
root = tk.Tk()
root.title("Normalizador de Áudio de Vídeo")

input_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()
target_loudness_var = tk.StringVar(value="-23.0")  # Valor padrão em LUFS

tk.Label(root, text="Pasta de Entrada:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=input_folder_var, width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Selecionar", command=select_input_folder).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Pasta de Saída:").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=output_folder_var, width=50).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Selecionar", command=select_output_folder).grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text="Loudness alvo (LUFS):").grid(row=2, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=target_loudness_var).grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text="Processar Vídeos", command=start_processing).grid(row=3, column=1, padx=5, pady=10)

root.mainloop()
