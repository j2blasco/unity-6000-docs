* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-isPrepared.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).isPrepared
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
isPrepared; 
### Description
Returns whether the [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) has successfully prepared the content to be played. 
A prepared VideoPlayer can play back the content instantly because preliminary parsing and buffering has been done.  
  
A VideoPlayer starts out as not prepared (`false`). To prepare the VideoPlayer, you need to use [VideoPlayer.Prepare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Prepare.html). When preparation is done, the VideoPlayer emits the [VideoPlayer.prepareCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-prepareCompleted.html) event, which sets `isPrepared` to `true`.   
  
The property goes back to `false` when you or the VideoPlayer calls [VideoPlayer.Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Stop.html).  
  
If there are preparation failures, this property might never be set to `true`. In this case, Unity sends an error description through the [VideoPlayer.errorReceived](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-errorReceived.html) event.  
  
Additional resources: [VideoPlayer.Prepare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Prepare.html).
```
using UnityEngine;
using UnityEngine.Video;
using System.Collections;  
  
// In the Inspector of your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), attach this script and a VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component. 
// Also, assign a VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) to your VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component.  
// Use this script to prepare a video.    
  
public class IsPreparedExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public IEnumerator Start()
    {
        VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) videoPlayer = GetComponent<VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)>();
        videoPlayer.Prepare();
        // Loops until the video is ready.
        // Then outputs the message to the console when the preparation is done. 
        while (!videoPlayer.isPrepared)
        {
            yield return null;
        }
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Preparation completed!");
    }
}

```

* * *
