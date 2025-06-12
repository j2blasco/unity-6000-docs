* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-useGravity.html

#  [Cloth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html).useGravity
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
useGravity; 
### Description
Should gravity affect the cloth simulation?
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Example()
    {
        // Dont use gravity on this cloth regardless if is Interactive or Skinned.
        transform.GetComponent<Cloth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html)>().useGravity = false;
    }
}

```

* * *
