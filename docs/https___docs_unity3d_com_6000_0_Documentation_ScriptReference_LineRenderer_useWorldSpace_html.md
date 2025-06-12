* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer-useWorldSpace.html

#  [LineRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html).useWorldSpace
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html "Go to LineRenderer Component in the Manual")
useWorldSpace; 
### Description
If enabled, the lines are defined in world space.
This means the object's position is ignored, and the lines are rendered around world origin.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Creates a line renderer at the origin with 2 colors.  
  
    void Start()
    {
        LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html) lineRenderer;
        lineRenderer = gameObject.AddComponent<LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html)>();
        lineRenderer.useWorldSpace = false;
        lineRenderer.material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Sprites/Default"));
        lineRenderer.SetColors(Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html));
    }
}

```

* * *
