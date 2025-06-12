* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-frameRate.html

#  [VideoClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html).frameRate
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
frameRate; 
### Description
The frame rate of the clip in frames per second. (Read Only).
The frame rate is the number of frames that are displayed in one second of the video clip. This is useful if you want to synchronize with other effects in your project, and monitor performance. However, [VideoPlayer.frameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-frameRate.html) usually gives a more accurate result.   
  
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
