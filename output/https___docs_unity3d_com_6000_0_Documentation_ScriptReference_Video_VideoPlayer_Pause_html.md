* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Pause.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).Pause
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
public void Pause(); 
### Description
Pauses the playback and leaves the current time intact.
Use this method to pause the playback of a video. This method sets [VideoPlayer.isPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-isPlaying.html) to `false`. To play again, use [VideoPlayer.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Play.html).   
  
If you pause the video when the VideoPlayer isn't prepared, this method triggers preparation and shows the first frame of the video.   
  
If you seek through to a different point in the video and then call `Pause()` before the VideoPlayer finishes preparation, it triggers preparation and shows the frame that was the seek target. For example, if you set [VideoPlayer.time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-time.html) to `10.0f` and then call `Pause()`, it shows the frame at 10 seconds.  
  
Additional resources: [VideoPlayer.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Play.html).
```
// In the Inspector of a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), attach this script and a VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component.   
  
using UnityEngine;
using UnityEngine.Video;  
  
public class PauseExample: MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) videoPlayer;   
  
    void Start()
    {
        // Get the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with this script attached. 
        videoPlayer = GetComponent<VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)>();
    }  
  
    private void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Press the Spacebar to pause the video if it's playing. 
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)("space"))
        {
            // If the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) is currently playing a video, pause the video. 
            if (videoPlayer.isPlaying)
            {
                videoPlayer.Pause(); 
            }
        }
    }
}

```

* * *
