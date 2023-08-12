# Python-Made-Gifs

## Usage
1. Customize the frames in the `frames/` directory to create your animation.
2. Run the GIF creation script: `python gif.py` after changing the necessary
3. Enjoy

## Features
- Create GIFs from individual frames, add music if you want.
- Adjust frame duration and order for custom animations.
- Support for various image formats (PNG, JPEG, etc.).
- Lightweight and easy-to-understand codebase.

## Examples
**Creating a GIF:**
```python
# In the GIF creation script import the necessary modules
from gif_utils import create_gif

# List of frames
put your frames in a single folder in an orderly manner, the script will do the rest

# Create a GIF
create_gif("frames-folder-name", music_file="music-file",speed="transition-speed")
