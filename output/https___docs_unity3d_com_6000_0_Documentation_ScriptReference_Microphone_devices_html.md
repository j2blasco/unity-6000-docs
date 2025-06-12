* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone-devices.html

#  [Microphone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.html).devices
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Microphone.html "Go to Microphone Component in the Manual")
devices; 
### Description
A list of available microphone devices, identified by name.
You can use the name with the [Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.Start.html) and [End](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.End.html) functions to specify which microphone you wish to start/stop recording.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Get list of Microphone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.html) devices and print the names to the log
    void Start()
    {
        foreach (var device in Microphone.devices[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone-devices.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Name: " + device);
        }
    }
}

```

Additional resources: [Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.Start.html), [End](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.End.html), [IsRecording](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.IsRecording.html).
* * *
