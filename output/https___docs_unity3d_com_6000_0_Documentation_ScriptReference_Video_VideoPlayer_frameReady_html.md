* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-frameReady.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).frameReady
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
### Parameters
Parameter | Description  
---|---  
value | The number of the frame that is ready (zero-based index).  
### Description
The VideoPlayer invokes this event when a new frame is ready to be displayed.
Use this event to: 
  * Analyze certain frames of a video.
  * Track progress of the video.
  * Play other effects such as animations or sound effects at a certain frame.


To enable this event so that the VideoPlayer emits it, set the [VideoPlayer.sendFrameReadyEvents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-sendFrameReadyEvents.html) property to `true`. This event is likely to tax the CPU, so set [VideoPlayer.sendFrameReadyEvents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-sendFrameReadyEvents.html) back to `false` when you don’t need it.   
  
The VideoPlayer also emits this event if you call [VideoPlayer.Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Pause.html) on a VideoPlayer that's not prepared yet or isn’t currently playing. When you call `Pause()` on a VideoPlayer that's not prepared or playing, it behaves as if you called `Play()` and then immediately called `Pause()`. This allows you to seek to a certain point in the video, and pause to give it time to prepare the frame before you play it.
```
// This script plays some audio when the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) reaches the frame ( targetFrame ) you set.  
// Make sure to assign a VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component to your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and assign an AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) in the Inspector.   
  
using UnityEngine;
using UnityEngine.UIElements;
using UnityEngine.Video;  
  
public class FrameReadyExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) videoPlayer;
    public AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource;  
  
    // The frame you want to play the sound at (set this value in the Inspector). 
    public int targetFrame;  
  
    void Start()
    {
        videoPlayer = GetComponent<VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)>();  
  
        if (videoPlayer != null)
        {
            // Prepare the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) to play the video. 
            videoPlayer.prepareCompleted += OnPrepareCompleted;
            videoPlayer.Prepare();
        }
        else
            Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)("Your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) doesn't have a VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component.");
    }  
  
    void OnPrepareCompleted(VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) vp)
    {
        // Clamp targetFrame to be within the frame count of the video. 
        var totalFrames = videoPlayer.frameCount; 
        targetFrame = Mathf.Clamp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Clamp.html)(targetFrame, 0, (int)totalFrames - 1);  
  
        videoPlayer.sendFrameReadyEvents = true;
        // When frameReady event is invoked, call this function. 
        videoPlayer.frameReady += OnFrameReady;  
  
        videoPlayer.Play(); 
    }  
  
    void OnFrameReady(VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) vp, long frameToPlay)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Frame " + frameToPlay + " is ready.");  
  
        // Play the audio when the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) video reaches the target frame.
        if (frameToPlay == targetFrame)
        {
            if (audioSource != null)
            {
                audioSource.Play();
            }
            else
                Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)("AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) component is missing."); 
           
            videoPlayer.sendFrameReadyEvents = false;
        }
    }
}
```

* * *
