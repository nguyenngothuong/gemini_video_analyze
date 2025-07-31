# Gemini Video Analyze - Phân tích Video YouTube với Gemini API

## ⚠️ Cảnh báo quan trọng

**Gemini API hiện tại KHÔNG hỗ trợ phân tích trực tiếp nội dung video YouTube**. Kết quả trả về hoàn toàn ngẫu nhiên và không chính xác!

## Vấn đề đã phát hiện

Khi test với cùng một video URL: `https://www.youtube.com/watch?v=_6_iwocubu0`

Gemini trả về các nội dung khác nhau hoàn toàn trong mỗi lần chạy:
- Lần 1: Video về cà phê đặc sản
- Lần 2: Video về khu nghỉ dưỡng InterContinental Phú Quốc  
- Lần 3: Video về Viettel Post
- Lần 4: Video về yến mạch (siêu thực phẩm)
- Lần 5: Video về ChatGPT và Marketing
- Lần 6: Video về BLACKPINK - DDU-DU DDU-DU

**Kết luận**: Gemini đang "hallucinate" (tạo nội dung không có thật) thay vì phân tích video thực tế.

## Cài đặt

```bash
# Clone repository
git clone https://github.com/nguyenngothuong/gemini_video_analyze.git
cd gemini_video_analyze

# Cài đặt dependencies
pip install google-generativeai python-dotenv

# Tạo file .env và thêm API key
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

## Sử dụng

```bash
# Tóm tắt video (5 câu)
python3 test_youtube_video.py summarize --sentences 5

# Phân tích toàn diện
python3 test_youtube_video.py --output output.txt all

# Các lệnh khác
python3 test_youtube_video.py transcript    # Tạo transcript
python3 test_youtube_video.py topics        # Trích xuất chủ đề
python3 test_youtube_video.py quiz          # Tạo câu hỏi
python3 test_youtube_video.py question "Câu hỏi của bạn"
python3 test_youtube_video.py timestamp "00:30"
python3 test_youtube_video.py clip "0:30" "1:00"
```

## Tính năng

- ✅ Hỗ trợ tiếng Việt
- ✅ Lưu kết quả ra file .txt
- ❌ **KHÔNG phân tích chính xác nội dung video YouTube**

## Giải pháp thay thế

Để phân tích video YouTube chính xác, bạn nên:

1. **Sử dụng YouTube Transcript API**: Download transcript thực từ YouTube
   ```bash
   pip install youtube-transcript-api
   ```

2. **Sử dụng các công cụ khác**:
   - OpenAI Whisper cho audio
   - YouTube Data API cho metadata
   - Sau đó dùng Gemini phân tích text

3. **Download video và xử lý local**:
   - Tách audio từ video
   - Dùng speech-to-text API
   - Phân tích transcript với Gemini

## Lưu ý cho developers

- Gemini API hiện tại chỉ hỗ trợ phân tích text và image, KHÔNG hỗ trợ video trực tiếp
- Khi gọi API với video URL, Gemini sẽ trả về nội dung ngẫu nhiên
- Luôn kiểm tra và xác thực kết quả trước khi sử dụng

## License

MIT

## Author

Nguyễn Ngô Thường

---

**Repo này được tạo ra để minh họa giới hạn của Gemini API với video YouTube. Không nên sử dụng cho production.**