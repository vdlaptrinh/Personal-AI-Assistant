import yt_dlp
import subprocess
import time
import os
from pydub import AudioSegment
from src.text_to_speech import text_to_speech

def download_and_play_m3u8(song_name):
    # Tìm kiếm bài hát trên YouTube
    search_query = f"ytsearch:{song_name}"
    
    # Cấu hình yt-dlp để lấy âm thanh tốt nhất
    ydl_opts = {
        'format': 'bestaudio/best',  # Chọn định dạng âm thanh tốt nhất
        'noplaylist': True,  # Không tải playlist
        'quiet': True,  # Không in ra quá nhiều thông tin
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        }
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Tìm kiếm video và trích xuất thông tin
        try:
            info = ydl.extract_info(search_query, download=False)
            
            # Kiểm tra nếu có video trong 'entries'
            if 'entries' in info and len(info['entries']) > 0:
                video_info = info['entries'][0]
                
                # Lọc các định dạng âm thanh (không phải video)
                audio_formats = [f for f in video_info['formats'] if 'audio' in f['format']]
                
                # Kiểm tra nếu có định dạng âm thanh
                if audio_formats:
                    # Chọn URL của định dạng âm thanh tốt nhất
                    audio_url = audio_formats[0]['url']
                    #print(f"Tìm thấy video: {video_info['title']} - Tải xuống từ URL: {audio_url}")
                    print(f"Tìm thấy video: {video_info['title']}")
                else:
                    print("Không tìm thấy định dạng âm thanh cho video này.")
                    return
            else:
                print("Không tìm thấy video nào trong kết quả tìm kiếm.")
                return
        except Exception as e:
            print(f"Lỗi khi trích xuất thông tin: {e}")
            return

    # Tải các phân đoạn của .m3u8
    print("Đang tải và phát bài hát...")
    text_to_speech("Vui lòng chờ tôi 1 tý nhé","vi","output_file")

    # Sử dụng ffmpeg để tải tệp m3u8 và phát trực tiếp
    output_file = 'output_audio'
    try:
        subprocess.run([
            'ffmpeg', '-i', audio_url, '-vn', '-acodec', 'libmp3lame', '-f', 'mp3', output_file,
            '-loglevel', 'quiet', '-y'
        ], check=True)

        # Sau khi tải xong, phát âm thanh
        print("Đã tải xong, đang phát bài hát...")
        
        sound = AudioSegment.from_mp3(output_file)  # convert MP3 to WAV
        sound.export(f"{output_file}.wav", format="wav")
        os.remove(output_file)
        print(f"Saved TTS output to {output_file}")
        subprocess.call(["aplay", "output_audio.wav"])
        #subprocess.call(['ffmpeg', output_file])  # Phát âm thanh bằng mpg123

    except Exception as e:
        print(f"Lỗi khi tải và phát âm thanh: {e}")

    # Xóa tệp sau khi phát xong
    #if os.path.exists(output_file):
        #os.remove(output_file)
        #print("Đã xóa tệp âm thanh sau khi phát xong.")

if __name__ == "__main__":
    song_name = input("Nhập tên bài hát: ")
    download_and_play_m3u8(song_name)
