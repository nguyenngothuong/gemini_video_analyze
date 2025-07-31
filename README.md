# Gemini Video Analyzer - Phân tích Video với Gemini API

## Tính năng chính

**Phân tích video local**: Gemini API hoạt động hoàn hảo với video files local
**YouTube URLs**: Hiện tại không ổn định, đặc biệt với nội dung tiếng Việt

## Cập nhật mới

- **Hỗ trợ phân tích video local**: Upload và phân tích video files trực tiếp
- **4 loại phân tích**: Summary, Transcript, Topics, Detailed Analysis  
- **Xử lý file lớn**: Tự động chọn phương thức phù hợp (inline data vs File API)
- **Kết quả chính xác**: Phân tích đầy đủ cả âm thanh, hình ảnh và nội dung

## Cấu trúc thư mục

```
gemini_video_analyze/
├── README.md                    # Hướng dẫn sử dụng
├── test_youtube_video.py        # Script chính
├── requirements.txt             # Dependencies
├── .env.example                # Mẫu file environment
├── docs/                       # Tài liệu
│   ├── api_docs.md             # API documentation
│   └── video.md                # Phân tích khả năng Gemini Video API
├── examples/                   # Video mẫu
│   └── sample_video.mp4        # Video demo (gitignore)
└── outputs/                    # Kết quả phân tích
    └── *.txt                   # Output files (gitignore)
```

## Cài đặt

```bash
# Clone repository
git clone https://github.com/nguyenngothuong/gemini_video_analyze.git
cd gemini_video_analyze

# Cài đặt dependencies
pip install -r requirements.txt

# Tạo file .env từ template
cp .env.example .env
# Chỉnh sửa .env và thêm API key của bạn
```

## Sử dụng

### Phân tích video local (Khuyến nghị)

```bash
# Phân tích chi tiết video local
python3 test_youtube_video.py local "video.mp4" --analysis-type detailed

# Tóm tắt video với 5 câu
python3 test_youtube_video.py local "video.mp4" --analysis-type summary --sentences 5

# Tạo transcript đầy đủ
python3 test_youtube_video.py local "video.mp4" --analysis-type transcript

# Trích xuất các chủ đề chính
python3 test_youtube_video.py local "video.mp4" --analysis-type topics

# Phân tích toàn diện (summary + topics + detailed + transcript)
python3 test_youtube_video.py --video-file "examples/video.mp4" --output outputs/analysis.txt all
```

### Phân tích YouTube URL (Beta - không ổn định)

```bash
# Tóm tắt video YouTube
python3 test_youtube_video.py summarize --sentences 5

# Các lệnh khác
python3 test_youtube_video.py transcript    # Tạo transcript
python3 test_youtube_video.py topics        # Trích xuất chủ đề
python3 test_youtube_video.py quiz          # Tạo câu hỏi
python3 test_youtube_video.py question "Câu hỏi của bạn"
python3 test_youtube_video.py timestamp "00:30"
python3 test_youtube_video.py clip "0:30" "1:00"
```

## Tính năng

### Video Local
- **Phân tích chính xác 100%** nội dung video
- **4 loại phân tích**: Summary, Transcript, Topics, Detailed
- **Hỗ trợ tiếng Việt** hoàn hảo
- **Xử lý file lớn** tự động (>20MB qua File API)
- **Transcript chi tiết** với timestamp và mô tả hình ảnh
- **Lưu kết quả** ra file .txt

### YouTube URLs  
- **Không ổn định** với nội dung tiếng Việt
- **Kết quả ngẫu nhiên** do API beta
- **Chỉ nên dùng** cho mục đích test

## Sample Output

### Summary Analysis
```
Video giới thiệu tính năng tự động hóa mới của Lark Base, cho phép kích hoạt quy trình từ tin nhắn Lark Messenger. 
Cụ thể, người dùng có thể cấu hình để khi bot được nhắc đến trong một nhóm chat, nội dung tin nhắn và thời gian 
sẽ tự động được thêm vào một bảng dữ liệu trong Lark Base. Điều kiện kích hoạt bao gồm tên bot (trùng với tên file), 
nhóm chat cụ thể và việc bot được tag trong tin nhắn.
```

### Topics Analysis  
```
1. Tính năng tự động hóa tin nhắn Lark Base:
   - Cho phép người dùng thiết lập các quy tắc để tự động thực hiện hành động trong Lark Base khi bot nhận được tin nhắn

2. Thiết lập điều kiện kích hoạt (Trigger):
   - Loại điều kiện: "Khi tin nhắn Lark được nhận" 
   - Phạm vi tin nhắn: Bot nhận tin nhắn trong nhóm chat
   - Điều kiện nội dung: Tin nhắn đề cập đến bot (@mention)

3. Thiết lập hành động tự động (Action):
   - Hành động: "Thêm bản ghi" vào bảng trong Lark Base
   - Nội dung: Tự động điền nội dung tin nhắn và thời gian
```

### Transcript Analysis (Sample)
```
[00:00 - 00:02] Người nói: "Rồi, ở đây nhá,"
Mô tả hình ảnh: Màn hình hiển thị giao diện Lark Base trên trình duyệt Chrome bên phải và Lark Messenger bên trái.

[00:02 - 00:10] Người nói: "phần automation của Lark Base này, nó mới có cái tính năng là... đây, khi một tin nhắn được gửi."
Mô tả hình ảnh: Con trỏ chuột di chuyển đến nút "Automation" và nhấp vào đó, mở ra "Automation center".
```

## Giải pháp thay thế cho YouTube

Để phân tích video YouTube chính xác:

1. **Download video về local rồi phân tích**:
   ```bash
   # Dùng yt-dlp download video
   yt-dlp "https://youtube.com/watch?v=VIDEO_ID" -o "video.mp4"
   
   # Phân tích với Gemini
   python3 test_youtube_video.py local "video.mp4" --analysis-type detailed
   ```

2. **Sử dụng YouTube Transcript API + Gemini**:
   ```bash
   pip install youtube-transcript-api
   # Get transcript -> Phân tích text với Gemini
   ```

## Lưu ý quan trọng

### Video Local Files
- **Gemini API 2.5-Flash** hỗ trợ tốt video analysis với local files
- **Kết quả chính xác** và đáng tin cậy cho nội dung tiếng Việt
- **File size**: <20MB dùng inline data, >20MB dùng File API với processing wait

### YouTube URLs  
- **Tính năng beta** không ổn định, đặc biệt với tiếng Việt
- **Kết quả ngẫu nhiên** do API chưa hỗ trợ đầy đủ YouTube integration
- **Khuyến nghị**: Download video về local để phân tích chính xác

### Technical Notes
- Supports các format: MP4, MOV, AVI, WebM, WMV, 3GPP
- Context window: có thể xử lý video dài (tùy model)
- Token cost: ~300 tokens/giây cho độ phân giải thường

## License

MIT

## Author

Nguyễn Ngô Thường

---

**Repo này minh họa khả năng phân tích video của Gemini API:**
- **Local video files**: Hoạt động hoàn hảo, khuyến nghị cho production
- **YouTube URLs**: Beta không ổn định, chỉ dùng để test

## Liên hệ

Email: work@nguyenngothuong.com

Có nhu cầu tư vấn hoặc phát triển tính năng tương tự, vui lòng liên hệ!