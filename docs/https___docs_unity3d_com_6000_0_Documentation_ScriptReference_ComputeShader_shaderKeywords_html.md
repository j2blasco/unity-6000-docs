* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-shaderKeywords.html

#  [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).shaderKeywords
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
shaderKeywords; 
### Description
An array containing names of the local shader keywords that are currently enabled for this compute shader.
Shader keywords determine which shader variants Unity uses. For information on working with [local shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) and [global shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) and how they interact, see [Using shader keywords with C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-scripts.html).  
  
**Note:** It is more efficient to use [enabledKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-enabledKeywords.html), which returns an array of [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) structs.  
  
This example prints the names of all currently enabled local shader keywords for a compute shader.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public ComputeShader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader;  
  
    private void Start()
    {
        foreach (var localKeywordName in computeShader.shaderKeywords)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Local shader keyword " + localKeywordName + " is currently enabled");
        }
    }
}

```

Additional resources: [Shader variants and keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-and-keywords.html), [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html), [GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html), [EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.EnableKeyword.html), [DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.DisableKeyword.html), [SetKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetKeyword.html), [keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-keywordSpace.html), [IsKeywordEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.IsKeywordEnabled.html), [enabledKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-enabledKeywords.html).
* * *
