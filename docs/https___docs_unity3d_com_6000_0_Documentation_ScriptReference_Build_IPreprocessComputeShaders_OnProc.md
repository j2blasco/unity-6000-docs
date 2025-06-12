* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPreprocessComputeShaders.OnProcessComputeShader.html

#  [IPreprocessComputeShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPreprocessComputeShaders.html).OnProcessComputeShader
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
public void OnProcessComputeShader([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) shader, string kernelName, IList<ShaderCompilerData> data); 
### Parameters
Parameter | Description  
---|---  
shader | The compute shader that Unity is about to compile.  
kernelName | The name of the kernel that Unity is about to compile.  
data | The list of shader variants that Unity is about to compile.  
### Description
Implement this interface to receive a callback before Unity compiles a compute shader kernel into a build.
Use this callback to examine the compute shader variants that Unity is about to compile into your build, and exclude any variant that you do not want. Excluding unwanted shader variants can reduce build size and build times.  
  
Variants are represented by [ShaderCompilerData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderCompilerData.html) structs. For each variant, you can check whether given global or local keywords are enabled using [ShaderKeywordSet.IsEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeywordSet.IsEnabled.html).  
  
To check whether a variant has a global keyword enabled, create a [ShaderKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword.html) instance with the name of the global keyword. To check whether a variant has a local keyword enabled, create a [ShaderKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword.html) instance with the name of the local keyword and an additional parameter that specifies the compute shader that uses the local keyword.  
  
To exclude a shader variant from the build, directly remove the elements from `data` . Note that removing elements individually in a for loop can be slow; if you are removing a lot of elements, consider moving the unwanted elements to the end of the List and then removing them all in a single operation.  
  
Note that this callback only provides details of compute shaders. To see regular shaders that Unity is about to compile into the build, see [IPreprocessShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPreprocessShaders.html) .  
  
This callback is invoked for both Player and AssetBundle builds.  
  
Additional resources: [Shader variants and keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-and-keywords.html), [Declaring and using shader keywords in HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants.html), [BuildPipeline.BuildPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html), [BuildPipeline.BuildAssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html).
```
using System.Collections.Generic;
using UnityEditor.Build;
using UnityEditor.Rendering;
using UnityEngine;
using UnityEngine.Rendering;  
  
class MyCustomBuildProcessor : IPreprocessComputeShaders[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPreprocessComputeShaders.html)
{
    ShaderKeyword[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword.html) m_GlobalKeywordBlue;  
  
    public MyCustomBuildProcessor()
    {
        // Global keywords are shader agnostic so they can be initialized early
        m_GlobalKeywordBlue = new ShaderKeyword[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword.html)("_BLUE");
    }  
  
    public int callbackOrder { get { return 0; } }  
  
    public void OnProcessComputeShader(ComputeShader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) shader, string kernelName, IList<ShaderCompilerData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderCompilerData.html)> data)
    {
        // Local keywords are initialized here as their constructor needs to specify the shader
        ShaderKeyword[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword.html) localKeywordRed = new ShaderKeyword[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword.html)(shader, "_RED");
        for (int i = data.Count - 1; i >= 0; --i)
        {
            // Variants with global keyword _BLUE disabled are included in the build
            if (!data[i].shaderKeywordSet.IsEnabled(m_GlobalKeywordBlue))
                continue;  
  
            // Variants with local keyword _RED disabled are included in the build
            if (!data[i].shaderKeywordSet.IsEnabled(localKeywordRed))
                continue;  
  
            // Any variants that do not meet the criteria above are stripped from the build.
            // In this example, Unity strips variants that have both _BLUE and _RED keywords enabled.
            data.RemoveAt(i);
        }
    }
}

```

* * *
