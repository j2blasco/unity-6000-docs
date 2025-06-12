* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html

# TextureMipmapLimitSettings
struct in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Structure that represents texture mipmap limit settings.
This code example illustrates how to modify [TextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html) from script.
```
#if UNITY_EDITOR
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("MyMenu/Modify MyGroup")]
    static void ModifyMyGroup()
    {
        const string textureMipmapLimitGroupName = "MyGroup";
        if (TextureMipmapLimitGroups.HasGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.HasGroup.html)(textureMipmapLimitGroupName))
        {
            TextureMipmapLimitSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html) settings = QualitySettings.GetTextureMipmapLimitSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetTextureMipmapLimitSettings.html)(textureMipmapLimitGroupName);  
  
            // For the currently active quality level, this group will now offset the Global Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) Mipmap Limit. (default behavior)
            settings.limitBiasMode = TextureMipmapLimitBiasMode.OffsetGlobalLimit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitBiasMode.OffsetGlobalLimit.html);  
  
            // Drop 1 extra mip. Assuming that the limitBias is now 1 and that the Global Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) Mipmap Limit is 1 as well (for example), then textures assigned to 'MyGroup' drop 2 mips in total.
            settings.limitBias++;  
  
            QualitySettings.SetTextureMipmapLimitSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.SetTextureMipmapLimitSettings.html)(textureMipmapLimitGroupName, settings);
        }
        else
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)($"Failed to modify settings, could not find texture mipmap limit group '{textureMipmapLimitGroupName}'!");
        }
    }
}
#endif

```

Additional resources: [TextureMipmapLimitGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.html), [QualitySettings.GetTextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetTextureMipmapLimitSettings.html), [QualitySettings.SetTextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.SetTextureMipmapLimitSettings.html).
### Properties
Property | Description  
---|---  
[limitBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings-limitBias.html) | The new value to apply on top of the global texture mipmap limit. Can act as an offset (default) or an override to it.  
[limitBiasMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings-limitBiasMode.html) | Indicates whether the limitBias functions as an offset to the global texture mipmap limit or, instead, acts as an override to it.  
* * *
