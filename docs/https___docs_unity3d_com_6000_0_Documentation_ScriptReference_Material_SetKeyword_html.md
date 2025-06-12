* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetKeyword.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).SetKeyword
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
public void SetKeyword(ref [Rendering.LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) keyword, bool value); 
### Parameters
Parameter | Description  
---|---  
keyword | The [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) to enable or disable.  
value | The desired keyword state.  
### Description
Sets the state of a local shader keyword for this material.
Shader keywords determine which shader variants Unity uses. For information on working with [local shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) and [global shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) and how they interact, see [Using shader keywords with C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-scripts.html).  
  
When `value` is `true`, this function calls [EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.EnableKeyword.html). Otherwise, it calls [DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.DisableKeyword.html).  
  
If the [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) does not exist in the [Shader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-keywordSpace.html) for the shader that this material uses, this function has no effect.  
  
The following example creates and caches a `LocalKeyword`, and provides a function to toggle its state.
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
  
    public void ToggleExampleFeature()
    {
        // Get the current state of the local keyword
        bool state = material.IsKeywordEnabled(exampleFeatureKeyword);  
  
        // Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) the state
        material.SetKeyword(exampleFeatureKeyword, !state);
    }
}

```

Additional resources: [Shader variants and keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-and-keywords.html), [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html), [GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html), [EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.EnableKeyword.html), [DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.DisableKeyword.html), [Shader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-keywordSpace.html), [IsKeywordEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.IsKeywordEnabled.html), [enabledKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-enabledKeywords.html), [shaderKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-shaderKeywords.html).
* * *
