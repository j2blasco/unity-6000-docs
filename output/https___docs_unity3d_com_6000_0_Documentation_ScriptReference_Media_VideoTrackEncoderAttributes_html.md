* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes.html

# VideoTrackEncoderAttributes
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
Descriptor for video track format.
```
using UnityEditor.Media;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class Recorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html)
{
    public VideoTrackEncoderAttributes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes.html) CreateEncoderAttributes()
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
  
        return videoAttr;
    }
}

```

### Properties
Property | Description  
---|---  
[bitRateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes-bitRateMode.html) | The VideoBitrateMode for the encoded video.  
[frameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes-frameRate.html) | The frame rate for the encoded video, in frames per second, expressed as a fraction.  
[height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes-height.html) | The image height in pixels.  
[includeAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes-includeAlpha.html) | True if the track is to include the alpha channel found in the texture passed to AddFrame. False otherwise.  
[targetBitRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes-targetBitRate.html) | The target bit rate for the encoder.  
[width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes-width.html) | The image width in pixels.  
### Constructors
Constructor | Description  
---|---  
[VideoTrackEncoderAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes-ctor.html) | Create a new VideoTrackEncoderAttributes with specific H.264 encoding options.  
* * *
