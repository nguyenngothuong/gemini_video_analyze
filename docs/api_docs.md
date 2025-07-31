* [Home](https://ai.google.dev/)
* [Gemini API](https://ai.google.dev/gemini-api)
* [Models](https://ai.google.dev/gemini-api/docs)

Was this helpful?

Send feedback# Video understanding

Gemini models can process videos, enabling many frontier developer use cases that would have historically required domain specific models. Some of Gemini's vision capabilities include the ability to:

* Describe, segment, and extract information from videos
* Answer questions about video content
* Refer to specific timestamps within a video

Gemini was built to be multimodal from the ground up and we continue to push the frontier of what is possible. This guide shows how to use the Gemini API to generate text responses based on video inputs.

## Video input

You can provide videos as input to Gemini in the following ways:

* [Upload a video file](https://ai.google.dev/gemini-api/docs/video-understanding#upload-video) using the File API before making a request to `generateContent`. Use this method for files larger than 20MB, videos longer than approximately 1 minute, or when you want to reuse the file across multiple requests.
* [Pass inline video data](https://ai.google.dev/gemini-api/docs/video-understanding#inline-video) with the request to `generateContent`. Use this method for smaller files (<20MB) and shorter durations.
* [Include a YouTube URL](https://ai.google.dev/gemini-api/docs/video-understanding#youtube) directly in the prompt.

### Upload a video file

You can use the [Files API](https://ai.google.dev/gemini-api/docs/files) to upload a video file. Always use the Files API when the total request size (including the file, text prompt, system instructions, etc.) is larger than 20 MB, the video duration is significant, or if you intend to use the same video in multiple prompts. The File API accepts video file formats directly.

The following code downloads the sample video, uploads it using the File API, waits for it to be processed, and then uses the file reference in a `generateContent` request.

[Python](https://ai.google.dev/gemini-api/docs/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/video-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/video-understanding#rest)

```
fromgoogleimport genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
)

print(response.text)
```

To learn more about working with media files, see [Files API](https://ai.google.dev/gemini-api/docs/files).

### Pass video data inline

Instead of uploading a video file using the File API, you can pass smaller videos directly in the request to `generateContent`. This is suitable for shorter videos under 20MB total request size.

Here's an example of providing inline video data:

[Python](https://ai.google.dev/gemini-api/docs/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding#javascript)[REST](https://ai.google.dev/gemini-api/docs/video-understanding#rest)

```
# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

response = client.models.generate_content(
    model='models/gemini-2.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### Include a You**Tube URL**

**Preview:** The YouTube URL feature is in preview and is available at no charge. Pricing and rate limits are likely to change.The Gemini API and AI Studio support YouTube URLs as a file data `Part`. You can include a YouTube URL with a prompt asking the model to summarize, translate, or otherwise interact with the video content.

**Limitations:**

* For the free tier, you can't upload more than 8 hours of YouTube video per day.
* For the paid tier, there is no limit based on video length.
* For models before 2.5, you can upload only 1 video per request. For models after 2.5, you can upload a maximum of 10 videos per request.
* You can only upload public videos (not private or unlisted videos).

The following example shows how to include a YouTube URL with a prompt:

[Python](https://ai.google.dev/gemini-api/docs/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/video-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/video-understanding#rest)

```
response = client.models.generate_content(
    model='models/gemini-2.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

## Refer to timestamps in the content

You can ask questions about specific points in time within the video using timestamps of the form `MM:SS`.

[Python](https://ai.google.dev/gemini-api/docs/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/video-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/video-understanding#rest)

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?" # Adjusted timestamps for the NASA video
```

## Transcribe video and provide visual descriptions

The Gemini models can transcribe and provide visual descriptions of video content by processing both the audio track and visual frames. For visual descriptions, the model samples the video at a rate of  **1 frame per second** . This sampling rate may affect the level of detail in the descriptions, particularly for videos with rapidly changing visuals.

[Python](https://ai.google.dev/gemini-api/docs/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/video-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/video-understanding#rest)

```
prompt = "Transcribe the audio from this video, giving timestamps for salient events in the video. Also provide visual descriptions."
```

## Customize video processing

You can customize video processing in the Gemini API by setting clipping intervals or providing custom frame rate sampling.

**Tip:** Video clipping and frames per second (FPS) are supported by all models, but the quality is significantly higher from 2.5 series models.### Set clipping intervals

You can clip video by specifying `videoMetadata` with start and end offsets.

[Python](https://ai.google.dev/gemini-api/docs/video-understanding#python)

```
response = client.models.generate_content(
    model='models/gemini-2.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),
                video_metadata=types.VideoMetadata(
                    start_offset='1250s',
                    end_offset='1570s'
                )
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### Set a custom frame rate

You can set custom frame rate sampling by passing an `fps` argument to `videoMetadata`.

**Note:** Due to built-in per image based safety checks, the same video may get blocked at some fps and not at others due to different extracted frames.[Python](https://ai.google.dev/gemini-api/docs/video-understanding#python)

```
# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

response = client.models.generate_content(
    model='models/gemini-2.5-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=5)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

By default 1 frame per second (FPS) is sampled from the video. You might want to set low FPS (< 1) for long videos. This is especially useful for mostly static videos (e.g. lectures). If you want to capture more details in rapidly changing visuals, consider setting a higher FPS value.

## Supported video formats

Gemini supports the following video format MIME types:

* `video/mp4`
* `video/mpeg`
* `video/mov`
* `video/avi`
* `video/x-flv`
* `video/mpg`
* `video/webm`
* `video/wmv`
* `video/3gpp`

## Technical details about videos

* **Supported models & context** : All Gemini 2.0 and 2.5 models can process video data.
* Models with a 2M context window can process videos up to 2 hours long at default media resolution or 6 hours long at low media resolution, while models with a 1M context window can process videos up to 1 hour long at default media resolution or 3 hours long at low media resolution.
* **File API processing** : When using the File API, videos are sampled at 1 frame per second (FPS) and audio is processed at 1Kbps (single channel). Timestamps are added every second.
* These rates are subject to change in the future for improvements in inference.
* **Token calculation** : Each second of video is tokenized as follows:
* Individual frames (sampled at 1 FPS):
  * If [`mediaResolution`](https://ai.google.dev/api/generate-content#MediaResolution) is set to low, frames are tokenized at 66 tokens per frame.
  * Otherwise, frames are tokenized at 258 tokens per frame.
* Audio: 32 tokens per second.
* Metadata is also included.
* Total: Approximately 300 tokens per second of video at default media resolution, or 100 tokens per second of video at low media resolution.
* **Timestamp format** : When referring to specific moments in a video within your prompt, use the `MM:SS` format (e.g., `01:15` for 1 minute and 15 seconds).
* **Best practices** :
* Use only one video per prompt request for optimal results.
* If combining text and a single video, place the text prompt *after* the video part in the `contents` array.
* Be aware that fast action sequences might lose detail due to the 1 FPS sampling rate. Consider slowing down such clips if necessary.

## What's next

This guide shows how to upload video files and generate text outputs from video inputs. To learn more, see the following resources:

* [System instructions](https://ai.google.dev/gemini-api/docs/text-generation#system-instructions): System instructions let you steer the behavior of the model based on your specific needs and use cases.
* [Files API](https://ai.google.dev/gemini-api/docs/files): Learn more about uploading and managing files for use with Gemini.
* [File prompting strategies](https://ai.google.dev/gemini-api/docs/files#prompt-guide): The Gemini API supports prompting with text, image, audio, and video data, also known as multimodal prompting.
* [Safety guidance](https://ai.google.dev/gemini-api/docs/safety-guidance): Sometimes generative AI models produce unexpected outputs, such as outputs that are inaccurate, biased, or offensive. Post-processing and human evaluation are essential to limit the risk of harm from such outputs.
