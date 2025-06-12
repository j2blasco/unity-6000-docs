* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask-value.html

#  [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html).value
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
value; 
### Description
Converts a layer mask value to an integer value.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Casts a ray using the layer mask,
    // which can be modified in the inspector.  
  
    LayerMask[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) mask = -1;
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(transform.position, transform.forward, 100, mask.value))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Hit something");
        }
    }
}

```

* * *
