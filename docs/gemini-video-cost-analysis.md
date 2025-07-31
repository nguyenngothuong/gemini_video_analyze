# Gemini Video API - Chi phí và Tối ưu

## Bảng so sánh chi phí các API

| Service | Input Cost | Output Cost | Video Processing | Notes |
|---------|------------|-------------|------------------|-------|
| **Gemini 2.5 Flash** | $0.075/1M tokens | $0.30/1M tokens | 300 tokens/giây (thường)<br>100 tokens/giây (thấp) | Khuyến nghị cho production |
| **Gemini 2.5 Pro** | $1.25/1M tokens | $5.00/1M tokens | Tương tự Flash | Chất lượng cao hơn |
| **OpenAI GPT-4 Turbo** | $10/1M tokens | $30/1M tokens | N/A (text only) | Cần Whisper để xử lý video |
| **OpenAI GPT-4o** | $2.50/1M tokens | $10/1M tokens | Hỗ trợ vision/audio | Mới, còn hạn chế |
| **Whisper API** | $0.006/phút | N/A | Audio only | Chỉ transcription |
| **Claude 3.5 Sonnet** | $3/1M tokens | $15/1M tokens | N/A (text only) | Không hỗ trợ video |

## So sánh chi phí theo thời lượng video

| Thời lượng | Gemini 2.5 Flash | Gemini 2.5 Pro | Whisper + GPT-4 | YouTube API + Gemini |
|------------|------------------|-----------------|-----------------|---------------------|
| **2 phút** | $0.003 (70 VNĐ) | $0.045 (1,050 VNĐ) | $0.062 (1,450 VNĐ) | $0.001 (25 VNĐ) |
| **5 phút** | $0.007 (165 VNĐ) | $0.112 (2,600 VNĐ) | $0.08 (1,850 VNĐ) | $0.002 (50 VNĐ) |
| **10 phút** | $0.014 (330 VNĐ) | $0.225 (5,250 VNĐ) | $0.13 (3,000 VNĐ) | $0.004 (95 VNĐ) |
| **30 phút** | $0.043 (1,000 VNĐ) | $0.675 (15,750 VNĐ) | $0.36 (8,400 VNĐ) | $0.012 (280 VNĐ) |
| **60 phút** | $0.086 (2,000 VNĐ) | $1.35 (31,500 VNĐ) | $0.69 (16,100 VNĐ) | $0.024 (560 VNĐ) |

## Chi tiết tính toán chi phí

### Gemini 2.5 Flash - Video Local Analysis

#### Video ngắn (1-3 phút)
```
Video 2 phút = 120 giây
Tokens input: 120 × 300 = 36,000 tokens (0.036M)
Chi phí input: 0.036M × $0.075 = $0.0027

Output ước tính:
- Summary: 200-500 tokens → $0.00006-0.00015
- Topics: 500-1000 tokens → $0.00015-0.0003  
- Transcript: 2000-3000 tokens → $0.0006-0.0009
- Detailed: 3000-5000 tokens → $0.0009-0.0015

Tổng chi phí: $0.003-0.004 (70-95 VNĐ)
```

#### Video trung bình (5-10 phút)
```
Video 8 phút = 480 giây  
Tokens input: 480 × 300 = 144,000 tokens (0.144M)
Chi phí input: 0.144M × $0.075 = $0.0108

Output ước tính:
- Summary: 300-600 tokens → $0.00009-0.00018
- Topics: 800-1500 tokens → $0.00024-0.00045
- Transcript: 4000-6000 tokens → $0.0012-0.0018
- Detailed: 5000-8000 tokens → $0.0015-0.0024

Tổng chi phí: $0.011-0.014 (260-330 VNĐ)
```

#### Video dài (30-60 phút)
```
Video 45 phút = 2,700 giây
Tokens input: 2,700 × 300 = 810,000 tokens (0.81M)  
Chi phí input: 0.81M × $0.075 = $0.06075

Output ước tính:
- Summary: 500-1000 tokens → $0.00015-0.0003
- Topics: 1500-3000 tokens → $0.00045-0.0009
- Transcript: 15000-25000 tokens → $0.0045-0.0075
- Detailed: 10000-20000 tokens → $0.003-0.006

Tổng chi phí: $0.061-0.068 (1,400-1,600 VNĐ)
```

### So sánh chi tiết với các giải pháp khác

#### OpenAI Whisper + GPT-4 Turbo
```
Video 10 phút:
- Whisper transcription: 10 × $0.006 = $0.06
- GPT-4 processing (ước tính 3000 tokens input + 1000 output):
  * Input: 3000 × $0.01/1K = $0.03
  * Output: 1000 × $0.03/1K = $0.03
- Tổng: $0.12 (2,800 VNĐ)

Ưu điểm: Transcription chính xác cao
Nhược điểm: Không phân tích visual, đắt hơn, cần 2 API calls
```

#### YouTube Transcript API + Gemini Text
```
Video 10 phút:
- YouTube Transcript API: Free (nếu có sẵn transcript)
- Gemini text processing: 2000 tokens × $0.075/1M = $0.00015
- Tổng: ~$0.0002 (5 VNĐ)

Ưu điểm: Rất rẻ, nhanh
Nhược điểm: Chỉ có sẵn cho một số video, không phân tích visual
```

#### Claude 3.5 Sonnet (Text only)
```
Video 10 phút (sau khi có transcript):
- Input: 3000 tokens × $3/1M = $0.009
- Output: 1000 tokens × $15/1M = $0.015
- Tổng: $0.024 (560 VNĐ)

Ưu điểm: Chất lượng phân tích text cao
Nhược điểm: Không xử lý video trực tiếp, cần transcript trước
```

## Tính toán chi phí thực tế

### Video ngắn (1-3 phút)
```
Video 2 phút = 120 giây
Tokens sử dụng: 120 × 300 = 36,000 tokens (0.036M)
Chi phí input: 0.036M × $0.075 = $0.0027
Chi phí output (ước tính 500 tokens): $0.00015
Tổng chi phí: ~$0.003 (70 VNĐ)
```

### Video trung bình (5-10 phút)
```
Video 8 phút = 480 giây  
Tokens sử dụng: 480 × 300 = 144,000 tokens (0.144M)
Chi phí input: 0.144M × $0.075 = $0.0108
Chi phí output (ước tính 1000 tokens): $0.0003
Tổng chi phí: ~$0.011 (260 VNĐ)
```

### Video dài (30-60 phút)
```
Video 45 phút = 2,700 giây
Tokens sử dụng: 2,700 × 300 = 810,000 tokens (0.81M)  
Chi phí input: 0.81M × $0.075 = $0.06075
Chi phí output (ước tính 3000 tokens): $0.0009
Tổng chi phí: ~$0.062 (1,450 VNĐ)
```

## Strategies tối ưu chi phí

### 1. Sử dụng độ phân giải thấp
```python
# Trong script, có thể điều chỉnh để optimize cost
# Video processing sẽ dùng ~100 tokens/giây thay vì 300
# Tiết kiệm 67% chi phí input
```

### 2. Batch processing
```bash
# Xử lý nhiều video cùng lúc để tận dụng context window
python3 test_youtube_video.py local "video1.mp4" --analysis-type summary
python3 test_youtube_video.py local "video2.mp4" --analysis-type summary  
python3 test_youtube_video.py local "video3.mp4" --analysis-type summary
```

### 3. Chọn analysis type phù hợp
- **Summary**: Output ngắn (~200-500 tokens) - rẻ nhất
- **Topics**: Output trung bình (~500-1000 tokens)  
- **Transcript**: Output dài (~2000-5000 tokens) - đắt nhất
- **Detailed**: Output rất dài (~3000-8000 tokens) - đắt nhất

### 4. File size optimization
```bash
# Nén video trước khi xử lý để giảm processing time
ffmpeg -i input.mp4 -vf scale=720:480 -c:v libx264 -crf 28 output_compressed.mp4
```

## So sánh với các giải pháp khác

### OpenAI Whisper + GPT-4
```
Whisper API: $0.006/phút
GPT-4 Turbo: $0.01/1K input tokens, $0.03/1K output tokens

Video 10 phút:
- Whisper: $0.06
- GPT-4 processing transcript: ~$0.05-0.15
- Tổng: $0.11-0.21 (2,500-4,900 VNĐ)
```

### YouTube Transcript API + Gemini
```
YouTube Transcript API: Free
Gemini text processing: ~$0.001-0.005
Tổng: $0.001-0.005 (25-120 VNĐ)
```

## Khuyến nghị cho từng use case

### Development/Testing
- **Sử dụng**: Gemini 2.5 Flash
- **Analysis type**: Summary
- **Video length**: <5 phút
- **Chi phí dự kiến**: <$0.01/video

### Production (Content Analysis)
- **Sử dụng**: Gemini 2.5 Flash  
- **Analysis type**: Topics + Summary
- **Video length**: 10-30 phút
- **Chi phí dự kiến**: $0.02-0.05/video

### Enterprise (Detailed Analysis)
- **Sử dụng**: Gemini 2.5 Pro
- **Analysis type**: Detailed + Transcript
- **Video length**: 30-120 phút  
- **Chi phí dự kiến**: $0.1-0.5/video

## Monitoring và kiểm soát chi phí

### 1. Set budget alerts
```python
# Trong code có thể add token counting
import tiktoken

def estimate_cost(video_duration_seconds):
    tokens = video_duration_seconds * 300  # Flash model
    input_cost = (tokens / 1000000) * 0.075
    return input_cost
```

### 2. Batch size optimization
- Xử lý tối đa 10-15 video/batch để tránh timeout
- Monitor API usage qua Google AI Studio

### 3. Cache results
```python
# Lưu kết quả để tránh xử lý lại video đã phân tích
cache_file = f"cache/{video_hash}.json"
if os.path.exists(cache_file):
    return load_cached_result(cache_file)
```

## Ước tính chi phí cho các dự án thực tế

### Bảng so sánh theo quy mô dự án

| Quy mô | Videos/tháng | Thời lượng TB | Gemini Flash | Gemini Pro | Whisper+GPT4 | Ghi chú |
|--------|--------------|---------------|--------------|------------|--------------|---------|
| **Startup** | 100 | 5 phút | $0.7<br>(16K VNĐ) | $11.2<br>(260K VNĐ) | $8<br>(186K VNĐ) | Content analysis cơ bản |
| **SME** | 1,000 | 10 phút | $14<br>(326K VNĐ) | $225<br>(5.25M VNĐ) | $130<br>(3M VNĐ) | Marketing, education |
| **Enterprise** | 10,000 | 30 phút | $430<br>(10M VNĐ) | $6,750<br>(157M VNĐ) | $3,600<br>(84M VNĐ) | Large scale analysis |
| **Enterprise+** | 100,000 | 15 phút | $2,150<br>(50M VNĐ) | $33,750<br>(787M VNĐ) | $19,500<br>(455M VNĐ) | Media companies |

### Chi tiết từng use case

#### Content Creator (Startup level)
```
Scenario: YouTuber phân tích 100 video/tháng, mỗi video 5 phút
- Gemini Flash (Summary): 100 × $0.007 = $0.7/tháng
- Gemini Flash (Detailed): 100 × $0.01 = $1/tháng  
- Whisper + GPT-4: 100 × $0.08 = $8/tháng

Khuyến nghị: Gemini Flash với Summary analysis
ROI: Tiết kiệm 90% so với OpenAI stack
```

#### E-learning Platform (SME level)
```
Scenario: Phân tích 1,000 video bài giảng/tháng, mỗi video 10 phút
- Gemini Flash (Topics + Summary): 1,000 × $0.016 = $16/tháng
- Gemini Pro (Full analysis): 1,000 × $0.225 = $225/tháng
- Whisper + GPT-4: 1,000 × $0.13 = $130/tháng

Khuyến nghị: Gemini Flash cho bulk processing
Features: Auto-generated quiz, topic extraction, timestamps
```

#### Media Company (Enterprise level)  
```
Scenario: Phân tích 10,000 video content/tháng, mỗi video 30 phút
- Gemini Flash (Batch processing): 10,000 × $0.043 = $430/tháng
- Chi phí nhân sự thay thế: ~$50,000/tháng (manual analysis)
- ROI: 99% cost reduction

Use cases: Content moderation, trend analysis, automated tagging
```

## Tổng kết và khuyến nghị

### Bảng tóm tắt ưu nhược điểm

| Giải pháp | Ưu điểm | Nhược điểm | Best for |
|-----------|---------|------------|----------|
| **Gemini 2.5 Flash** | • Chi phí rẻ nhất cho video<br>• Xử lý audio + visual<br>• Hỗ trợ tiếng Việt tốt<br>• Single API call | • Chất lượng không bằng Pro<br>• YouTube URLs không ổn định | Production, bulk processing |
| **Gemini 2.5 Pro** | • Chất lượng phân tích cao nhất<br>• Context window lớn<br>• Reasoning tốt | • Đắt hơn 15-20x Flash<br>• Overkill cho use case đơn giản | High-end analysis, research |
| **Whisper + GPT-4** | • Transcription rất chính xác<br>• GPT-4 reasoning mạnh<br>• Mature ecosystem | • Chỉ xử lý audio<br>• Cần 2 API calls<br>• Đắt | Audio-focused analysis |
| **YouTube API + Gemini** | • Rẻ nhất (gần như free)<br>• Nhanh | • Chỉ một số video có transcript<br>• Không có visual analysis<br>• Phụ thuộc vào YouTube | Quick text analysis |

### Khuyến nghị theo từng scenario

#### Bắt đầu (< 1000 videos/tháng)
```
✅ Sử dụng: Gemini 2.5 Flash
✅ Analysis type: Summary (200-500 tokens output)
✅ Optimize: Nén video xuống 720p trước khi upload
✅ Cost: < $10/tháng

Lý do: Cost-effective, dễ implement, đủ chức năng cơ bản
```

#### Scale up (1000-10000 videos/tháng)  
```
✅ Sử dụng: Gemini 2.5 Flash với mixed analysis types
✅ Strategy: Summary cho bulk, Detailed cho important content
✅ Optimize: Batch processing, caching results
✅ Cost: $10-500/tháng

Lý do: Balance giữa cost và quality, flexible scaling
```

#### Enterprise (>10000 videos/tháng)
```
✅ Sử dụng: Hybrid approach
  - Gemini Flash cho bulk processing
  - Gemini Pro cho high-value content
✅ Features: Custom prompts, automated workflows
✅ Cost: $500-5000/tháng

Lý do: Maximize ROI, custom integration possibilities
```

### Metrics quan trọng cần track

1. **Cost per video** = Total cost / Number of videos processed
2. **Token efficiency** = Useful output tokens / Total input tokens  
3. **Processing time** = Average seconds per video
4. **Quality score** = Manual evaluation of output accuracy
5. **ROI** = (Manual labor cost saved - API cost) / API cost

### Roadmap và tương lai

**Q2 2024**: 
- Gemini video capabilities đang improve rapidly
- Expect cost reduction và quality improvement

**Dự đoán giá**:
- Gemini Flash: Có thể giảm 20-30% trong 6 tháng tới
- Competition từ OpenAI GPT-4o sẽ push prices down

**Khuyến nghị**:
- Start với Gemini Flash ngay để có experience
- Build infrastructure có thể switch models dễ dàng  
- Monitor cost closely trong giai đoạn đầu

### Kết luận cuối cùng

**Gemini Video API hiện tại là lựa chọn tốt nhất** cho video analysis với tiếng Việt vì:

1. **Chi phí competitive**: Rẻ hơn 5-10x so với Whisper+GPT-4
2. **Single API**: Không cần orchestrate multiple services  
3. **Multimodal**: Xử lý cả audio lẫn visual content
4. **Quality**: Đủ tốt cho majority of use cases
5. **Vietnamese support**: Native support không cần translation

**Action items**:
- Bắt đầu với 2.5 Flash + Summary analysis
- Test với ~10-20 videos để evaluate quality  
- Scale up dần dần based on results
- Monitor cost và adjust strategy accordingly