def replace_audio_in_video(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    final_video = video_clip.set_audio(audio_clip)
    final_video.write_videofile(output_path, audio_codec='aac')
