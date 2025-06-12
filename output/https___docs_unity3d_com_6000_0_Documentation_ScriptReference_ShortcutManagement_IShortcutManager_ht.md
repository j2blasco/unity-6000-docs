* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.html

# IShortcutManager
interface in UnityEditor.ShortcutManagement
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
Represents a manager that configures a particular instance of the shortcuts system.
The manager maintains a list of _available_ profiles which can be retrieved with [GetAvailableProfiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.GetAvailableProfiles.html). Some of the methods require the passed profile ID to be available at the time it is called. Creating a new profile with [CreateProfile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.CreateProfile.html) makes it available and deleting a profile with [DeleteProfile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.DeleteProfile.html) makes it not available anymore.  
  
It also maintains a reference to the _active_ profile ([activeProfileId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager-activeProfileId.html)) which determines the active bindings based on the shortcut overrides of the active profile. [RebindShortcut](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.RebindShortcut.html) and [ClearShortcutOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.ClearShortcutOverride.html) requires the active profile to not be _read-only_ (i.e. [IsProfileReadOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.IsProfileReadOnly.html) returns `false` for [activeProfileId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager-activeProfileId.html)) since these two methods modify the active profile.  
  
Finally, it maintains a list of available shortcuts which can be retrieved with [GetAvailableShortcuts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.GetAvailableShortcuts.html). All methods that take a shortcut ID require that the shortcut is avaliable.
### Properties
Property | Description  
---|---  
[activeProfileId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager-activeProfileId.html) | Gets or sets the ID of the currently active profile.  
### Public Methods
Method | Description  
---|---  
[ClearShortcutOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.ClearShortcutOverride.html) | Clears the binding for shortcut with given shortcut ID from the active profile.  
[CreateProfile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.CreateProfile.html) | Creates a new profile with the given profile ID.  
[DeleteProfile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.DeleteProfile.html) | Deletes profile with the given profile ID.  
[GetAvailableProfileIds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.GetAvailableProfileIds.html) | Returns an enumeration of all of avaliable profile IDs.  
[GetAvailableShortcutIds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.GetAvailableShortcutIds.html) | Returns an enumeration of all available shortcut IDs.  
[GetShortcutBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.GetShortcutBinding.html) | Returns the active binding for the given shortcut ID.  
[IsProfileIdValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.IsProfileIdValid.html) | Checks that the profile ID is valid.  
[IsProfileReadOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.IsProfileReadOnly.html) | Is the profile for the given profile ID read-only?  
[IsShortcutOverridden](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.IsShortcutOverridden.html) | Does the active profile override the binding for the given shortcut ID?  
[RebindShortcut](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.RebindShortcut.html) | Rebinds the shortcut for the given shortcut ID to the given binding in the active profile.  
[RenameProfile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager.RenameProfile.html) | Renames the ID of a profile.  
### Events
Event | Description  
---|---  
[activeProfileChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager-activeProfileChanged.html) | Raised when the ID of the active profile is changed.  
[shortcutBindingChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.IShortcutManager-shortcutBindingChanged.html) | Raised when shortcut overrides are changed on the active profile.  
* * *
