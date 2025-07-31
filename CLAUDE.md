# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Gemini Video Analyzer that provides video analysis capabilities using Google's Gemini API. The main script `test_youtube_video.py` supports both local video file analysis (recommended for production) and YouTube URL analysis (beta, unstable for Vietnamese content).

## Core Architecture

### Main Components

- **VideoAnalyzer Class**: Central class handling all video analysis operations
  - Supports 4 analysis types: `summary`, `transcript`, `topics`, `detailed`
  - Handles both local files and YouTube URLs
  - Auto-detects file size and chooses appropriate API method (inline data <20MB, File API >20MB)

- **File Processing Strategy**:
  - Files >20MB: Uses `genai.upload_file()` with processing wait loop
  - Files <20MB: Uses inline data with `mime_type: video/mp4`
  - Automatic processing status monitoring for large files

- **Command Structure**: 
  - `local` command for local video analysis (primary use case)
  - Legacy YouTube commands: `summarize`, `transcript`, `topics`, `quiz`, `question`, `timestamp`, `clip`, `all`

## Environment Setup

```bash
# Required environment setup
cp .env.example .env
# Edit .env with your GEMINI_API_KEY from https://aistudio.google.com/app/apikey

# Install dependencies
pip install -r requirements.txt
```

## Key Commands

### Production Video Analysis
```bash
# Primary local video analysis (recommended)
python3 test_youtube_video.py local "path/to/video.mp4" --analysis-type detailed
python3 test_youtube_video.py local "path/to/video.mp4" --analysis-type summary --sentences 5
python3 test_youtube_video.py local "path/to/video.mp4" --analysis-type transcript
python3 test_youtube_video.py local "path/to/video.mp4" --analysis-type topics

# Comprehensive analysis with output file
python3 test_youtube_video.py --video-file "examples/video.mp4" --output outputs/analysis.txt all
```

### Testing and Development
```bash
# Test with YouTube URLs (unstable, use for testing only)
python3 test_youtube_video.py summarize --sentences 3
python3 test_youtube_video.py transcript
python3 test_youtube_video.py topics

# Test specific features
python3 test_youtube_video.py question "Your question here"
python3 test_youtube_video.py timestamp "00:30"
python3 test_youtube_video.py clip "0:30" "1:00"
```

## Important Technical Details

### API Configuration
- **Default Model**: `gemini-2.5-flash` (cost-effective, recommended for production)
- **Alternative**: `gemini-2.5-pro` (higher quality, 15-20x more expensive)
- **Token Cost**: ~300 tokens/second for normal resolution, ~100 tokens/second for low resolution
- **Supported Formats**: MP4, MOV, AVI, WebM, WMV, 3GPP

### File Processing Logic
The system automatically handles large files with a processing wait mechanism:
```python
# For files >20MB, waits for processing completion
while uploaded_file.state.name == "PROCESSING":
    time.sleep(2)
    uploaded_file = genai.get_file(uploaded_file.name)
```

### Output Management
- All analysis results are saved to timestamped files by default
- Use `--output` parameter to specify custom output file paths
- Results include metadata: video source, analysis date, command used

## Cost Optimization

Based on `docs/gemini-video-cost-analysis.md`:

- **Startup Scale** (<1000 videos/month): Use Flash model with Summary analysis (~$10/month)
- **Production Scale** (1000-10000 videos/month): Mixed approach, Flash for bulk processing (~$100-500/month)
- **Enterprise Scale** (>10000 videos/month): Hybrid Flash/Pro approach (~$500-5000/month)

## Development Patterns

### Adding New Analysis Types
When adding new analysis types to the `local` command, update:
1. `analyze_local_video()` method prompt selection
2. Command line argument choices in `local_parser.add_argument()`
3. Analysis title mapping in the main execution logic

### Error Handling
The system includes comprehensive error handling for:
- Missing API keys with clear guidance
- File not found scenarios
- API processing failures
- Timeout handling for large file uploads

### Vietnamese Language Support
This system is optimized for Vietnamese content analysis. All prompts are in Vietnamese, and the system provides accurate results for Vietnamese audio and video content when using local file analysis.

## Production Deployment Considerations

### Environment Requirements
- Python 3.7+
- Stable internet connection for API calls
- Sufficient disk space for video processing (temporary files)
- API rate limiting considerations for high-volume usage

### Monitoring and Logging
The system outputs processing status including:
- File size detection and method selection
- Upload progress for large files
- Processing wait status with progress indicators
- Final analysis completion confirmation

### Security Notes
- API keys are loaded from environment variables only
- No API keys should be committed to the repository
- The `.gitignore` excludes `.env` files and output files
- Large video files are excluded from git tracking

## Directory Structure Context

- `docs/`: Contains comprehensive API documentation and cost analysis
- `examples/`: Sample videos for testing (git-ignored)
- `outputs/`: Analysis results (git-ignored)
- Root level contains core script and configuration files

## YouTube URL Limitations

YouTube URL analysis is currently unreliable, especially for Vietnamese content. The API is in beta and produces inconsistent results. For production use, always download videos locally first using tools like `yt-dlp` before analysis.