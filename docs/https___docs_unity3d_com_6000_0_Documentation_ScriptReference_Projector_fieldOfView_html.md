* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector-fieldOfView.html

#  [Projector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector.html).fieldOfView
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
fieldOfView; 
### Description
The field of view of the projection in degrees.
This is the vertical field of view; horizontal FOV varies depending on the [aspectRatio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector-aspectRatio.html). Field of view is ignored when projector is orthographic (see [orthographic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector-orthographic.html)). Additional resources: [projector component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Projector.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Get the projector
        Projector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector.html) proj = GetComponent<Projector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector.html)>();
        // Use it
        proj.fieldOfView = 80.0f;
    }
}

```

* * *
