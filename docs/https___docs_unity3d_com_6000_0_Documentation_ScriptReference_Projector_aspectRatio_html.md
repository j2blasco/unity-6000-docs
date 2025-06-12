* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector-aspectRatio.html

#  [Projector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector.html).aspectRatio
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Projector.html "Go to Projector Component in the Manual")
aspectRatio; 
### Description
The aspect ratio of the projection.
This is projection width divided by height. An aspect ratio of 1.0 makes the projection square; a ratio of 2.0 makes it twice as wide than high. Additional resources: [projector component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Projector.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Get the projector
        Projector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector.html) proj = GetComponent<Projector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector.html)>();
        // Use it
        proj.aspectRatio = 2.0f;
    }
}

```

* * *
