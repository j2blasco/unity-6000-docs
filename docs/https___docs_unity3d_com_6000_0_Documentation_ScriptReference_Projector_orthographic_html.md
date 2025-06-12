* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector-orthographic.html

#  [Projector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector.html).orthographic
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
orthographic; 
### Description
Is the projection orthographic (_true_) or perspective (_false_)?
When orthographic is _true_ , projection is defined by [orthographicSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector-orthographicSize.html).  
When orthographic is _false_ , projection is defined by [fieldOfView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector-fieldOfView.html). Additional resources: [projector component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Projector.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Projector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector.html) proj = GetComponent<Projector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector.html)>();
        proj.orthographic = true;
    }
}

```

* * *
