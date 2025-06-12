* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-isSupported.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).isSupported
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html "Go to Shader Component in the Manual")
isSupported; 
### Description
Can this shader run on the end-users graphics card? (Read Only)
Returns true if the shader itself or any fallbacks setup in the shader are supported. Most often you use this when implementing special effects.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Disable renderer if material's shader is not supported
        Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();  
  
        if (!rend.material.shader.isSupported)
        {
            rend.enabled = false;
        }
    }
}

```

Additional resources: [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) class, [ShaderLab documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html).
* * *
