* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager-shortcutBindingChanged.html

#  [IShortcutManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.html).shortcutBindingChanged
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
value | Shortcut binding changed event handler.  
### Description
Raised when shortcut overrides are changed on the active profile.
This event is raised when the shortcut overrides are changed on the active profile, e.g. via [RebindShortcut](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.RebindShortcut.html) or [ClearShortcutOverrides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.ClearShortcutOverrides.html). It is not raised when shortcut overrides change in response to changing the active profile changed (use [activeProfileChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager-activeProfileChanged.html) instead).
* * *
