<p align="center">
  <img src="logo.png" alt="Project Logo" width="300"/>
</p>

<h1 align="center">Anaglyph 3D Video Converter with Color Blindness Adjustments</h1>

## Table of Contents

1. [Description](#description)  
2. [Features](#features)  
3. [Requirements](#requirements)  
4. [How It Works](#how-it-works)  
5. [License](#license)  


# Description
This project is a Python-based Anaglyph 3D Video Converter designed to create 3D movies with support for color blindness adjustments. It processes a video file frame-by-frame to generate a stereoscopic effect by creating separate perspectives for the left and right eyes.

In addition to standard 3D effects for normal vision, the converter provides tailored adjustments for different types of color blindness:
- Protanopia (red-blind)
- Deuteranopia (green-blind)
- Tritanopia (blue-blind)
  
The output video includes the original audio track, achieved by seamlessly merging it using FFmpeg. Whether you're experimenting with 3D effects or making 3D content accessible for those with color vision deficiencies, this tool offers a customizable and easy-to-use solution.

# Features
- Anaglyph 3D Conversion: Transforms videos into stereoscopic 3D format by creating left and right eye perspectives.
- Color Blindness Support: Provides tailored adjustments for:
  - Standard vision
  - Protanopia (red-blind)
  - Deuteranopia (green-blind)
  - Tritanopia (blue-blind)
- Audio Retention: Merges the original video audio into the final output seamlessly using FFmpeg.
- Customizable Output: Saves the processed video with a filename that includes the original name and the selected color blindness type.
- Frame-by-Frame Processing: Utilizes OpenCV to process video frames efficiently.
- User-Friendly Output: Produces *.mp4* files for compatibility with most media players.

# Requirements
To run this project, you’ll need the following:

## Python
Python 3.6 or higher.

## Python Libraries
Install the required Python libraries using the requirements.txt file:
```bash 
pip install -r requirements.txt
```
The required libraries are:
- OpenCV (opencv-python): For video processing.
- NumPy: For numerical operations and frame manipulation.

## FFmpeg
FFmpeg is required for merging the audio from the original video into the output.
Install FFmpeg from ffmpeg.org or using a package manager:
- On macOS: brew install ffmpeg
- On Ubuntu/Debian: sudo apt install ffmpeg
- On Windows: [Download](https://www.ffmpeg.org/download.html) the executable and add it to your system's PATH.

## System Requirements
- A computer with sufficient memory and processing power to handle video processing.
- Compatible operating systems: Windows, macOS, or Linux.

# How It Works
This script processes a video file to create an anaglyph 3D movie, with optional adjustments for different types of color blindness. Here’s a step-by-step breakdown:
1. Video Input:
  - The script reads the input video frame-by-frame using OpenCV.
  - It extracts the width, height, frames per second (FPS), and total number of frames to ensure smooth processing.
2. Creating 3D Perspectives:
  - For each frame, the script shifts the image slightly to simulate separate perspectives for the left and right eyes:
    - Left Eye: A left-shifted version of the frame.
    - Right Eye: A right-shifted version of the frame.
3. Anaglyph Generation:
  - The script combines the left and right eye perspectives into a single frame, adjusting the colors based on the selected mode:
    - Standard: Red and cyan channels are merged for standard 3D effects.
    - Protanopia (red-blind): Converts the red channel to grayscale for better visualization.
    - Deuteranopia (green-blind): Reduces the green channel to simulate adjustments for green-blind users.
    - Tritanopia (blue-blind): Adjusts blue and green channels for blue-blind users.
4. Video Output Without Audio:
  - The processed frames are written to a temporary .avi file using OpenCV.
5. Audio Merging:
  - The script uses FFmpeg to add the original video’s audio track to the processed video.
  - The final output is saved as an .mp4 file for better compatibility with most media players.
6. Output File Naming:
  - The output file name includes the original file name and the selected color blindness type, e.g., example_video_deuteranopia.mp4.

This process ensures the output video maintains the original audio and provides a visually optimized 3D effect tailored to the viewer’s needs.

# How To Use
1. Put your .mp4 file in the same directory as the script.
2. Change the name of the file to be "input_video.mp4".
   - Optionally, you could instead change the value of the "input_video" variable to match the name of your .mp4 file.
3. Within the script, change the value of "colorblindness_type" to your target type.
4. Run the script. 

# License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this software in accordance with the terms of the license.
See the LICENSE file for detailed license information.
