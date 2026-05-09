import os
import sys

# Reconfigure stdout to handle emojis in filenames
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Try to import moviepy, if not found, prompt to install
try:
    # MoviePy 2.x style
    from moviepy import VideoFileClip
except ImportError:
    try:
        # Legacy style
        from moviepy.editor import VideoFileClip
    except ImportError as e:
        print(f"Error: {e}")
        print("Please install it using: pip install moviepy")
        sys.exit(1)

def convert_gif_to_webm(input_path, output_path):
    print(f"Loading: {input_path}")
    try:
        # Load the GIF
        clip = VideoFileClip(input_path)
        
        print(f"Converting and compressing to WebM... (Targeting high efficiency)")
        # WebM with high compression
        # bitrate='1000k' is usually plenty for web assets
        clip.write_videofile(output_path, codec='libvpx-vp9', bitrate='1000k', audio=False)
        
        print(f"Successfully converted to: {output_path}")
        original_size = os.path.getsize(input_path) / (1024 * 1024)
        new_size = os.path.getsize(output_path) / (1024 * 1024)
        
        print(f"Original size: {original_size:.2f} MB")
        print(f"Optimized size: {new_size:.2f} MB")
        print(f"Reduction: {((original_size - new_size) / original_size) * 100:.2f}%")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define paths
    assets_dir = os.path.join("public", "assets")
    
    # Target the giant GIF
    input_gif = os.path.join(assets_dir, "From KlickPin CF Timeless sweet text ideas with charm and ideas for thoughtful sharing that feel deeply personal ✨ - Pin-2181499816349440.gif")
    output_webm = os.path.join(assets_dir, "capabilities_engine.webm")
    
    if os.path.exists(input_gif):
        convert_gif_to_webm(input_gif, output_webm)
    else:
        print(f"Could not find input file: {input_gif}")
        # List files in assets to help debug
        print("Available assets:")
        for f in os.listdir(assets_dir):
            print(f" - {f}")
