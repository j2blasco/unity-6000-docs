* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-sleepTimeout.html

#  [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html).sleepTimeout
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
sleepTimeout; 
### Description
A power saving setting, allowing the screen to dim some time after the last active user interaction.
Most useful for handheld devices, allowing OS to preserve battery life in most efficient ways. Does nothing on non-handheld devices.  
  
sleepTimeout is measured in seconds. The default value varies from platform to platform, generally being non-zero.  
  
On mobile devices it would be useful to set sleepTimeout to [SleepTimeout.NeverSleep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SleepTimeout.NeverSleep.html) for games using accelerometer as the main source of input. However, such games should allow screen dimming while in menu or paused. Currently you will only be able to set this property to one of the values predefined in [SleepTimeout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SleepTimeout.html) class. A get will return either one of the predefined values, or the actual number of seconds until screen gets dimmed, as specified in system preferences of the device.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Disable screen dimming
        Screen.sleepTimeout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-sleepTimeout.html) = SleepTimeout.NeverSleep[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SleepTimeout.NeverSleep.html);
    }
}

```

Additional resources: [SleepTimeout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SleepTimeout.html).
* * *
