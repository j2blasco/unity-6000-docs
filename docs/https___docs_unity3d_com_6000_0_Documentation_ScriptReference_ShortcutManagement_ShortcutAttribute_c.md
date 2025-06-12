* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutAttribute-ctor.html

# ShortcutAttribute Constructor
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
public ShortcutAttribute(string id, Type context = null); 
## Declaration
public ShortcutAttribute(string id, Type context, [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html) defaultKeyCode, [ShortcutManagement.ShortcutModifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutModifiers.html) defaultShortcutModifiers = None); 
## Declaration
public ShortcutAttribute(string id, [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html) defaultKeyCode, [ShortcutManagement.ShortcutModifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutModifiers.html) defaultShortcutModifiers = None); 
## Declaration
public ShortcutAttribute(string id, Type context, string tag, [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html) defaultKeyCode, [ShortcutManagement.ShortcutModifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutModifiers.html) defaultShortcutModifiers = None); 
## Declaration
public ShortcutAttribute(string id, Type context, string tag, [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html) defaultKeyCode, [ShortcutManagement.ShortcutModifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutModifiers.html) defaultShortcutModifiers = None, int priority); 
### Parameters
Parameter | Description  
---|---  
id | Shortcut ID.  
context | Optional shortcut context type.  
defaultKeyCode | Optional key code for default binding.  
defaultShortcutModifiers | Optional shortcut modifiers for default binding.  
tag | Optional custom context used to filter shortcuts after window context is determined.  
priority | Optional priority for adjusting order position in Helper Bar.  
### Description
Creates an attribute for an _action shortcut_ with an ID, optional context, and optional default binding.
An action shortcut is triggered when the binding for the shortcut is pressed down. The method on which this attribute is placed must either take no arguments or a single argument of type [ShortcutArguments](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutArguments.html).  
  
You can bind a [ClutchShortcutAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ClutchShortcutAttribute.html) and a [ShortcutAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutAttribute.html) to the same mouse button. In this case, the action shortcut triggers when the mouse button is released.  
  
The ID is used to display the shortcut in the configuration interface unless the optional displayName property is set. Use a forward slash group multiple shortcuts together in the configuration interface, e.g. "MyWindow/Shortcut1" and "MyWindow/Shortcut2".
* * *
