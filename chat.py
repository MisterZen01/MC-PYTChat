import os
import pytchat
import minescript

# Set environment variable for the home directory
if os.name == 'nt':
    os.environ['USERPROFILE'] = os.getenv('USERPROFILE', 'C:\\Users\\Default')
else:
    os.environ['HOME'] = os.getenv('HOME', '/home/default')

# Function to fetch and process chat messages
def fetch_youtube_chat(video_id):
    try:
        minescript.echo("Starting YouTube Chat...")
        chat = pytchat.create(video_id=video_id)
        while chat.is_alive():
            for c in chat.get().sync_items():
                
                # Check if the message does not start with "!"
                if not c.message.startswith("!"):
                    minescript.echo(f"[{c.author.name}] {c.message}")

    except Exception as e:
        minescript.echo(f"An error occurred: {e}")

def main():
    video_id = "qGGrQaWRiuM"  # Replace with your YouTube live video ID
    fetch_youtube_chat(video_id)
    minescript.echo("Finished fetching chat.")

if __name__ == "__main__":
    main()
