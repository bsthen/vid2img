import subprocess
import os

def capture_images(video_path, num_images, output_quality='1'):
    # Get video filename without extension
    video_filename = os.path.splitext(os.path.basename(video_path))[0]

    # Create output directory using video filename
    output_dir = f'{video_filename}_images'
    os.makedirs(output_dir, exist_ok=True)

    # Calculate time intervals to extract frames
    duration = get_video_duration(video_path)
    interval = duration / (num_images + 1)

    # Generate image filenames
    image_filenames = [os.path.join(output_dir, f'image_{i}.jpg') for i in range(num_images)]

    # Execute FFmpeg command to capture images
    for i, filename in enumerate(image_filenames):
        time_point = interval * (i + 1)
        subprocess.run(['ffmpeg', '-i', video_path, '-ss', str(time_point), '-vframes', '1', '-q:v', output_quality, filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print(f"{num_images} images captured and saved in '{output_dir}' directory.")

def get_video_duration(video_path):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', video_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    duration = float(result.stdout)
    return duration

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python3 vid2img.py <video_path> <num_images>")
        sys.exit(1)

    video_path = sys.argv[1]
    num_images = int(sys.argv[2])

    capture_images(video_path, num_images)
