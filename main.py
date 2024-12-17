"""
Anaglyph 3D Video Converter with Color Blindness Adjustments

Description:
This script processes an input video to create an anaglyph 3D movie. It supports adjustments for different types of color blindness, including:
  - Standard vision
  - Protanopia (red-blind)
  - Deuteranopia (green-blind)
  - Tritanopia (blue-blind)

The script ensures that the output video includes the original audio using FFmpeg. It first generates a temporary video without audio and then merges the original audio back into the final output.

Requirements:
- Python packages: cv2 (OpenCV), numpy, subprocess, os
- FFmpeg installed and accessible via the command line.

Usage:
1. Install the required libraries:
   - OpenCV: `pip install opencv-python`
   - NumPy: `pip install numpy`
2. Ensure FFmpeg is installed and available in your PATH.
3. Replace the `input_video` variable with the path to your video file.
4. Choose a color blindness type from: "standard", "protanopia", "deuteranopia", or "tritanopia".
5. Run the script. The output video will be saved in the same directory as the input, with the format:
   `<original_name>_<colorblindness_type>.mp4`

Example:
To convert `test_video.mp4` for deuteranopia:
- Set `input_video = "test_video.mp4"`
- Set `colorblindness_type = "deuteranopia"`
- Run the script. The output will be `test_video_deuteranopia.mp4`.
"""


import cv2
import numpy as np
import os
import subprocess  # For calling FFmpeg

def convert_to_anaglyph_with_colorblindness(video_path, colorblindness_type="standard"):
    """
    Convert a video into an anaglyph 3D movie with adjustments for different types of color blindness.
    Includes audio in the output by merging with FFmpeg.
    
    Parameters:
        video_path (str): Path to the input video file.
        colorblindness_type (str): Type of color blindness ("standard", "protanopia", "deuteranopia", "tritanopia").
    """
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return
    
    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if frame_width == 0 or frame_height == 0 or fps == 0:
        print("Error: Video properties could not be read.")
        cap.release()
        return
    
    print(f"Video Properties - Width: {frame_width}, Height: {frame_height}, FPS: {fps}, Total Frames: {total_frames}")
    
    # Generate output file name for video
    base_name, ext = os.path.splitext(os.path.basename(video_path))
    output_video_name = f"{base_name}_{colorblindness_type}_video.avi"  # Temporary file for video without audio
    final_output_name = f"{base_name}_{colorblindness_type}.mp4"  # Final file with audio
    output_path = os.path.join(os.path.dirname(video_path), output_video_name)
    final_output_path = os.path.join(os.path.dirname(video_path), final_output_name)
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Use MJPG codec for AVI
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    
    print(f"Processing video for {colorblindness_type}...")
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("No more frames to read.")
            break

        # Create left and right perspectives by shifting slightly
        left_eye = np.roll(frame, -10, axis=1)  # Shift left
        right_eye = np.roll(frame, 10, axis=1)  # Shift right

        # Adjust the anaglyph based on the color blindness type
        anaglyph_frame = np.zeros_like(frame)
        
        if colorblindness_type == "standard":
            anaglyph_frame[:, :, 2] = left_eye[:, :, 2]  # Red channel
            anaglyph_frame[:, :, 0:2] = right_eye[:, :, 0:2]  # Cyan channel
        
        elif colorblindness_type == "protanopia":
            gray_left = cv2.cvtColor(left_eye, cv2.COLOR_BGR2GRAY)
            anaglyph_frame[:, :, 2] = gray_left
            anaglyph_frame[:, :, 0:2] = right_eye[:, :, 0:2]
        
        elif colorblindness_type == "deuteranopia":
            anaglyph_frame[:, :, 2] = left_eye[:, :, 2]
            anaglyph_frame[:, :, 1] = 0
            anaglyph_frame[:, :, 0] = right_eye[:, :, 0]
        
        elif colorblindness_type == "tritanopia":
            anaglyph_frame[:, :, 2] = left_eye[:, :, 2]
            anaglyph_frame[:, :, 1] = right_eye[:, :, 1]
            anaglyph_frame[:, :, 0] = 0

        # Write the frame to the output video
        out.write(anaglyph_frame)

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    
    print("Anaglyph video processing complete. Adding audio...")
    
    # Use FFmpeg to add audio
    try:
        ffmpeg_command = [
            "ffmpeg", "-y",
            "-i", output_path,  # Input video without audio
            "-i", video_path,  # Input original video with audio
            "-c:v", "copy",  # Copy video codec to avoid re-encoding
            "-c:a", "aac",  # Use AAC for audio encoding
            "-map", "0:v:0", "-map", "1:a:0",  # Map video from the first input and audio from the second
            final_output_path
        ]
        subprocess.run(ffmpeg_command, check=True)
        print(f"Final video with audio saved at: {final_output_path}")
    except subprocess.CalledProcessError as e:
        print("Error during FFmpeg processing:", e)
    finally:
        # Clean up the temporary video file
        if os.path.exists(output_path):
            os.remove(output_path)

# Example usage
input_video = "test_video.mp4"  # Replace with your input video file path

# Modify the colorblindness_type parameter for different modes
colorblindness_type = "deuteranopia"  # Choose from "standard", "protanopia", "deuteranopia", "tritanopia"

convert_to_anaglyph_with_colorblindness(input_video, colorblindness_type)
