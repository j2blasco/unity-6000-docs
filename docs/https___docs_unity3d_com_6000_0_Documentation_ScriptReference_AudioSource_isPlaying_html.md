* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-isPlaying.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).isPlaying
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
isPlaying; 
### Description
Returns whether the AudioSource is currently playing an [AudioResource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioResource.html)(Read Only).
AudioSource.isPlaying returns true if the [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) is playing any [AudioResource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioResource.html), such as [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) or AudioRandomContainer. This includes if you use PlayOneShot() or if you play a video or timeline track through the AudioSource.   
  
**Note:** [AudioSource.isPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-isPlaying.html) returns _false_ when `AudioSource.Pause()` is called. If you use `AudioSource.Play()` back again, it returns true.  
  
**Note:** If you use [AudioSource.PlayDelayed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayDelayed.html) to play your clip, AudioSource.isPlaying returns true during the delay.
```
// When the audio component has stopped playing, play otherClip.
// Remember to assign an AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) in the Inspector.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) otherClip;
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource;  
  
    void Start()
    {
        audioSource = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (!audioSource.isPlaying)
        { 
            audioSource.clip = otherClip;
            audioSource.Play();
        }
    }
}

```

* * *
