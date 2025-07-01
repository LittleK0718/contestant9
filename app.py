from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def meow_counter():
    # Create file if it doesn't exist
    if not os.path.exists('/mnt/cat.txt'):
        with open('/mnt/cat.txt', 'w') as f:
            f.write('meow\n')
    else:
        # Append meow to existing file
        with open('/mnt/cat.txt', 'a') as f:
            f.write('meow\n')
    
    # Read and return all meows
    with open('/mnt/cat.txt', 'r') as f:
        meows = f.read()
    
    return meows

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
