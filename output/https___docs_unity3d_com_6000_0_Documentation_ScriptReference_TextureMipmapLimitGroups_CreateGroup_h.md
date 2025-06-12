* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.CreateGroup.html

#  [TextureMipmapLimitGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.html).CreateGroup
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
public static void CreateGroup(string groupName); 
### Parameters
Parameter | Description  
---|---  
groupName | Name of the new texture mipmap limit group.  
### Description
(Editor Only) Attempts to create a texture mipmap limit group with the indicated `groupName`.
This operation fails and throws an exception if `groupName` is null/empty or a texture mipmap limit group with the same name already exists. If no other group with the same name exists, Unity creates the new group across all quality levels. By default, the new group mirrors the global texture mipmap limit.  
  
If Unity creates the new group successfully, textures previously bound to `groupName` stop using [QualitySettings.globalTextureMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-globalTextureMipmapLimit.html) as a fallback and begin respecting the new group's [TextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html) instead.
```
#if UNITY_EDITOR
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Attempts to create a texture mipmap limit group with the name "MyGroup", as long as it doesn't exist already.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("MyMenu/Create MipmapLimitGroup")]
    static void CreateMyGroup()
    {
        const string textureMipmapLimitGroup = "MyGroup";
        if (!TextureMipmapLimitGroups.HasGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.HasGroup.html)(textureMipmapLimitGroup))
        {
            TextureMipmapLimitGroups.CreateGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.CreateGroup.html)(textureMipmapLimitGroup);
        }
        else
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)($"Cannot create new texture mipmap limit group '{textureMipmapLimitGroup}', it already exists!");
        }
    }
}
#endif

```

Additional resources: [HasGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.HasGroup.html), [RemoveGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.RemoveGroup.html).
* * *
