* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.EnableKeyword.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).EnableKeyword
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html "Go to Material Component in the Manual")
## Declaration
public void EnableKeyword(ref [Rendering.LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) keyword); 
## Declaration
public void EnableKeyword(string keyword); 
### Parameters
Parameter | Description  
---|---  
keyword | The [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) to enable.  
keyword | The name of the [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) to enable.  
### Description
Enables a local shader keyword for this material.
Shader keywords determine which shader variants Unity uses. For information on working with [local shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) and [global shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) and how they interact, see [Using shader keywords with C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-scripts.html).  
  
If you pass in a [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) and it does not exist in the [Shader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-keywordSpace.html) for the shader that this material uses, this function has no effect. If you pass a string and a [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) with that `name` does not exist in the [Shader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-keywordSpace.html) for the shader that this material uses, this function has no effect.  
  
The version of this function that takes a string as a parameter is slower than the version that takes a [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html). If you call this function more than once, it is best practice to create a [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) struct, cache it, and use that.  
  
**Note:** A `LocalKeyword` is specific to a single [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) or [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) instance. You cannot use it with other [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) or [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) instances, even if they declare keywords with the same name.  
  
The following example creates a `LocalKeyword` struct with the name `EXAMPLE_FEATURE_ON`, and caches it. It provides functions to enable and disable it.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class MaterialKeywordExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material;
    private LocalKeyword[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) exampleFeatureKeyword;  
  
    void Start()
    {
        // Get the instance of the Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) class that this material uses
        var shader = material.shader;  
  
        // Create and cache the LocalKeyword[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html)
        exampleFeatureKeyword = new LocalKeyword[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html)(shader, "EXAMPLE_FEATURE_ON");
    }  
  
    public void EnableExampleFeature()
    {
        material.EnableKeyword(exampleFeatureKeyword);
    }  
  
    public void DisableExampleFeature()
    {
        material.DisableKeyword(exampleFeatureKeyword);
    }
}

```

Additional resources: [Shader variants and keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-and-keywords.html), [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html), [GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html), [DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.DisableKeyword.html), [SetKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetKeyword.html), [Shader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-keywordSpace.html), [IsKeywordEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.IsKeywordEnabled.html), [enabledKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-enabledKeywords.html), [shaderKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-shaderKeywords.html).
* * *
