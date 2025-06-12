* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings-driverCapabilities.html

#  [AudioSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.html).driverCapabilities
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSettings.html "Go to AudioSettings Component in the Manual")
[AudioSpeakerMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSpeakerMode.html) driverCapabilities; 
### Description
Returns the speaker mode capability of the current audio driver. (Read Only)
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Set the speaker mode to that of the system settings.  
  
    void Start()
    {
        AudioSettings.speakerMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings-speakerMode.html) = AudioSettings.driverCapabilities[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings-driverCapabilities.html);
    }
}

```

* * *
