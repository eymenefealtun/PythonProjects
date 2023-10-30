from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("SampleVideo.mp4")

videoClip.write_gif("SampleResultGif.gif")
