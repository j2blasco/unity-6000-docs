* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-spread.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).spread
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
spread; 
### Description
Sets the spread angle (in degrees) of a 3d stereo or multichannel sound in speaker space.
0 = all sound channels are located at the same speaker location and is 'mono'. 360 = all subchannels are located at the opposite speaker location to the speaker location that it should be according to 3D position. Default = 0.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // when any AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) goes trough this transform, it will set it as 'mono'
    // and will restore the value to 3D effect after exiting
    // Make sure the audio source has a collider.
    void OnTriggerEnter(Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) other)
    {
        AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audio = other.GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();  
  
        if (audio)
        {
            audio.spread = 0;
        }
    }  
  
    void OnTriggerExit(Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) other)
    {
        AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audio = other.GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();  
  
        if (audio)
        {
            audio.spread = 360;
        }
    }
}

```

* * *
