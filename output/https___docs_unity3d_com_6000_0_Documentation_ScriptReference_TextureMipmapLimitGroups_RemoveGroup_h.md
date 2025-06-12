* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.RemoveGroup.html

#  [TextureMipmapLimitGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.html).RemoveGroup
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
public static void RemoveGroup(string groupName); 
### Parameters
Parameter | Description  
---|---  
groupName | Name of the texture mipmap limit group to remove.  
### Description
(Editor Only) Attempts to remove a texture mipmap limit group with the indicated `groupName`.
This operation fails and throws an exception if `groupName` is null or there is no texture mipmap limit group named `groupName`. If Unity finds a matching group, Unity removes it from all quality levels.  
  
Unity does not modify textures bound to the removed group. These textures continue to point to the removed group as long as you do not update and re-import them yourself. If you do not adjust the relevant textures, they automatically fall back to the global texture mipmap limit.
```
#if UNITY_EDITOR
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Attempts to remove the texture mipmap limit group "MyGroup", if it exists in the project.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("MyMenu/Remove TextureMipmapLimitGroup")]
    static void RemoveMyGroup()
    {
        const string textureMipmapLimitGroupName = "MyGroup";
        if (TextureMipmapLimitGroups.HasGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.HasGroup.html)(textureMipmapLimitGroupName))
        {
            TextureMipmapLimitGroups.RemoveGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.RemoveGroup.html)(textureMipmapLimitGroupName);
        }
        else
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)($"Cannot remove texture mipmap limit group '{textureMipmapLimitGroupName}' as it does not exist!");
        }
    }
}
#endif

```

Additional resources: [HasGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.HasGroup.html), [CreateGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.CreateGroup.html).
* * *
