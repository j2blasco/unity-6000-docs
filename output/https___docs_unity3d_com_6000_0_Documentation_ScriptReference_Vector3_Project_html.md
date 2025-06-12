* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Project.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).Project
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Project([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) vector, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) onNormal); 
### Description
Projects a vector onto another vector.
To understand vector projection, imagine that `onNormal` is resting on a line pointing in its direction. Somewhere along that line will be the nearest point to the tip of `vector`. The projection is just `onNormal` rescaled so that it reaches that point on the line.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/Vec3ProjectDiagram.png)  
  
The function will return a zero vector if `onNormal` is almost zero.  
  
An example of the usage of projection is a rail-mounted gun that should slide so that it gets as close as possible to a target object. The projection of the target heading along the direction of the rail can be used to move the gun by applying a force to a rigidbody, say.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Slide(Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target, Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) railDirection)
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) heading = target.position - transform.position;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) force = Vector3.Project[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Project.html)(heading, railDirection);  
  
        GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>().AddForce(force);
    }
}

```

* * *
