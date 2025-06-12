* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawWireSphere.html

#  [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html).DrawWireSphere
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
## Declaration
public static void DrawWireSphere([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, float radius); 
### Description
Draws a wireframe sphere with `center` and `radius`.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float explosionRadius = 5.0f;  
  
    void OnDrawGizmosSelected()
    {
        // Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) the explosion radius when selected
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);
        Gizmos.DrawWireSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawWireSphere.html)(transform.position, explosionRadius);
    }
}

```

* * *
