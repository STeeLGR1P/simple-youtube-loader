from pytube import YouTube


def download_video(url, output_path="."):
    try:
        def on_progress(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage = (bytes_downloaded / total_size) * 100
            print(f"Загружено: {percentage:.2f}%")

        yt = YouTube(url, on_progress_callback=on_progress)

        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        for i, stream in enumerate(streams):
            print(f"{i + 1}. {stream.resolution}")
        choice = int(input("Выберите качество (введите номер): ")) - 1
        selected_stream = streams[choice]
        selected_stream.download(output_path)

        print(f"Загрузка видео: {yt.title}...")
        stream.download(output_path)
        print("Загрузка завершена!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    video_url = input("Введите URL YouTube видео: ")

    save_path = input("Введите путь для сохранения (оставьте пустым для текущей директории): ") or "."

    download_video(video_url, save_path)


