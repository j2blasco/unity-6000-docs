* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-prepareCompleted.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).prepareCompleted
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
value | The instance of the VideoPlayer that invoked the event.  
### Description
The [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) invokes this event when the video is ready for playback.
The [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) uses [VideoPlayer.Prepare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Prepare.html) to ready a video for playback. When the preparation finishes, the [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) invokes this callback. If you start playback after this callback is invoked, frames become available instantly. If you call [VideoPlayer.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Play.html) without using [VideoPlayer.Prepare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Prepare.html) first, the [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) invokes `Prepare()` anyway. If preparation succeeds, the [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) still invokes this event.  
  
Additional resources: [VideoPlayer.Prepare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Prepare.html), [EventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.EventHandler.html).
```
// In this script, you can only interact with the button to play the video after the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) 
// finishes its preparation of the video. To start the preparation process, press Spacebar in Play mode.   
  
// Attach this script to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you want to play a video clip on. 
// Attach a VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component with a video clip and assign a Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) in the Inspector.  
  
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Video;  
  
public class PrepareExample: MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) videoPlayer;
    public Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) playButton;  
  
    private void Awake()
    {
        // Get the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component from GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with this script attached.  
        videoPlayer = GetComponent<VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)>();
        // Attach the event handler, which triggers when the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) finishes its preparation. 
        videoPlayer.prepareCompleted += OnPrepareCompleted;
        videoPlayer.playOnAwake = false;
        playButton.interactable = false;
    }  
  
    // Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) handler for when VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) finishes the preparation process. 
    void OnPrepareCompleted(VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) vp)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Preparation complete. You can now play the video.");
        
        // Preparation is complete so allow interactions with the play button. 
        playButton.interactable = true;
        playButton.onClick.AddListener(OnPlayButtonClicked);
    }  
  
    void OnPlayButtonClicked()
    {
        // If the play button is clicked and the preparation is done, play the video. 
        if (videoPlayer.isPrepared)
        {
            videoPlayer.Play();
        }
    }  
  
    private void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Press Spacebar to prepare the video. 
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)("space"))
        {
            if (!videoPlayer.isPrepared)
            {
                videoPlayer.Prepare(); 
            }
        }
    }
}

```

* * *
