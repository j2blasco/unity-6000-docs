* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-length.html

#  [VideoClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html).length
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
length; 
### Description
The length of the video clip in seconds. (Read Only).
You can use this property to ensure any events, sounds, visual effects, logic etc. you want to trigger during the video happen within the time limits of the video.   
  
**Note** : The VideoClip can return an inaccurate length because the external encoder can be imprecise. Use [VideoPlayer.frameCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-frameCount.html) and [VideoPlayer.frameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-frameRate.html) to get more accurate results.
```
// This script outputs the length of the video clip given by the VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) component
// and the length given by calculating the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) frame rate and frame count. These can 
// sometimes give different results, but the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) is more accurate, especially after the video
// plays through once.   
  
using UnityEngine;
using UnityEngine.Video;  
  
public class VideoClipExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) videoPlayer;   
  
    void Start()
    {
        if(videoPlayer != null)
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
        // Get frame count and frame rate from the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html). 
        ulong frameCount = videoPlayer.frameCount;
        double frameRate = videoPlayer.frameRate;  
  
        // Calculate the length in seconds. 
        double lengthInSeconds = frameCount / frameRate;  
  
        // Output the length from the VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) and the calculated length. 
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Initial clip length: {clip.length} seconds.");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Calculated Length[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.html): {lengthInSeconds} seconds.");
    }  
  
    void OnLoop(VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) vp)
    {
        // Recalculate the video length with each loop. 
        CalculateVideoLength(vp.clip); 
    }
}
```

* * *
