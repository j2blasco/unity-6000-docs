* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.UnPause.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).UnPause
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html "Go to AudioSource Component in the Manual")
## Declaration
public void UnPause(); 
### Description
Unpause the paused playback of this AudioSource.
This function is similar to if you call Play() on a paused AudioSource, except that it will not create a new playback voice if it is not currently paused.  
  
This is also useful if you have paused one-shots and want to resume playback without creating a new playback voice for the attached AudioClip.  
  
If you use `UnPause` on an AudioSource that hasn't played before or has stopped, the audio will not play. This is because `UnPause` resumes the clip from when the clip was last paused. You need to play and then pause the clip before you can unpause it.
```
using UnityEngine;  
  
// The Audio Source component has an AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) option.  The audio
// played in this example comes from AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) and is called audioData.  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)))]
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource;  
  
    void Start()
    {
        audioSource = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
        audioSource.Play(0);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("started");
    }  
  
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 70, 150, 30), "Pause"))
        {
            audioSource.Pause();
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Pause: " + audioSource.time);
        }  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 170, 150, 30), "Continue"))
        {
            audioSource.UnPause();
        }
    }
}

```

* * *
