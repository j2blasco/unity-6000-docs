* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-loopPointReached.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).loopPointReached
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
value | The instance of the VideoPlayer that invokes the event.  
### Description
The VideoPlayer emits this event when the video reaches the end of its playback.
If you set the [VideoPlayer.isLooping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-isLooping.html) property to `true`, this event makes the video play again. Otherwise the [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) stops. You can also set the **Loop** property in the Inspector window of the [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component.  
  
Additional resources: [VideoPlayer.isLooping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-isLooping.html), [VideoPlayer.started](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-started.html), [EventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.EventHandler.html).
```
// This script plays a Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html) when the video finishes, and then loops the video. 
// Attach this script and a VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). Also attach a ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) in the Inspector.   
  
using UnityEngine;
using UnityEngine.Video;  
  
public class LoopPointReachedExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) videoPlayer;
    public ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) particles;   
  
    void Start()
    {
        videoPlayer = GetComponent<VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)>();
        particles.playOnAwake = false;   
  
        // When the video playback is done, restart the video. 
        videoPlayer.isLooping = true;  
  
        // Each time the video reaches the end, call this function. 
        videoPlayer.loopPointReached += OnLoopPointReached;  
  
        videoPlayer.Play();
    }  
  
    void OnLoopPointReached(VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) vp)
    {
        // Play the particle effect when the video reaches the end.  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Loop finished, play particle effect.");
        particles.Play();
    }
}

```

* * *
