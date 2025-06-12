* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaEncoder.html

# MediaEncoder
class in UnityEditor.Media
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
Encodes images and audio samples into an audio or movie file.
Constructing an instance of this class creates an encoder that will create an audio, video or audio/video file with the specified tracks in it.  
  
Call the AddFrame() and AddSamples() methods alternately for each track, so that frames and samples keep each track equally filled.  
  
Once all the wanted frames and samples are added to the file, call Dispose() to end each track properly and close the file.
```
using UnityEditor.Media;
using UnityEngine;
using Unity.Collections;
using System.IO;  
  
public class Recorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html)
{
    static public void RecordMovie()
    {
        var videoAttr = new VideoTrackAttributes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackAttributes.html)
        {
            frameRate = new MediaRational[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaRational.html)(50),
            width = 320,
            height = 200,
            includeAlpha = false
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
### Constructors
Constructor | Description  
---|---  
[MediaEncoder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaEncoder-ctor.html) | Create a new encoder with various track arrangements.  
### Public Methods
Method | Description  
---|---  
[AddFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaEncoder.AddFrame.html) | Appends a frame to the file's video track.  
[AddSamples](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaEncoder.AddSamples.html) | Appends sample frames to the specified audio track.  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaEncoder.Dispose.html) | Finishes writing all tracks and closes the file being written.  
* * *
