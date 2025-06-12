* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.Create.html

#  [GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html).Create
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
public static [Rendering.GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) Create(string name); 
### Parameters
Parameter | Description  
---|---  
name | The name of the global shader keyword.  
### Returns
**GlobalKeyword** Returns a new instance of the GlobalKeyword class. 
### Description
Creates and returns a [GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) that represents a new or existing global shader keyword.
Unity creates and returns a `GlobalKeyword` struct to represent the global shader keyword with the given name. If a global shader keyword with the given name does not yet exist in Unity's internal list of global shader keywords, Unity adds a global shader keyword with the given name to the list.  
  
The following example creates a `GlobalKeyword` struct with the name `EXAMPLE_FEATURE_ON`, and caches it. It provides functions to enable and disable it.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class GlobalKeywordExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private GlobalKeyword[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) exampleFeatureKeyword;  
  
    private void Start()
    {
        exampleFeatureKeyword = GlobalKeyword.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.Create.html)("EXAMPLE_FEATURE_ON");
    }  
  
    public void EnableExampleFeature()
    {
        Shader.EnableKeyword[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.EnableKeyword.html)(exampleFeatureKeyword);
    }  
  
    public void DisableExampleFeature()
    {
        Shader.DisableKeyword[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.DisableKeyword.html)(exampleFeatureKeyword);
    }
}

```

Additional resources: [Shader variants and keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-and-keywords.html), [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html), [GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html), [EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.EnableKeyword.html), [DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.DisableKeyword.html), [SetKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetKeyword.html), [IsKeywordEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.IsKeywordEnabled.html), [enabledGlobalKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-enabledGlobalKeywords.html), [globalKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-globalKeywords.html).
* * *
