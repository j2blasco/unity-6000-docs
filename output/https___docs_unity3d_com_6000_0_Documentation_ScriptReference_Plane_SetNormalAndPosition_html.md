* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.SetNormalAndPosition.html

#  [Plane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html).SetNormalAndPosition
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
public void SetNormalAndPosition([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) inNormal, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) inPoint); 
### Parameters
Parameter | Description  
---|---  
inNormal | The plane's normal vector.  
inPoint | A point that lies on the plane.  
### Description
Sets a plane using a point that lies within it along with a normal to orient it.
Note that the normal must be a _normalised_ vector.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float fieldLength;
    public float fieldWidth;
    public Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html) goalLine1;
    public Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html) goalLine2;
    public Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html) leftSideLine;
    public Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html) rightSideLine;  
  
    void Start()
    {
        // Set up goal lines of a playing field.
        goalLine1.SetNormalAndPosition(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html), Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html) * fieldLength / 2);
        goalLine1.SetNormalAndPosition(-Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html), -Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html) * fieldLength / 2);  
  
        // Set up side lines.
        leftSideLine.SetNormalAndPosition(-Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html), -Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html) * fieldWidth / 2);
        rightSideLine.SetNormalAndPosition(Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html), Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html) * fieldWidth / 2);
    }
}

```

Additional resources: [Set3Points](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.Set3Points.html).
* * *
