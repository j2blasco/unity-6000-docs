* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsShaderLevel.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).graphicsShaderLevel
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
graphicsShaderLevel; 
### Description
Graphics device shader capability level (Read Only).
This is approximate "shader capability" level of the graphics device, expressed in DirectX shader model terms. Possible values are:  
  
**50** Shader Model 5.0 (DX11.0)   
**46** OpenGL 4.1 capabilities (Shader Model 4.0 + tessellation)   
**45** Metal / OpenGL ES 3.1 capabilities (Shader Model 3.5 + compute shaders)   
**40** Shader Model 4.0 (DX10.0)   
**35** OpenGL ES 3.0 capabilities (Shader Model 3.0 + integers, texture arrays, instancing)   
**30** Shader Model 3.0   
**25** Shader Model 2.5 (DX11 feature level 9.3 feature set)   
**20** Shader Model 2.0.  
  
Additional resources: [shader compilation targets](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html).
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Check for shader model 4.5 or better support
        if (SystemInfo.graphicsShaderLevel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsShaderLevel.html) >= 45)
            print("Woohoo, decent shaders supported!");
    }
}

```

* * *
