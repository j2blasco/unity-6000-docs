* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager-activeProfileChanged.html

#  [IShortcutManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.html).activeProfileChanged
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
### Parameters
Parameter | Description  
---|---  
value | Active profile changed event handler.  
### Description
Raised when the ID of the active profile is changed.
This event is raised when the active profile is changed, e.g. when [activeProfileId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager-activeProfileId.html) changes. It is not raised when the shortcut overrides of the active profile are changed, e.g. via [RebindShortcut](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.RebindShortcut.html) or [ClearShortcutOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.ClearShortcutOverride.html).
* * *
