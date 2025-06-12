* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ClutchShortcutAttribute.html

# ClutchShortcutAttribute
class in UnityEditor.ShortcutManagement
/
Inherits from:[ShortcutManagement.ShortcutAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutAttribute.html)
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
Registers a static method as the action for a clutch shortcut.
A clutch shortcut is triggered when the user presses the key binding for the shortcut and also when the user releases the key. The method on which this attribute is placed must take a single argument of type [ShortcutArguments](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutArguments.html).  
  
You can bind a [ClutchShortcutAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ClutchShortcutAttribute.html) and a [ShortcutAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutAttribute.html) to the same mouse button. In this case, the clutch shortcut triggers when the mouse button is slightly dragged and also when it is released.
### Constructors
Constructor | Description  
---|---  
[ClutchShortcutAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ClutchShortcutAttribute-ctor.html) | Creates an attribute for a clutch shortcut with an ID, optional context, and optional default binding.  
### Inherited Members
### Properties
Property | Description  
---|---  
[displayName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutAttribute-displayName.html) | Optional override of the Shortcut ID when listing the Shortcut in the configuration interface.  
* * *
