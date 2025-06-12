* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDrawGizmosSelected.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnDrawGizmosSelected()
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Description
Implement [OnDrawGizmosSelected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDrawGizmosSelected.html) to draw a gizmo if the object is selected.
[Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html) are drawn only when the object is selected. Gizmos are not pickable. This is used to ease setup. For example an explosion script could draw a sphere showing the explosion radius.
```
using UnityEngine;  
  
public class GizmoTest : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float explosionRadius = 5.0f;  
  
    void OnDrawGizmosSelected()
    {
        // Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) the explosion radius when selected
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(1, 1, 0, 0.75F);
        Gizmos.DrawSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawSphere.html)(transform.position, explosionRadius);
    }
}

```

Additional resources: [OnDrawGizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDrawGizmos.html).
* * *
