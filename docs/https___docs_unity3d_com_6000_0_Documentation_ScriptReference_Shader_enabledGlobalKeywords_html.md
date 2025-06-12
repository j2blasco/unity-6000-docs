* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-enabledGlobalKeywords.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).enabledGlobalKeywords
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
enabledGlobalKeywords; 
### Description
An array containing the global shader keywords that are currently enabled.
Shader keywords determine which shader variants Unity uses. For information on working with [local shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) and [global shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) and how they interact, see [Using shader keywords with C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-scripts.html).  
  
This example prints the names of all currently enabled global shader keywords.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private void Start()
    {
        foreach (var globalKeyword in Shader.enabledGlobalKeywords[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-enabledGlobalKeywords.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Global shader keyword " + globalKeyword.name + " is currently enabled");
        }
    }
}

```

Additional resources: [Shader variants and keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-and-keywords.html), [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html), [GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html), [EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.EnableKeyword.html), [DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.DisableKeyword.html), [SetKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetKeyword.html), [IsKeywordEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.IsKeywordEnabled.html), [globalKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-globalKeywords.html).
* * *
