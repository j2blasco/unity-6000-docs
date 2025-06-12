* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.EventHandler.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).EventHandler
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
public delegate void EventHandler([Video.VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) source); 
### Parameters
Parameter | Description  
---|---  
source | The [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) that emits the event.  
### Description
Delegate type for all events without parameters emitted by [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)s.
Use this EventHandler to define what you want to happen when the [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) emits certain events. This EventHandler accepts the following VideoPlayer events: 
  * [VideoPlayer.loopPointReached](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-loopPointReached.html)
  * [VideoPlayer.started](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-started.html)
  * [VideoPlayer.prepareCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-prepareCompleted.html)
  * [VideoPlayer.seekCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-seekCompleted.html)


This EventHandler doesn't accept events that have parameters.   
  
Additional resources: For EventHandlers that can accept parameters, refer to VideoPlayer.ErrorEventHandler which handles [VideoPlayer.errorReceived](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-errorReceived.html), VideoPlayer.FrameReadyEventHandler which handles [VideoPlayer.frameReady](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-frameReady.html), and VideoPlayer.TimeEventHandler.
```
// This script sets up a generic EventHandler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.EventHandler.html) to process a few different parameter-less events from the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).   
  
using UnityEngine;
using UnityEngine.Video;  
  
public class EventHandlerExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) videoPlayer;  
  

    void Start()
    {
        videoPlayer = GetComponent<VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)>();  
  
        // Define a generic EventHandler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.EventHandler.html) for events that have the same signature.
        VideoPlayer.EventHandler eventHandler = OnVideoPlayerEvent;  
  
        // Assign the generic EventHandler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.EventHandler.html) to manage multiple VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) events. 
        videoPlayer.prepareCompleted += eventHandler;
        videoPlayer.started += eventHandler;
        videoPlayer.loopPointReached += eventHandler;
        videoPlayer.seekCompleted += eventHandler;  
  
        videoPlayer.Prepare();
    }  
  
    // All those events will invoke this same function and be handled the same way. 
    private void OnVideoPlayerEvent(VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) vp)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("An event occurred on VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).");
    }
}
```

* * *
