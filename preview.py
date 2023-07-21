import os
from PIL import Image
from moviepy.editor import VideoFileClip


def generate_image_preview(image_path, preview_height=200):
    try:
        # Open the image
        image = Image.open(image_path)
        width_percent = (preview_height / float(image.size[1]))
        new_width = int((float(image.size[0]) * float(width_percent)))
        # Resize the image to the desired preview size
        preview_image = image.resize((new_width, preview_height))

        # Save the preview image
        preview_image.save(image_path+"__preview.jpg")
        print("Preview image generated successfully.")
    except Exception as e:
        print(f"Error generating preview image: {e}")


def generate_video_preview(video_path, preview_time=5, preview_size=(200, 200)):
    try:
        # Load the video clip
        clip = VideoFileClip(video_path)

        # Get a frame at the specified time (default: 5 seconds into the video)
        preview_frame = clip.get_frame(preview_time)

        # Convert the frame to a PIL image
        preview_image = Image.fromarray(preview_frame)

        # Resize the image to the desired preview size
        preview_image = preview_image.resize(preview_size)

        # Save the preview image
        preview_image.save(video_path+"__preview.jpg")
        print("Preview image generated successfully.")
    except Exception as e:
        print(f"Error generating preview image: {e}")
# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# target = os.path.join(APP_ROOT, 'files/')
# filelist = os.listdir(target)
# for file in filelist:
#     # generate_image_preview(os.path.join(target, file))
#     if file.endswith(".mp4"):
#         generate_video_preview(os.path.join(target, file))