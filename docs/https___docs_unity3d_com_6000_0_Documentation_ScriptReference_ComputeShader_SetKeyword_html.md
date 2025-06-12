* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetKeyword.html

#  [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).SetKeyword
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html "Go to ComputeShader Component in the Manual")
## Declaration
public void SetKeyword(ref [Rendering.LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) keyword, bool value); 
### Parameters
Parameter | Description  
---|---  
keyword | The [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) keyword to enable or disable.  
value | The desired keyword state.  
### Description
Sets the state of a local shader keyword for this compute shader.
Shader keywords determine which shader variants Unity uses. For information on working with [local shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) and [global shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) and how they interact, see [Using shader keywords with C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-scripts.html).  
  
When `value` is `true`, this function calls [EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.EnableKeyword.html). Otherwise, it calls [DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.DisableKeyword.html).  
  
If the [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) does not exist in the [keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-keywordSpace.html), this function has no effect.  
  
The following example toggles the state of all local shader keywords in a compute shader.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public ComputeShader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader;  
  
    void Start()
    {
        // Get all the local keywords that affect the Compute Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html)
        var keywordSpace = computeShader.keywordSpace;  
  
        // Iterate over the local keywords
        foreach (var localKeyword in keywordSpace.keywords)
        {
            // Get the current state of the local keyword
            bool state = computeShader.IsKeywordEnabled(localKeyword);  
  
            // Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) the state
            computeShader.SetKeyword(localKeyword, !state);
        }
    }
}

```

Additional resources: [Shader variants and keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-and-keywords.html), [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html), [GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html), [EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.EnableKeyword.html), [DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.DisableKeyword.html), [keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-keywordSpace.html), [IsKeywordEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.IsKeywordEnabled.html), [enabledKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-enabledKeywords.html), [shaderKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-shaderKeywords.html).
* * *
