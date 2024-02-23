from pytube import YouTube

def download_audio(url):
    try:
        yt = YouTube(url)
        audio_streams = yt.streams.filter(only_audio=True).order_by('abr').desc()
        if audio_streams:
            print("Qualidade de áudio disponível:")
            for i, stream in enumerate(audio_streams, start=1):
                print(f"{i}. {stream.abr} - {stream.mime_type}")

            choice = int(input("Escolha a qualidade de áudio (digite o número): "))
            chosen_stream = audio_streams[choice - 1]
            
            print(f"Baixando áudio na qualidade {chosen_stream.abr}...")
            chosen_stream.download(output_path='./audio/', filename_prefix='audio', filename=chosen_stream.default_filename.replace('mp4', 'mp3'))
            print("Download do áudio concluído.")
        else:
            print("Nenhum stream de áudio disponível para este vídeo.")
    except Exception as e:
        print(f"Erro ao baixar o áudio: {str(e)}")

def download_video(url):
    try:
        yt = YouTube(url)
        video_streams = yt.streams.filter(file_extension='mp4', progressive=True)
        
        if video_streams:
            video_streams = sorted(video_streams, key=lambda x: int(x.resolution[:-1]), reverse=True)
            # video_streams = yt.streams.filter(file_extension='mp4').order_by('resolution').desc()
            
            print("Qualidade de vídeo disponível:")
            for i, stream in enumerate(video_streams, start=1):
                print(f"{i}. {stream.resolution} - {stream.mime_type}")

            choice = int(input("Escolha a qualidade de vídeo (digite o número): "))
            chosen_stream = video_streams[choice - 1]
            
            print(f"Baixando vídeo na qualidade {chosen_stream.resolution}...")
            chosen_stream.download(output_path='./video/', filename_prefix='video')
            print("Download do vídeo concluído.")
        else:
            print("Nenhum stream de vídeo disponível para este vídeo.")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {str(e)}")

url = input("Digite a URL do vídeo: ")

download_type = input("Baixar áudio ou vídeo? Digite 'audio' ou 'video': ")

if download_type.lower() == 'audio':
    download_audio(url)
elif download_type.lower() == 'video':
    download_video(url)
else:
    print("Entrada inválida. Por favor, digite 'audio' ou 'video'.")
