# app.py - Main Flask application
from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import speech_recognition as sr
import google.generativeai as genai
from moviepy.editor import VideoFileClip
import tempfile

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500 MB max upload
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configure Google Gemini API
GOOGLE_API_KEY = "AIzaSyCut4dIvyAsuQx-_dZxDYk7jzRecodBl7o"  
genai.configure(api_key=GOOGLE_API_KEY)

# Configure allowed video extensions
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'wmv', 'mkv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_audio_from_video(video_path):
    """Extract audio from video and save as WAV file"""
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_audio:
        temp_audio_path = temp_audio.name
    
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(temp_audio_path, codec='pcm_s16le')
    return temp_audio_path

def transcribe_audio(audio_path):
    """Transcribe audio to text using speech_recognition"""
    recognizer = sr.Recognizer()
    
    # Process audio in chunks to handle large files
    full_transcript = ""
    with sr.AudioFile(audio_path) as source:
        # Detect duration and process in 30-second chunks
        audio_duration = source.DURATION
        chunk_size = 30  # seconds
        
        for i in range(0, int(audio_duration) + 1, chunk_size):
            try:
                audio = recognizer.record(source, duration=min(chunk_size, audio_duration - i))
                text = recognizer.recognize_google(audio)
                full_transcript += " " + text
            except sr.UnknownValueError:
                full_transcript += " [inaudible segment] "
            except Exception as e:
                print(f"Error transcribing chunk {i}-{i+chunk_size}: {e}")
    
    return full_transcript.strip()

def summarize_with_gemini(text):
    """Generate a summary using Google Gemini AI"""
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"""
    Please summarize the following lecture transcript. 
    Identify key concepts, main points, and important takeaways.
    Structure the summary with sections for:
    1. Main Topic Overview
    2. Key Concepts
    3. Important Details
    4. Conclusions
    
    Here is the transcript:
    {text}
    """
    
    response = model.generate_content(prompt)
    return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file provided'}), 400
    
    file = request.files['video']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        try:
            # Process video
            audio_path = extract_audio_from_video(file_path)
            transcript = transcribe_audio(audio_path)
            summary = summarize_with_gemini(transcript)
            
            # Clean up temporary files
            os.remove(audio_path)
            
            return jsonify({
                'success': True,
                'transcript': transcript,
                'summary': summary
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    app.run(debug=True)