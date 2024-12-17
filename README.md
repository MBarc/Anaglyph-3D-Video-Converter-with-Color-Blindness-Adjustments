# Anaglyph 3D Video Converter with Color Blindness Adjustments
This Python script converts a video into an **anaglyph 3D movie** while offering adjustments for different types of color blindness. It also retains the original audio in the output video using FFmpeg.

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
  - Normal vision
  - Protanopia (red-blind)
  - Deuteranopia (green-blind)
  - Tritanopia (blue-blind)
- Audio Retention: Merges the original video audio into the final output seamlessly using FFmpeg.
- Customizable Output: Saves the processed video with a filename that includes the original name and the selected color blindness type.
- Frame-by-Frame Processing: Utilizes OpenCV to process video frames efficiently.
- User-Friendly Output: Produces *.mp4* files for compatibility with most media players.
