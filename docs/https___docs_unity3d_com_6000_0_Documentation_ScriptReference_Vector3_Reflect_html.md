* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Reflect.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).Reflect
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Reflect([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) inDirection, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) inNormal); 
### Parameters
Parameter | Description  
---|---  
inDirection | The direction vector towards the plane.  
inNormal | The normal vector that defines the plane.  
### Description
Reflects a vector off the plane defined by a normal.
This method calculates the reflection vector using the following formula: v = inDirection - 2 * inNormal * dot(inDirection inNormal). The `inNormal` vector defines a plane. A plane's normal is the vector that is perpendicular to its surface. The `inDirection` vector is treated as a directional arrow coming into the plane. The returned value is a vector of equal magnitude to `inDirection` but with its direction reflected.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/Vec3ReflectDiagram.png)  
_Reflection of a vector off a plane._
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) originalObject;
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) reflectedObject;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Makes the reflected object appear opposite of the original object,
        // mirrored along the z-axis of the world
        reflectedObject.position = Vector3.Reflect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Reflect.html)(originalObject.position, Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html));
    }
}

```

* * *
