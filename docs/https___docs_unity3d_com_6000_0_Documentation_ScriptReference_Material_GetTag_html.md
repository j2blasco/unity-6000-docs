* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetTag.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).GetTag
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
public string GetTag(string tag, bool searchFallbacks); 
## Declaration
public string GetTag(string tag, bool searchFallbacks, string defaultValue); 
### Description
Get the value of material's shader tag.
If the material's shader does not define the tag, `defaultValue` is returned.  
  
If `searchFallbacks` is `true` then this function will look for tag in all subshaders and all fallbacks. If `searchFallbacks` is `false` then only the currently used subshader will be queried for the tag.  
  
Using `GetTag` without searching through fallbacks makes it possible to detect which subshader is currently being used: add a custom tag to each subshader with different value, and query the value at run time. For example, Unity water uses this function to detect when the shader falls back to non-reflective one, and turns off reflection camera in that case.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Attach this to a gameObject that has a renderer.  
  
    string materialTag = "RenderType";  
  
    void Start()
    {
        Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
        string result = rend.material.GetTag(materialTag, true, "Nothing");  
  
        if (result == "Nothing")
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)(materialTag + " not found in " + rend.material.shader.name);
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Tag found!, its value: " + result);
        }
    }
}
```

* * *
