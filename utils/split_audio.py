import os
from pydub import AudioSegment


def split_audio_by_channel(filepath, target_dir_path, export_format="wav"):
    if os.path.isdir(filepath) or not os.path.exists(filepath):
        return
    sound = AudioSegment.from_file(file=filepath)
    channel_paths = []
    for idx, channel in enumerate(sound.split_to_mono()):
        filename = os.path.abspath(filepath).split(os.sep)[-1]
        tf = os.path.join(target_dir_path, f"{filename}-{idx}.wav")
        channel.export(tf, format=export_format)
        channel_paths.append(tf)

    return channel_paths


def split_audio_by_duration(
    audio_file_path, target_file_path, start_ms, end_ms, export_format="wav"
):
    audio = AudioSegment.from_file(file=audio_file_path)
    audio = audio[start_ms:end_ms]
    audio.export(target_file_path, format=export_format)
