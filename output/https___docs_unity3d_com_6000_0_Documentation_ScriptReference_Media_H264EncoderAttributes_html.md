* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.H264EncoderAttributes.html

# H264EncoderAttributes
struct in UnityEditor.Media
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Descriptor for H.264 encoder attributes.
```
using UnityEditor.Media;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using Unity.Collections;
using System.IO;  
  
public class Recorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html)
{
    static public void RecordMovie()
    {
        H264EncoderAttributes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.H264EncoderAttributes.html) h264Attr = new H264EncoderAttributes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.H264EncoderAttributes.html)
        {
            gopSize = 25,
            numConsecutiveBFrames = 2,
            profile = VideoEncodingProfile.H264High[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoEncodingProfile.H264High.html)
        };  
  
        var videoAttr = new VideoTrackEncoderAttributes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes.html)(h264Attr)
        {
            frameRate = new MediaRational[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaRational.html)(50),
            width = 320,
            height = 200,
            targetBitRate = 3000000
        };  
  
        var audioAttr = new AudioTrackAttributes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.AudioTrackAttributes.html)
        {
            sampleRate = new MediaRational[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaRational.html)(48000),
            channelCount = 2,
            language = "fr"
        };  
  
        int sampleFramesPerVideoFrame = audioAttr.channelCount *
            audioAttr.sampleRate.numerator / videoAttr.frameRate.numerator;  
  
        var encodedFilePath = Path.Combine(Path.GetTempPath(), "my_movie.mp4");  
  
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)((int)videoAttr.width, (int)videoAttr.height, TextureFormat.RGBA32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGBA32.html), false);  
  
        using (var encoder = new MediaEncoder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaEncoder.html)(encodedFilePath, videoAttr, audioAttr))
        using (var audioBuffer = new NativeArray<float>(sampleFramesPerVideoFrame, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html)))
        {
            for (int i = 0; i < 100; ++i)
            {
                // Fill 'tex' with the video content to be encoded into the file for this frame.
                // ...
                encoder.AddFrame(tex);  
  
                // Fill 'audioBuffer' with the audio content to be encoded into the file for this frame.
                // ...
                encoder.AddSamples(audioBuffer);
            }
        }
    }
}

```

### Properties
Property | Description  
---|---  
[gopSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.H264EncoderAttributes-gopSize.html) | The maximum size of a group of pictures, in frames.  
[numConsecutiveBFrames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.H264EncoderAttributes-numConsecutiveBFrames.html) | The maximum number of consecutive B frames between I and P frames.  
[profile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.H264EncoderAttributes-profile.html) | The VideoEncodingProfile for the encoded video.  
* * *
