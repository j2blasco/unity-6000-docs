* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray-ctor.html

# Ray Constructor
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
## Declaration
public Ray([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) origin, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction); 
### Description
Creates a ray starting at `origin` along `direction`.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Create a ray from the transform position along the transform's z-axis
        Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray = new Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html)(transform.position, transform.forward);
    }
}

```

* * *
