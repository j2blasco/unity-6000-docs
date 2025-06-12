* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.html

# TextureMipmapLimitGroups
class in UnityEngine
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
Script interface for texture mipmap limit groups.
Use this class to add, remove or detect texture mipmap limit groups in C#.  
  
Additional resources: [TextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html), [QualitySettings.globalTextureMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-globalTextureMipmapLimit.html).
### Static Methods
Method | Description  
---|---  
[CreateGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.CreateGroup.html) | (Editor Only) Attempts to create a texture mipmap limit group with the indicated groupName.  
[GetGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.GetGroups.html) | Retrieves a string array containing the name of all texture mipmap limit groups available in the project.  
[HasGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.HasGroup.html) | Checks whether a texture mipmap limit group with the indicated groupName exists in the project. This operation fails and throws an exception if groupName is null.  
[RemoveGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.RemoveGroup.html) | (Editor Only) Attempts to remove a texture mipmap limit group with the indicated groupName.  
* * *
