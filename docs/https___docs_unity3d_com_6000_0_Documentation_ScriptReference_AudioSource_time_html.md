* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-time.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).time
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
time; 
### Description
Playback position in seconds.
Use this to read current playback time or to seek to a new playback time.  
  
**Be aware that:** On a compressed audio track position does not necessarily reflect the actual time in the track  
Compressed audio is represented as a set of so-called packets.   
The length of a packet depends on the compression settings and can quite often be 2-3 seconds per packet. Additional resources: [timeSamples](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-timeSamples.html) variable.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource;  
  
    void Start()
    {
        audioSource = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Return[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Return.html)))
        {
            audioSource.Stop();
            audioSource.Play();
        }
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(audioSource.time);
    }
}

```

* * *
