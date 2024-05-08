import cv2

def capture_frame(video_path, frame_number, output_folder="output_images"):
  """
  Captures a specific frame from a video and saves it with the video name.

  Args:
      video_path (str): Path to the video file (e.g., "cute_girl.mp4").
      frame_number (int): The frame number to capture (0-based indexing).
      output_folder (str, optional): Folder to save the captured image. Defaults to "output_images".
  """

  # Create the output folder if it doesn't exist
  import os
  if not os.path.exists(output_folder):
    os.makedirs(output_folder)

  # Open the video capture object
  cap = cv2.VideoCapture(video_path)

  # Check if video opened successfully
  if not cap.isOpened():
    print("Error opening video!")
    return

  # Seek to the desired frame
  success, image = cap.read()
  frame_count = 0
  while success and frame_count < frame_number:
    success, image = cap.read()
    frame_count += 1

  # Check if frame was read successfully
  if not success:
    print(f"Error: Frame number {frame_number} not found in the video!")
    cap.release()
    return

  # Extract video name without extension
  video_name, _ = os.path.splitext(os.path.basename(video_path))

  # Generate output image filename
  output_filename = os.path.join(output_folder, f"{video_name}.jpg")

  # Save the captured image
  cv2.imwrite(output_filename, image)
  print(f"Frame {frame_number} captured and saved as: {output_filename}")

  # Release the video capture object
  cap.release()

# Example usage
video_path = "cute_girl.mp4"
frame_number = 5
capture_frame(video_path, frame_number)
