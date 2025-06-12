* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-frameCount.html

#  [VideoClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html).frameCount
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
frameCount; 
### Description
The length of the video clip in frames. (Read Only).
It’s useful to know the length of a video in frames to ensure any effects you play on a video play within the time frame of the video. [VideoClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) extracts the frame count from the metadata of the file.   
  
**Note** : The length VideoClip returns can be inaccurate as the external encoder can be imprecise. Use [VideoPlayer.frameCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-frameCount.html) to get a more accurate value. However, [VideoPlayer.frameCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-frameCount.html) becomes more precise after one playthrough, so won’t be completely accurate until after the clip finishes once.   
  
Additional resources: [VideoPlayer.frameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-frameRate.html), [VideoPlayer.frameCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-frameCount.html).
```
// This script uses both the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) and VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) components' frame count and frame rate
// to calculate the length of the video in seconds. Sometimes this can return different results, 
// but the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) is more accurate, especially after a full playthrough.
// The script recalculates the counts on each loop.   
  
using UnityEngine;
using UnityEngine.Video;  
  
public class VideoClipLengthCalculator : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) videoPlayer;  
  
    void Start()
    {
        if (videoPlayer != null)
        {
            videoPlayer = GetComponent<VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)>();
            videoPlayer.isLooping = true;
            VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) videoClip = videoPlayer.clip;  
  
            if (videoClip != null)
            {
                CalculateVideoLength(videoClip);
                videoPlayer.loopPointReached += OnLoop;
                videoPlayer.Play();
            }
            else
            {
                Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)("VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) is not assigned.");
            }
        }
        else
        {
            Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)("VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) is not assigned.");
        }
    }  
  
    void CalculateVideoLength(VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) clip)
    {
        // Get frame count and frame rate from the VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html). 
        ulong videoClipFrameCount = clip.frameCount;
        double videoClipFrameRate = clip.frameRate;  
  
        // Calculate the length in seconds (VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html)) and output to console. 
        double videoClipLengthInSeconds = videoClipFrameCount / videoClipFrameRate; 
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Calculated VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) length: {videoClipLengthInSeconds} seconds.");  
  
        // Get frame count and frame rate from the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html). 
        ulong videoPlayerFrameCount = videoPlayer.frameCount;
        double videoPlayerFrameRate = videoPlayer.frameRate;  
  
        // Calculate the length in seconds (VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)) and output to console. 
        double videoPlayerLengthInSeconds = videoPlayerFrameCount / videoPlayerFrameRate;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Calculated VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) Length[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.html): {videoPlayerLengthInSeconds} seconds.");  
  
    }  
  
    void OnLoop(VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) vp)
    {
        // Recalculate the video length after loop happens. 
        CalculateVideoLength(vp.clip);
    }
}

```

* * *
