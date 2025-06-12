* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-clip.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).clip
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
[AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) clip; 
### Description
The default [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) to play.
AudioSource [clip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-clip.html) determines the audio clip that should play next.   
  
When you assign a new audio clip to [clip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-clip.html), the old clip it replaces (if any) stops and is replaced by the new one. However, the new clip doesn't automatically play so you need to use [AudioSource.Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Play.html) (or similar) to play it.
```
// This script outputs a GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) play button. The script plays an audio clip on launch, but if you press the play button it switches to another clip and then plays that one instead. 
// For this script to work, assign it to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). Then, assign an audio clip in the Inspector, and another clip to the Audio Source.    
  
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)))]
public class AudioSourceClipExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) otherClip;
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audio;   
  
    void Start()
    {
        audio = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
        audio.Play();
    }  
  
    private void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 70, 30, 30), "Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) clip"))
        {
            audio.clip = otherClip;
            audio.Play();
        }
    }
}
```

* * *
