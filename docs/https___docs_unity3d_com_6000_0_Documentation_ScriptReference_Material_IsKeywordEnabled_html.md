* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.IsKeywordEnabled.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).IsKeywordEnabled
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
public bool IsKeywordEnabled(ref [Rendering.LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) keyword); 
## Declaration
public bool IsKeywordEnabled(string keyword); 
### Parameters
Parameter | Description  
---|---  
keyword | The [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) to check.  
keyword | The name of the [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) to check.  
### Returns
**bool** Returns `true` if a [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) with the given name is enabled for this material. 
### Description
Checks whether a local shader keyword is enabled for this material.
Shader keywords determine which shader variants Unity uses. For information on working with [local shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) and [global shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) and how they interact, see [Using shader keywords with C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-scripts.html).  
  
If you pass in a [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) and it does not exist in the [Shader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-keywordSpace.html) for the shader that this material uses, this function returns `false`. If you pass a string and a [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) with that `name` does not exist in the [Shader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-keywordSpace.html) for the shader that this material uses, this function returns `false`.  
  
The version of this function that takes a string as a parameter is slower than the version that takes a [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html). If you call this function more than once, it is best practice to create a [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) struct, cache it, and use that.  
  
**Note:** A `LocalKeyword` is specific to a single [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) or [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) instance. You cannot use it with other [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) or [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) instances, even if they declare keywords with the same name.  
  
This example iterates over the local shader keywords in the local keyword space for a material. It determines whether they are overridden by a global shader keyword, and prints their state.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class KeywordExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material;  
  
    void Start()
    {
        CheckShaderKeywordState();
    }  
  
    void CheckShaderKeywordState()
    {
        // Get the instance of the Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) class that the material uses
        var shader = material.shader;  
  
        // Get all the local keywords that affect the Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html)
        var keywordSpace = shader.keywordSpace;  
  
        // Iterate over the local keywords
        foreach (var localKeyword in keywordSpace.keywords)
        {
            // If the local keyword is overridable,
            // and a global keyword with the same name exists and is enabled,
            // then Unity uses the global keyword state
            if (localKeyword.isOverridable && Shader.IsKeywordEnabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.IsKeywordEnabled.html)(localKeyword.name))
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Local keyword with name of " + localKeyword.name + " is overridden by a global keyword, and is enabled");
            }
            // Otherwise, Unity uses the local keyword state
            else
            {
                var state = material.IsKeywordEnabled(localKeyword) ? "enabled" : "disabled";
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Local keyword with name of " + localKeyword.name + " is " + state);
            }
        }
    }
}

```

Additional resources: [Shader variants and keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-and-keywords.html), [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html), [GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html), [EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.EnableKeyword.html), [DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.DisableKeyword.html), [SetKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetKeyword.html), [Shader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-keywordSpace.html), [enabledKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-enabledKeywords.html), [shaderKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-shaderKeywords.html).
* * *
