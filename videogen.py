import sys
import ast
import moviepy.audio.io.AudioFileClip
import moviepy.video.compositing.CompositeVideoClip
import moviepy.video.VideoClip

def generate_word_video(words, word_duration, beep_duration, output_filename, beep_path):
    clips = []
    video_size = (1280, 720)
    bg_color = (0, 0, 0)

    # Correct reference to AudioFileClip
    beep = moviepy.audio.io.AudioFileClip.AudioFileClip(beep_path)
    
    plus_clip = moviepy.video.VideoClip.TextClip(
                    text="+", font_size=100, color='white', size=video_size, method='label', duration=beep_duration, text_align='center', font="C:\\Windows\\Fonts\\arial.ttf"
                ).with_audio(beep)
    clips.append(plus_clip)
    
    for i, word in enumerate(words):
        # Word display
        word_clip = moviepy.video.VideoClip.TextClip(
            text=word, font_size=80, color='white', size=video_size, method='label', duration=word_duration, text_align='center', font="C:\\Windows\\Fonts\\arial.ttf"
        )
        clips.append(word_clip)

        # Beep and plus display
        
    
    
    # Combine all clips
    final = moviepy.video.compositing.CompositeVideoClip.concatenate_videoclips(clips=clips, bg_color=bg_color, transition=plus_clip, method='compose')
    final.write_videofile(output_filename, fps=24, audio_codec='aac')


# Get inputs from command-line arguments
wordDuration = int(sys.argv[1])
beepDuration = int(sys.argv[2])
filename = sys.argv[3]
beep = sys.argv[4]
wordList = ast.literal_eval(input("WordList: "))

generate_word_video(
    words=wordList,
    word_duration=wordDuration,
    beep_duration=beepDuration,
    output_filename=filename,
    beep_path=beep
)
