* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-scripts.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Changing how shaders work using keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants.html)
  * Toggle shader keywords in a script


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-material-inspector.html)
Toggle shader keywords in the Editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants-shortcuts.html)
Add built-in keyword sets
# Toggle shader keywords in a script
Use a C# script to enable or disable keywords, and check whether a keyword has local or global scope.
## Toggle a keyword
To change the state of a keyword, use the `Material` API. For example, `Material.EnableKeyword()`.
## Toggle keywords in multiple shaders
By default, HLSL **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) keywords have global scope. As a result, to toggle keywords with the same name across multiple shaders, you can use a C# global keyword object.
Follow these steps:
  1. Create a [`GlobalKeyword`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) object with the same name as the keywords you want to enable or disable.
  2. Use the [`Shader`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) API to enable or disable the global keyword, which adjusts the HLSL keyword with the same name in all shaders. For example, [`Shader.EnableKeyword`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.EnableKeyword.html).


**Note:** When you create a new `GlobalKeyword`, Unity updates its internal mapping between global and local keyword space for all loaded shaders. This can be a CPU-intensive operation. To reduce the impact of this operation, try to create all global keywords after application startup, while your application is loading.
### Prevent global keyword objects affecting shaders
To prevent global keyword objects affecting shader keywords, give the shader keyword local scope instead of global scope. 
Add `_local` to the keyword directive. For example:
```
#pragma shader_feature_local RED

```

Now the shader isn’t affected by global `Shader` APIs. You can only enable or disable the keyword using `Material` APIs like `Material.EnableKeyword()`.
**Note:** If you use [Fallback](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Fallback.html) or [UsePass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UsePass.html) in a shader, its keyword scope overrides the keyword scopes of the referenced shaders.
## Check the scope of a keyword
To check the scope of a keyword in a shader, select the shader in the **Project** window, then in the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window open the **Keywords** dropdown. Unity displays keywords with global scope under **Overridable** , and keywords with local scope under **Not Overridable**. 
You can also use the [LocalKeyword.isOverridable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword-isOverridable.html) API. 
**Note:** The term `Local` in `LocalKeyword` means the API represents an HLSL keyword rather than a C# keyword object. It doesn’t relate to the scope of the keyword.
To check if a keyword is enabled, do the following:
  * If the keyword is overridable, check whether a C# global keyword with the same name exists. If so, check the state of the keyword using the `Shader` API. For example, `Shader.IsKeywordEnabled()`.
  * If the keyword isn’t overridable, check the state of a keyword using the `Material` API. For example, `Material.IsKeywordEnabled()`.


This following code demonstrates how to check whether Unity considers a keyword enabled or disabled for a material:
```
using UnityEngine;
using UnityEngine.Rendering;

public class KeywordExample : MonoBehaviour
{
    public Material material;

    void Start()
    {
        CheckShaderKeywordState();
    }

    void CheckShaderKeywordState()
    {
        // Get the instance of the Shader class that the material uses
        var shader = material.shader;

        // Get all the local keywords that affect the Shader
        var keywordSpace = shader.keywordSpace;

        // Iterate over the local keywords
        foreach (var localKeyword in keywordSpace.keywords)
        {
            // If the local keyword is overridable (i.e., it was declared with a global scope),
            // and a global keyword with the same name exists and is enabled,
            // then Unity uses the global keyword state
            if (localKeyword.isOverridable && Shader.IsKeywordEnabled(localKeyword.name))
            {
                Debug.Log("Local keyword with name of " + localKeyword.name + " is overridden by a global keyword, and is enabled");
            }
            // Otherwise, Unity uses the local keyword state
            else
            {
                var state = material.IsKeywordEnabled(localKeyword) ? "enabled" : "disabled";
                Debug.Log("Local keyword with name of " + localKeyword.name + " is " + state);
            }            
        }
    }
}


```

## Change a keyword with a command buffer
To enable or disable a local or global keyword with a Command Buffer, use [`CommandBuffer.EnableKeyword`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.EnableKeyword.html) or [`CommandBuffer.DisableKeyword`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DisableKeyword.html).
## Additional resources
  * [Shader Graph Keywords](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest?subfolder=/manual/Keywords.html)
  * [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) API


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-material-inspector.html)
Toggle shader keywords in the Editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants-shortcuts.html)
Add built-in keyword sets
