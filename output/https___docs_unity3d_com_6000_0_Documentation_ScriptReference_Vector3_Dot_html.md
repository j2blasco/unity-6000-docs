* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Dot.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).Dot
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
public static float Dot([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) lhs, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) rhs); 
### Description
Dot Product of two vectors.
The dot product is a float value equal to the magnitudes of the two vectors multiplied together and then multiplied by the cosine of the angle between them.  
  
For [normalized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-normalized.html) vectors Dot returns 1 if they point in exactly the same direction, -1 if they point in completely opposite directions and zero if the vectors are perpendicular.
```
// detects if other transform is behind this object  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) other;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (other)
        {
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) forward = transform.TransformDirection(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html));
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) toOther = Vector3.Normalize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Normalize.html)(other.position - transform.position);  
  
            if (Vector3.Dot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Dot.html)(forward, toOther) < 0)
            {
                print("The other transform is behind me!");
            }
        }
    }
}

```

* * *
