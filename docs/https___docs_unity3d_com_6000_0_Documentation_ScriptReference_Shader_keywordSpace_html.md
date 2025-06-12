* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-keywordSpace.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).keywordSpace
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
[Rendering.LocalKeywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeywordSpace.html) keywordSpace; 
### Description
The local keyword space of this shader.
Shader keywords determine which shader variants Unity uses. For information on working with [local shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) and [global shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) and how they interact, see [Using shader keywords with C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-scripts.html).  
  
`keywordSpace` contains: 
  * All keywords declared in the source file. For more information, see [Declaring shader keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords#declaring-keywords.html).
  * All keywords declared in dependencies of that source file. This means all Shaders that are included via the [Fallback command](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Fallback.html), and all Passes that are included via the [UsePass command](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UsePass.html).
  * All keywords that Unity adds automatically. For more information, see [Unity's predefined shader keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords#predefined-shader-keywords.html).


This example iterates over the local shader keywords in the local keyword space for a graphics shader. It determines whether they are overridden by a global shader keyword, and prints their state.
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
Additional resources: [Material.EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.EnableKeyword.html), [Material.DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.DisableKeyword.html), [Shader keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords.html).
* * *
