* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.RotateAround.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).RotateAround
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html "Go to Transform Component in the Manual")
## Declaration
public void RotateAround([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) axis, float angle); 
### Description
Rotates the transform about `axis` passing through `point` in world coordinates by `angle` degrees.
This modifies both the position and the rotation of the transform.
```
using UnityEngine;  
  
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to rotate around the target position.
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Assign a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in the Inspector to rotate around
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) target;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Spin the object around the target at 20 degrees/second.
        transform.RotateAround(target.transform.position, Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html), 20 * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html));
    }
}

```

* * *
