* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-width.html

#  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).width
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
width; 
### Description
Width of the Texture in pixels (Read Only).
This value is the width of the Texture at the highest resolution that [PlayerSettings.mipStripping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-mipStripping.html) allows.  
  
In the Unity Editor, this returns the width of the Texture at full resolution.  
  
At run time, if [PlayerSettings.mipStripping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-mipStripping.html) is disabled, this returns the width of the Texture at full resolution. If [PlayerSettings.mipStripping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-mipStripping.html) is enabled, this returns the width of the Texture at the highest resolution that has not been stripped.  
  
Additional resources: [QualitySettings.globalTextureMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-globalTextureMipmapLimit.html), [PlayerSettings.mipStripping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-mipStripping.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Print Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) size to the Console
    Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html);
    void Start()
    {
        print("Size is " + Texture.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-width.html) + " by " + Texture.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-height.html));
    }
}

```

* * *
