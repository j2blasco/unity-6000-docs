* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-position.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).position
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html "Go to Rigidbody Component in the Manual")
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position; 
### Description
The position of the rigidbody.
[Rigidbody.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-position.html) allows you to get and set the position of a Rigidbody using the physics engine. If you change the position of a Rigidbody using [Rigidbody.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-position.html), the transform will be updated after the next physics simulation step. This is faster than updating the position using [Transform.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html), as the latter will cause all attached Colliders to recalculate their positions relative to the Rigidbody.  
  
If you want to continuously move a rigidbody use [Rigidbody.MovePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.MovePosition.html) instead, which takes interpolation into account.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>().position = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
    }
}

```

* * *
