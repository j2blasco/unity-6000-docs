* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.StepForward.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).StepForward
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
## Declaration
public void StepForward(); 
### Description
Immediately advance the current time by one frame.
If the video is currently playing, this method will pause the video before it advances to the next frame. However, if the VideoPlayer isn't prepared, this method will trigger preparation and display the first frame, but will not skip to the next frame. It steps forward from non-initialized to frame 0.   
  
This method is useful if you want to: 
  * Analyze each frame of a video.
  * Debug issues related to the video or elements that play at certain frames.
  * Take finer control over the playback speed, because you can choose exactly when the next frame will appear. However, the WebGL implementation is unable to provide frame-accurate control due to platform limitations.


```
using UnityEngine;
using UnityEngine.Video;
using System.Collections;  
  
// In the Inspector of your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), attach this script and a VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component. 
// Also, assign a VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) to your VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component.  
// Use this script to cycle through a video frame by frame.   
  
public class StepForwardExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) videoPlayer;  
  
    public void Start()
    {
        videoPlayer = GetComponent<VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)>();
        videoPlayer.Pause();
    }  
  
    private void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)("space") && videoPlayer.isPrepared)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) key pressed."); 
            // Go forward one frame in the video when you press the Spacebar. 
            videoPlayer.StepForward(); 
        }
    }
}

```

* * *
