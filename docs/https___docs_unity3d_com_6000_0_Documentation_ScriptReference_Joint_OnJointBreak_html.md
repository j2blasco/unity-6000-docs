* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint.OnJointBreak.html

#  [Joint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint.html).OnJointBreak(float)
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
### Description
Called when a joint attached to the same game object broke.
When a force that is higher than the breakForce of the joint, the joint will break off. When the joint breaks off, OnJointBreak will be called and the break force applied to the joint will be passed in. After OnJointBreak the joint will automatically be removed from the game object and deleted.  
  
Note: OnJointBreak is called by Unity, it is not a function you can call from a joint.  
  
Additional resources: [Joint.breakForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-breakForce.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnJointBreak(float breakForce)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("A joint has just been broken!, force: " + breakForce);
    }
}

```

* * *
