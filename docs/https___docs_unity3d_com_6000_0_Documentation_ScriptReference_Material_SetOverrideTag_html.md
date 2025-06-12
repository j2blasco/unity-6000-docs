* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetOverrideTag.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).SetOverrideTag
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
public void SetOverrideTag(string tag, string val); 
### Parameters
Parameter | Description  
---|---  
tag | Name of the tag to set.  
val | Name of the value to set. Empty string to clear the override flag.  
### Description
Sets an override tag/value on the material.
Will set a tag/value on the material that overrides the value of said tag from the shader. This can be used to make sure replacement shaders (such as rendering DepthNormals) work even if the original shader only supports a certain render type. For example if a shader only supports a specific render type but renders in many ways using keywords, SetOverrideTag can be used fom a custom material inspector to ensure that the material renders correctly even if the shader is replaced. Note that overriding the LightMode tag has no effect.
```
using UnityEngine;  
  
public static class MaterialUtils
{
    public enum BlendMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendMode.html)
    {
         Opaque,
         Cutout,
         Fade,
         Transparent
    }  
  
    public static void SetupBlendMode(Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, BlendMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendMode.html) blendMode)
    {
        switch (blendMode)
        {
            case BlendMode.Opaque:
                material.SetOverrideTag("RenderType", "");
                material.DisableKeyword("_ALPHATEST_ON");
                material.renderQueue = -1;
                break;
            case BlendMode.Cutout:
                material.SetOverrideTag("RenderType", "TransparentCutout");
                material.EnableKeyword("_ALPHATEST_ON");
                material.renderQueue = 2450;
                break;
        }
    }
}

```

* * *
