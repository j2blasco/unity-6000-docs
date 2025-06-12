* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Play.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).Play
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
public void Play(ulong delay = 0); 
### Parameters
Parameter | Description  
---|---  
delay | Deprecated. Delay in number of samples, assuming a 44100Hz sample rate (meaning that Play(44100) will delay the playing by exactly 1 sec).  
### Description
Plays the [clip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-clip.html).
The delay parameter is deprecated, please use the newer [AudioSource.PlayDelayed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayDelayed.html) function instead which specifies the delay in seconds.  
  
If [AudioSource.clip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-clip.html) is set to the same clip that is playing then the clip will sound like it is re-started. [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) will assume any [Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Play.html) call will have a new audio clip to play.  
  
**Note:** The [AudioSource.PlayScheduled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayScheduled.html) API will give you more accurate control over when the audio clip is played.  
  
For a list of audio file types Unity supports, refer to [Audio Clip](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html).
```
using UnityEngine;  
  
// The Audio Source component has an AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) option.  The audio
// played in this example comes from AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) and is called audioData.  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)))]
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioData;  
  
    void Start()
    {
        audioData = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
        audioData.Play(0);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("started");
    }  
  
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 70, 150, 30), "Pause"))
        {
            audioData.Pause();
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Pause: " + audioData.time);
        }  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 170, 150, 30), "Continue"))
        {
            audioData.UnPause();
        }
    }
}

```

Additional resources: [Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Stop.html), [Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Pause.html), [clip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-clip.html) and [PlayScheduled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayScheduled.html) functions.
* * *
