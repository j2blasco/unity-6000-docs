* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.ClampMagnitude.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).ClampMagnitude
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) ClampMagnitude([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) vector, float maxLength); 
### Description
Returns a copy of `vector` with its magnitude clamped to `maxLength`.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Move the object around with the arrow keys but confine it
    // to a given radius around a center point.  
  
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) centerPt;
    public float radius;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Get the new position for the object.
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) movement = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Horizontal"), 0, Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Vertical"));
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) newPos = transform.position + movement;  
  
        // Calculate the distance of the new position from the center point. Keep the direction
        // the same but clamp the length to the specified radius.
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) offset = newPos - centerPt;
        transform.position = centerPt + Vector3.ClampMagnitude[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.ClampMagnitude.html)(offset, radius);
    }
}

```

* * *
