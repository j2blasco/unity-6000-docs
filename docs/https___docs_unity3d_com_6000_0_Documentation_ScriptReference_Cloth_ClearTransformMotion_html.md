* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.ClearTransformMotion.html

#  [Cloth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html).ClearTransformMotion
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cloth.html "Go to Cloth Component in the Manual")
## Declaration
public void ClearTransformMotion(); 
### Description
Clear the pending transform changes from affecting the cloth simulation.
When the transform of a cloth changes, the cloth will not directly follow that change, but instead, the new positions of the SkinnedMeshRenderer's vertices will affect the cloth through the configured constraints in the next cloth simulation update, so that moving the tranform will result in realistic motion of the cloth.  
  
You can call ClearTransformMotion on the cloth to change this behavior. Calling ClearTransformMotion will move the cloth simulation particles along with the transform, so that the transform movement has no effect on the cloth simulation. This is useful if you want to teleport Characters from one point in the Scene to another, without having the cloth suddenly jerk into place.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) newPosition;  
  
    void Start()
    {
        transform.position = newPosition;
        GetComponent<Cloth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html)>().ClearTransformMotion();
    }
}

```

* * *
