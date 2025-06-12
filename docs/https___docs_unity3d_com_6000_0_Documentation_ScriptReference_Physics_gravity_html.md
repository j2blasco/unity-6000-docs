* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-gravity.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).gravity
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) gravity; 
### Description
The gravity applied to all rigid bodies in the Scene.
Gravity can be turned off for an individual rigidbody using its [useGravity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-useGravity.html) property.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Example()
    {
        Physics.gravity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-gravity.html) = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, -1.0F, 0);
    }
}

```

ParticleSystem.gravityModifiers is Obsolete.
* * *
