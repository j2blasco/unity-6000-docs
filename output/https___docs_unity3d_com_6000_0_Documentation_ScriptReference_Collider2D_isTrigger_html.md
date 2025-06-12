* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-isTrigger.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).isTrigger
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
isTrigger; 
### Description
Is this collider configured as a trigger?
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Collider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) coll;  
  
    // Use this for initialization
    void Start()
    {
        //Check if the isTrigger option on the Collider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is set to true or false
        if (coll.isTrigger)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("This Collider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) can be triggered");
        }
        else if (!coll.isTrigger)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("This Collider2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) cannot be triggered");
        }
    }
}

```

* * *
