* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Pause.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).Pause
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
public void Pause(); 
### Description
Pauses playing the [clip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-clip.html).
Additional resources: [Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Play.html), [Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Stop.html) functions.
```
// Allow a song to be chosen and played.  If can be paused, and the song played further.
// Two songs are supported.  
  
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)))]
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // two clips, perhaps songs for the game
    public AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) song1;
    public AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) song2;  
  
    private AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource;
    private bool paused1;
    private bool paused2;  
  
    // both songs are in paused state
    void Start()
    {
        audioSource = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
        paused1 = true;
        paused2 = true;
    }  
  
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 200, 100), "Play song1"))
        {
            if (paused1 && paused2)
            {
                audioSource.clip = song1;
                audioSource.Play(0);
                paused1 = false;
            }
        }  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(250, 10, 200, 100), "Pause song1"))
        {
            if (paused1 == false)
            {
                audioSource.Pause();
                paused1 = true;
            }
        }  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 180, 200, 100), "Play song2"))
        {
            if (paused2 && paused1)
            {
                audioSource.clip = song2;
                audioSource.Play(0);
                paused2 = false;
            }
        }  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(250, 180, 200, 100), "Pause song2"))
        {
            if (paused2 == false)
            {
                audioSource.Pause();
                paused2 = true;
            }
        }
    }
}

```

* * *
