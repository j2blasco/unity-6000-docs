* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-operator_Vector3.html

#  [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html).Vector4
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
Converts a [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) to a Vector4.
Vector3s can be implicitly converted to Vector4 (w is set to zero in the result).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // color as a Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) (red, green, blue)
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) color = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1.0f, 0.25f, 0f);  
  
        // This converts the Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) to a Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) with the w parameter set to 0
        Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) colorWithOpacity = color;
        // set the opacity in the w parameter
        colorWithOpacity.w = 0.75f;
    }
}

```

* * *
