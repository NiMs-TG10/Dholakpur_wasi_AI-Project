# Dholakpur_wasi_AI Project

## Project Overview
This project is an AI-powered application that combines a machine learning model with a web interface and bot functionality. It consists of three main components working together to provide an integrated AI solution.

## Project Structure
```
.
├── AI_Model/           # Flask application and AI model
│   └── venv/          # Python virtual environment
├── Frontend+Bot/      # Web interface and bot components
│   └── node_modules/  # Node.js dependencies
└── spawner/          # Process management component
```

## Components

### AI Model
- Flask-based REST API
- Machine learning model implementation
- Handles AI processing and predictions

### Frontend + Bot
- Web interface for user interactions
- Bot implementation for automated tasks
- Built with Node.js

### Spawner
- Process management and coordination
- Handles component lifecycle

## Installation

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### Setting up the AI Model
1. Navigate to the AI_Model directory:
```bash
cd AI_Model
```
2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Setting up the Frontend and Bot
1. Navigate to the Frontend+Bot directory:
```bash
cd Frontend+Bot
```
2. Install Node.js dependencies:
```bash
npm install
```
3. Create a `.env` file with required environment variables:
```
OPENAI_API_KEY=your_api_key_here
```

### Setting up the Spawner
1. Navigate to the spawner directory:
```bash
cd spawner
```
2. Follow the setup instructions in the spawner's documentation

## Configuration
1. Configure the AI Model:
- Update configuration in `AI_Model/config.py`
- Set environment variables for API keys and secrets

2. Configure the Frontend:
- Update frontend settings in `Frontend+Bot/config.js`
- Configure bot settings as needed

3. Configure the Spawner:
- Adjust process management settings
- Set up logging and monitoring preferences

## Usage

### Starting the Application
1. Start the AI Model:
```bash
cd AI_Model
source venv/bin/activate
python app.py
```

2. Start the Frontend and Bot:
```bash
cd Frontend+Bot
npm start
```

3. Start the Spawner:
```bash
cd spawner
./start.sh
```

## Dependencies

### AI Model Dependencies
- Flask
- Python AI/ML libraries
- Additional requirements listed in `requirements.txt`

### Frontend + Bot Dependencies
- Node.js
- Express.js
- OpenAI API
- Additional npm packages listed in `package.json`

### Spawner Dependencies
- Process management libraries
- System-specific requirements

## Security Notes
- Never commit API keys or sensitive credentials
- Use environment variables for secrets
- Keep dependencies updated
- Follow security best practices for production deployment

## Contributing
Please read our contributing guidelines before submitting pull requests.

## License
[Add your license information here]
