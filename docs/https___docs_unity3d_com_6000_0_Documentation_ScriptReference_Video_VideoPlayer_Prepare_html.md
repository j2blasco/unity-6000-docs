* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Prepare.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).Prepare
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
public void Prepare(); 
### Description
Prepares the playback engine so that it's ready for playback.
To prepare, the playback engine reserves the resources vital for playback, and preloads some of the content to be played. If the preparation succeeds, this method emits the [VideoPlayer.prepareCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-prepareCompleted.html) event and sets [VideoPlayer.isPrepared](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-isPrepared.html) to `true`. The VideoPlayer is then ready to display the frames immediately and you can access all properties related to the source.   
  
If you don't prepare the VideoPlayer before you play a video, the [VideoPlayer.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Play.html) method will do the preparation but the video won't play instantly. If you use [VideoPlayer.Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Stop.html), the VideoPlayer becomes unprepared again because it frees its resources for performance reasons. To halt a video but keep its preparation, use [VideoPlayer.Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Pause.html) instead.   
  
Additional resources: [VideoPlayer.isPrepared](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-isPrepared.html).
```
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Video;
 
// The button to play the video in the script only becomes interactable after the preparation is finished.
// To start the preparation process, press the Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) key in Play mode.   
  
// Attach this script to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you want to play a video clip on. 
// Attach a VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component with a video clip and assign a UI Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) in the Inspector.  
  
public class PrepareExample: MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) videoPlayer;
    public Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) playButton;  
  
    private void Awake()
    {
        // Get the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component attached to GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with this script attached.  
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
        if(videoPlayer.isPrepared)
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
