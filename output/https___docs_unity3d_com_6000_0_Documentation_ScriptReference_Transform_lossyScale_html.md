* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-lossyScale.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).lossyScale
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) lossyScale; 
### Description
The global scale of the object (Read Only).
Please note that if you have a parent transform with scale and a child that is arbitrarily rotated, the scale will be skewed. Thus scale can not be represented correctly in a 3 component vector but only a 3x3 matrix. Such a representation is quite inconvenient to work with however. lossyScale is a convenience property that attempts to match the actual world scale as much as it can. If your objects are not skewed the value will be completely correct and most likely the value will not be very different if it contains skew too.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        print(transform.lossyScale);
    }
}

```

* * *
