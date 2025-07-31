#!/usr/bin/env python3
"""
Test script for YouTube video analysis using Gemini API
Video: https://www.youtube.com/watch?v=_6_iwocubu0
"""

import os
import sys
import google.generativeai as genai
import argparse
from datetime import datetime
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class VideoAnalyzer:
    def __init__(self, api_key=None):
        """Initialize the Gemini client"""
        # Priority: command line arg > env variable > default
        if not api_key:
            api_key = os.getenv('GEMINI_API_KEY')
        
        if not api_key:
            raise ValueError("API key required. Set GEMINI_API_KEY in .env or pass via --api-key")
            
        genai.configure(api_key=api_key)
        self.model_name = os.getenv('GEMINI_MODEL', 'gemini-2.5-flash')
        
    def summarize_video(self, video_url, sentences=3):
        """Summarize the video in specified number of sentences"""
        print(f"\n🎥 Summarizing video in {sentences} sentences...")
        
        model = genai.GenerativeModel(self.model_name)
        prompt = f'Hãy tóm tắt video YouTube này bằng tiếng Việt trong {sentences} câu: {video_url}'
        
        response = model.generate_content(prompt)
        return response.text
    
    def generate_transcript(self, video_url, with_timestamps=True):
        """Generate transcript of the video"""
        print("\n📝 Generating transcript...")
        
        model = genai.GenerativeModel(self.model_name)
        prompt = f"Hãy phiên âm nội dung tiếng Việt từ video YouTube này: {video_url}"
        if with_timestamps:
            prompt += " Vui lòng bao gồm dấu thời gian cho các sự kiện quan trọng và mô tả hình ảnh."
        
        response = model.generate_content(prompt)
        return response.text
    
    def create_quiz(self, video_url, num_questions=5):
        """Create a quiz based on video content"""
        print(f"\n📋 Creating quiz with {num_questions} questions...")
        
        model = genai.GenerativeModel(self.model_name)
        prompt = f'''Tạo một bài kiểm tra với {num_questions} câu hỏi và đáp án dựa trên video YouTube này: {video_url}
        
Định dạng kết quả như sau:
CÂU HỎI:
1. [Câu hỏi]
2. [Câu hỏi]
...

ĐÁP ÁN:
1. [Đáp án]
2. [Đáp án]
...'''
        
        response = model.generate_content(prompt)
        return response.text
    
    def analyze_timestamp(self, video_url, timestamp):
        """Analyze specific timestamp in the video"""
        print(f"\n⏰ Analyzing timestamp {timestamp}...")
        
        model = genai.GenerativeModel(self.model_name)
        prompt = f'Điều gì đang xảy ra tại thời điểm {timestamp} trong video YouTube này: {video_url}? Vui lòng mô tả cả nội dung hình ảnh và âm thanh bằng tiếng Việt.'
        
        response = model.generate_content(prompt)
        return response.text
    
    def extract_key_topics(self, video_url):
        """Extract key topics discussed in the video"""
        print("\n🔑 Extracting key topics...")
        
        model = genai.GenerativeModel(self.model_name)
        prompt = f'Liệt kê các chủ đề và khái niệm chính được thảo luận trong video YouTube này: {video_url}. Trình bày dưới dạng danh sách với giải thích ngắn gọn bằng tiếng Việt.'
        
        response = model.generate_content(prompt)
        return response.text
    
    def answer_question(self, video_url, question):
        """Answer a specific question about the video"""
        print(f"\n❓ Answering question: {question}")
        
        model = genai.GenerativeModel(self.model_name)
        prompt = f'Dựa trên video YouTube này: {video_url}\n\nCâu hỏi: {question}\nVui lòng trả lời bằng tiếng Việt.'
        
        response = model.generate_content(prompt)
        return response.text
    
    def analyze_video_with_clip(self, video_url, start_time, end_time):
        """Analyze a specific clip of the video"""
        print(f"\n🎬 Analyzing clip from {start_time} to {end_time}...")
        
        model = genai.GenerativeModel(self.model_name)
        prompt = f'Vui lòng phân tích đoạn từ {start_time} đến {end_time} trong video YouTube này: {video_url}. Những điểm chính được thảo luận là gì? Trả lời bằng tiếng Việt.'
        
        response = model.generate_content(prompt)
        return response.text

    def analyze_local_video(self, video_path, analysis_type="summary", sentences=3):
        """Analyze local video file using Gemini API"""
        print(f"\n🎥 Analyzing local video: {os.path.basename(video_path)}")
        
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")
        
        # Get file size to determine upload method
        file_size = os.path.getsize(video_path)
        file_size_mb = file_size / (1024 * 1024)
        
        model = genai.GenerativeModel(self.model_name)
        
        # Choose prompt based on analysis type
        if analysis_type == "summary":
            prompt = f"Hãy tóm tắt video này bằng tiếng Việt trong {sentences} câu. Mô tả nội dung chính, các hoạt động và thông tin quan trọng."
        elif analysis_type == "transcript":
            prompt = "Hãy tạo phiên bản văn bản (transcript) chi tiết của video này bằng tiếng Việt, bao gồm cả mô tả hình ảnh và âm thanh."
        elif analysis_type == "topics":
            prompt = "Liệt kê các chủ đề và khái niệm chính trong video này. Trình bày dưới dạng danh sách với giải thích ngắn gọn bằng tiếng Việt."
        elif analysis_type == "detailed":
            prompt = "Hãy phân tích chi tiết video này bằng tiếng Việt, bao gồm: nội dung chính, các bước/hành động, công cụ được sử dụng, và mục đích của video."
        else:
            prompt = "Hãy phân tích và mô tả nội dung của video này bằng tiếng Việt."
        
        try:
            if file_size_mb > 20:
                # Use File API for large files
                print(f"📁 Uploading large file ({file_size_mb:.1f}MB) using File API...")
                uploaded_file = genai.upload_file(video_path)
                
                # Wait for the file to be processed
                import time
                print("⏳ Waiting for file to be processed...")
                while uploaded_file.state.name == "PROCESSING":
                    print(".", end="", flush=True)
                    time.sleep(2)
                    uploaded_file = genai.get_file(uploaded_file.name)
                
                if uploaded_file.state.name == "FAILED":
                    raise Exception("File processing failed")
                
                print("\n✅ File ready for analysis")
                response = model.generate_content([uploaded_file, prompt])
            else:
                # Use inline data for smaller files
                print(f"📁 Processing file ({file_size_mb:.1f}MB) using inline data...")
                with open(video_path, 'rb') as video_file:
                    video_data = video_file.read()
                
                response = model.generate_content([
                    {
                        "mime_type": "video/mp4",
                        "data": video_data
                    },
                    prompt
                ])
            
            return response.text
            
        except Exception as e:
            raise Exception(f"Error analyzing video: {str(e)}")

def save_to_file(content, filename):
    """Save content to a text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\n💾 Saved to: {filename}")

def main():
    parser = argparse.ArgumentParser(description='Video analysis with Gemini API (YouTube URLs and local files)')
    parser.add_argument('--api-key', help='Gemini API key (optional if set in environment)')
    
    # Use environment variable for default URL if available
    default_url = os.getenv('DEFAULT_VIDEO_URL', 'https://www.youtube.com/watch?v=_6_iwocubu0')
    parser.add_argument('--video-url', default=default_url, 
                        help='YouTube video URL to analyze')
    parser.add_argument('--video-file', help='Local video file path to analyze')
    parser.add_argument('--output', help='Output filename (default: video_analysis_<timestamp>.txt)')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Summarize command
    summary_parser = subparsers.add_parser('summarize', help='Summarize the video')
    summary_parser.add_argument('--sentences', type=int, default=3, help='Number of sentences for summary')
    
    # Transcript command
    transcript_parser = subparsers.add_parser('transcript', help='Generate transcript')
    transcript_parser.add_argument('--no-timestamps', action='store_true', help='Generate transcript without timestamps')
    
    # Quiz command
    quiz_parser = subparsers.add_parser('quiz', help='Create a quiz from video content')
    quiz_parser.add_argument('--questions', type=int, default=5, help='Number of quiz questions')
    
    # Timestamp command
    timestamp_parser = subparsers.add_parser('timestamp', help='Analyze specific timestamp')
    timestamp_parser.add_argument('time', help='Timestamp to analyze (format: MM:SS)')
    
    # Topics command
    subparsers.add_parser('topics', help='Extract key topics from video')
    
    # Question command
    question_parser = subparsers.add_parser('question', help='Ask a question about the video')
    question_parser.add_argument('query', help='Your question about the video')
    
    # Clip command
    clip_parser = subparsers.add_parser('clip', help='Analyze a video clip')
    clip_parser.add_argument('start', help='Start time (e.g., 30s, 1m30s)')
    clip_parser.add_argument('end', help='End time (e.g., 60s, 2m)')
    
    # All command
    subparsers.add_parser('all', help='Run all analysis options')
    
    # Local video command
    local_parser = subparsers.add_parser('local', help='Analyze local video file')
    local_parser.add_argument('video_path', help='Path to local video file')
    local_parser.add_argument('--analysis-type', choices=['summary', 'transcript', 'topics', 'detailed'], 
                             default='summary', help='Type of analysis to perform')
    local_parser.add_argument('--sentences', type=int, default=3, 
                             help='Number of sentences for summary (only for summary type)')
    
    args = parser.parse_args()
    
    if not args.command:
        print("❌ Please specify a command. Use --help to see available options.")
        sys.exit(1)
    
    try:
        analyzer = VideoAnalyzer(api_key=args.api_key)
        
        # Determine if we're analyzing YouTube URL or local file
        if args.command == 'local':
            video_source = args.video_path
            print(f"🎥 Analyzing local video: {os.path.basename(video_source)}")
        else:
            video_source = args.video_file if args.video_file else args.video_url
            if args.video_file:
                print(f"🎥 Analyzing local video: {os.path.basename(video_source)}")
            else:
                print(f"🎥 Analyzing YouTube video: {video_source}")
        
        print("=" * 80)
        
        # Prepare output filename
        if args.output:
            output_filename = args.output
        else:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"video_analysis_{timestamp}.txt"
        
        # Content accumulator
        video_type = "Local Video" if (args.command == 'local' or args.video_file) else "YouTube Video"
        full_content = f"{video_type} Analysis\n{'='*50}\n"
        full_content += f"Video Source: {video_source}\n"
        full_content += f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        full_content += f"Command: {args.command}\n"
        full_content += "="*50 + "\n\n"
        
        if args.command == 'local':
            result = analyzer.analyze_local_video(video_source, args.analysis_type, args.sentences)
            analysis_title = {
                'summary': '📄 Summary',
                'transcript': '📝 Transcript', 
                'topics': '🔑 Key Topics',
                'detailed': '🔍 Detailed Analysis'
            }.get(args.analysis_type, '📄 Analysis')
            
            print(f"\n{analysis_title}:")
            print(result)
            full_content += f"{args.analysis_type.upper()}:\n" + "-"*30 + "\n" + result + "\n"
            
        elif args.command == 'summarize':
            if args.video_file:
                result = analyzer.analyze_local_video(video_source, "summary", args.sentences)
            else:
                result = analyzer.summarize_video(video_source, args.sentences)
            print("\n📄 Summary:")
            print(result)
            full_content += "SUMMARY:\n" + "-"*30 + "\n" + result + "\n"
            
        elif args.command == 'transcript':
            if args.video_file:
                result = analyzer.analyze_local_video(video_source, "transcript")
            else:
                result = analyzer.generate_transcript(video_source, not args.no_timestamps)
            print("\n📝 Transcript:")
            print(result)
            full_content += "TRANSCRIPT:\n" + "-"*30 + "\n" + result + "\n"
            
        elif args.command == 'quiz':
            if args.video_file:
                result = analyzer.analyze_local_video(video_source, "detailed")
                result += "\n\n" + analyzer.create_quiz(video_source, args.questions)
            else:
                result = analyzer.create_quiz(video_source, args.questions)
            print("\n📋 Quiz:")
            print(result)
            full_content += "QUIZ:\n" + "-"*30 + "\n" + result + "\n"
            
        elif args.command == 'timestamp':
            result = analyzer.analyze_timestamp(video_source, args.time)
            print(f"\n⏰ Analysis at {args.time}:")
            print(result)
            full_content += f"TIMESTAMP ANALYSIS ({args.time}):\n" + "-"*30 + "\n" + result + "\n"
            
        elif args.command == 'topics':
            if args.video_file:
                result = analyzer.analyze_local_video(video_source, "topics")
            else:
                result = analyzer.extract_key_topics(video_source)
            print("\n🔑 Key Topics:")
            print(result)
            full_content += "KEY TOPICS:\n" + "-"*30 + "\n" + result + "\n"
            
        elif args.command == 'question':
            result = analyzer.answer_question(video_source, args.query)
            print("\n💡 Answer:")
            print(result)
            full_content += f"QUESTION: {args.query}\n" + "-"*30 + "\n" + result + "\n"
            
        elif args.command == 'clip':
            result = analyzer.analyze_video_with_clip(video_source, args.start, args.end)
            print(f"\n🎬 Clip Analysis ({args.start} - {args.end}):")
            print(result)
            full_content += f"CLIP ANALYSIS ({args.start} - {args.end}):\n" + "-"*30 + "\n" + result + "\n"
            
        elif args.command == 'all':
            # Run all analysis options
            print("\n🔄 Running all analysis options...\n")
            
            if args.video_file:
                # For local videos, run comprehensive analysis
                # Summary
                print("1️⃣ VIDEO SUMMARY")
                print("-" * 40)
                summary = analyzer.analyze_local_video(video_source, "summary", 5)
                print(summary)
                full_content += "1. VIDEO SUMMARY:\n" + "-"*30 + "\n" + summary + "\n\n"
                
                # Key Topics
                print("\n2️⃣ KEY TOPICS") 
                print("-" * 40)
                topics = analyzer.analyze_local_video(video_source, "topics")
                print(topics)
                full_content += "2. KEY TOPICS:\n" + "-"*30 + "\n" + topics + "\n\n"
                
                # Detailed Analysis
                print("\n3️⃣ DETAILED ANALYSIS")
                print("-" * 40)
                detailed = analyzer.analyze_local_video(video_source, "detailed")
                print(detailed)
                full_content += "3. DETAILED ANALYSIS:\n" + "-"*30 + "\n" + detailed + "\n\n"
                
                # Transcript
                print("\n4️⃣ TRANSCRIPT")
                print("-" * 40)
                transcript = analyzer.analyze_local_video(video_source, "transcript")
                print(transcript)
                full_content += "4. TRANSCRIPT:\n" + "-"*30 + "\n" + transcript + "\n"
            else:
                # For YouTube videos, use existing methods
                # Summary
                print("1️⃣ VIDEO SUMMARY")
                print("-" * 40)
                summary = analyzer.summarize_video(video_source, 5)
                print(summary)
                full_content += "1. VIDEO SUMMARY:\n" + "-"*30 + "\n" + summary + "\n\n"
                
                # Key Topics
                print("\n2️⃣ KEY TOPICS")
                print("-" * 40)
                topics = analyzer.extract_key_topics(video_source)
                print(topics)
                full_content += "2. KEY TOPICS:\n" + "-"*30 + "\n" + topics + "\n\n"
                
                # Quiz
                print("\n3️⃣ QUIZ")
                print("-" * 40)
                quiz = analyzer.create_quiz(video_source, 3)
                print(quiz)
                full_content += "3. QUIZ:\n" + "-"*30 + "\n" + quiz + "\n\n"
                
                # Sample timestamp analysis
                print("\n4️⃣ SAMPLE TIMESTAMP ANALYSIS (00:30)")
                print("-" * 40)
                timestamp_analysis = analyzer.analyze_timestamp(video_source, "00:30")
                print(timestamp_analysis)
                full_content += "4. SAMPLE TIMESTAMP ANALYSIS (00:30):\n" + "-"*30 + "\n" + timestamp_analysis + "\n"
        
        # Save to file
        save_to_file(full_content, output_filename)
        
        print("\n" + "=" * 80)
        print("✅ Analysis completed successfully!")
        print(f"💾 Results saved to: {output_filename}")
        
        if args.video_file or args.command == 'local':
            print("\n✨ Local video analysis completed using Gemini API.")
            print("   Results should be accurate as the video content was directly processed.")
        else:
            print("\n⚠️  LƯU Ý: Gemini có thể không phân tích chính xác nội dung video YouTube.")
            print("   Để có kết quả chính xác hơn, hãy sử dụng video file local hoặc transcript.")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure you have installed google-generativeai package:")
        print("   pip install google-generativeai python-dotenv")
        print("2. Check that your API key is valid in .env file")
        print("3. Ensure the video URL is valid and public")
        print("4. Note: Direct YouTube video analysis might not be supported in all regions")
        sys.exit(1)

if __name__ == "__main__":
    main()