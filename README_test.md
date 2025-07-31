# YouTube Video Analysis Test Script

Script Python để test các tính năng phân tích video YouTube với Gemini API.

## Cài đặt

```bash
pip install -r requirements.txt
```

## Cấu hình

1. Copy file `.env` và thêm API key của bạn:
```bash
cp .env.example .env
```

2. Sửa file `.env`:
```
GEMINI_API_KEY=your_actual_api_key_here
```

## Sử dụng

### 1. Tóm tắt video
```bash
python test_youtube_video.py --api-key YOUR_API_KEY summarize --sentences 5
```

### 2. Tạo transcript
```bash
python test_youtube_video.py transcript
python test_youtube_video.py transcript --no-timestamps  # Không có timestamp
```

### 3. Tạo quiz
```bash
python test_youtube_video.py quiz --questions 10
```

### 4. Phân tích timestamp cụ thể
```bash
python test_youtube_video.py timestamp "01:30"
```

### 5. Trích xuất chủ đề chính
```bash
python test_youtube_video.py topics
```

### 6. Hỏi câu hỏi về video
```bash
python test_youtube_video.py question "What is the main topic of this video?"
```

### 7. Phân tích một đoạn video
```bash
python test_youtube_video.py clip "30s" "2m"
```

### 8. Chạy tất cả các phân tích
```bash
python test_youtube_video.py all
```

## Các Options

- `--api-key`: API key của Gemini (tùy chọn nếu đã set trong environment)
- `--video-url`: URL video YouTube khác (mặc định: https://www.youtube.com/watch?v=_6_iwocubu0)

## Ví dụ sử dụng

```bash
# Tóm tắt video trong 3 câu
python test_youtube_video.py summarize

# Tạo quiz với 7 câu hỏi
python test_youtube_video.py quiz --questions 7

# Hỏi về nội dung video
python test_youtube_video.py question "What are the key points discussed?"

# Phân tích đoạn từ giây 30 đến phút 2
python test_youtube_video.py clip "30s" "2m"
```

## Lưu ý

- Video phải là public (không phải private hoặc unlisted)
- Free tier: Giới hạn 8 giờ video/ngày
- Paid tier: Không giới hạn độ dài video
- Hỗ trợ các format: MP4, MPEG, MOV, AVI, FLV, MPG, WebM, WMV, 3GPP