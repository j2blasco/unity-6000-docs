* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-operator_Vector2.html

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
Converts a [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) to a Vector4.
Vector2s can be implicitly converted to Vector4 (z and w is set to zero in the result).
```
using UnityEngine;
using System.Collections.Generic;  
  

public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) renderer = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();  
  
        // Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) vectors are always defined as Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html).
        // The value here is converted to a Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) from a Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html).
        renderer.material.SetVector("_SomeVariable", Vector2.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-one.html));
    }
}

```

* * *
