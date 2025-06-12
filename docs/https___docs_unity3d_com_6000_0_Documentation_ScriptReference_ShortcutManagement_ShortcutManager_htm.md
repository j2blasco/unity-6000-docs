* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutManager.html

# ShortcutManager
class in UnityEditor.ShortcutManagement
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
Provides access to an instance of [IShortcutManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.html) for managing shortcuts.
### Static Properties
Property | Description  
---|---  
[defaultProfileId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutManager-defaultProfileId.html) | A constant defining the ID of the default shortcut profile. See the documentation for the IShortcutManager.activeProfileId property.  
[instance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutManager-instance.html) | An instance of the IShortcutManager interface used for managing shortcuts in the editor.  
### Static Methods
Method | Description  
---|---  
[RegisterContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutManager.RegisterContext.html) | Registers a IShortcutContext as a custom context used to filter shortcuts.  
[RegisterTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutManager.RegisterTag.html) | Registers the tag as a custom context used to filter shortcuts after a window context is determined.  
[UnregisterContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutManager.UnregisterContext.html) | Removes a IShortcutContext from the shortcut context list.  
[UnregisterTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutManager.UnregisterTag.html) | Removes a tag from the custom context list.  
* * *
