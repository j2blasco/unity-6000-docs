* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-zero.html

#  [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html).zero
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
[Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) zero; 
### Description
Returns a matrix with all elements set to zero (Read Only).
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // will print:
        // 0.00000 0.00000 0.00000 0.00000
        // 0.00000 0.00000 0.00000 0.00000
        // 0.00000 0.00000 0.00000 0.00000
        // 0.00000 0.00000 0.00000 0.00000
        var matrix = Matrix4x4.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-zero.html);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(matrix);
    }
}

```

Additional resources: [Matrix4x4.identity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-identity.html) property.
* * *
