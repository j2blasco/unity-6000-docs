* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localPosition.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).localPosition
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) localPosition; 
### Description
Position of the transform relative to the parent transform.
If the transform has no parent, it is the same as [Transform.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Example()
    {
        // Move the object to the same position as the parent:
        transform.localPosition = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 0);  
  
        // Get the y component of the position relative to the parent
        // and print it to the Console
        print(transform.localPosition.y);
    }
}

```

Note that the parent transform's world rotation and scale are applied to the local position when calculating the world position. This means that while 1 unit in [Transform.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html) is always 1 unit, 1 unit in [Transform.localPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localPosition.html) will get scaled by the scale of all ancestors.
* * *
