* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Quad.html

#  [PrimitiveType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.html).Quad
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
A quad primitive.
Additional resources: [GameObject.CreatePrimitive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html).
```
using UnityEngine;
using System.Collections;  
  
// Creates a quad primitive  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) quad = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Quad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Quad.html));
    }
}

```

* * *
