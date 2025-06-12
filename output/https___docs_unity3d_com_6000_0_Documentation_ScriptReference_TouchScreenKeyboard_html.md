* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.html

# TouchScreenKeyboard
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
Interface for on-screen keyboards. Only native iPhone, Android, and Windows Store Apps are supported.
This interface allows to display different types of the keyboard: ASCII, Numbers, URL, Email, and others.  
  
Because the appearance of the keyboard has the potential to obscure portions of your user interface, it is up to you to make sure that parts of your user interface are not obscured when the keyboard is being displayed.  
  
`TouchScreenKeyboard.visible` and `TouchScreenKeyboard.area` should be used to determine if the keyboard is being shown (activated) and what portion of the screen is using.  
  
**Universal Windows Platform** : On Universal Windows Apps the touch screen keyboard is supported when physical keyboard is not connected.
### Static Properties
Property | Description  
---|---  
[area](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-area.html) | Indicates the portion of the screen that is currently covered by the on-screen keyboard.  
[hideInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-hideInput.html) | Will text input field above the keyboard be hidden when the keyboard is on screen?  
[inputFieldAppearance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-inputFieldAppearance.html) | Returns the current visibility status of the on-screen keyboard's input field. (Read Only)  
[isInPlaceEditingAllowed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-isInPlaceEditingAllowed.html) | Checks if the text within an input field can be selected and modified while TouchScreenKeyboard is open.  
[isSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-isSupported.html) | Checks if on-screen keyboards are supported.  
[visible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-visible.html) | Returns true whenever any keyboard is visible on the screen.  
### Properties
Property | Description  
---|---  
[active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-active.html) | Is the keyboard visible or sliding into the position on the screen?  
[canGetSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-canGetSelection.html) | Specifies whether the TouchScreenKeyboard supports the selection property. (Read Only)  
[canSetSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-canSetSelection.html) | Specifies whether the TouchScreenKeyboard supports the selection property. (Read Only)  
[characterLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-characterLimit.html) | How many characters the keyboard input field is limited to. 0 = infinite.  
[selection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-selection.html) | Gets or sets the character range of the selected text within the string currently being edited.  
[status](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-status.html) | Returns the status of the on-screen keyboard. (Read Only)  
[targetDisplay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-targetDisplay.html) | Specified on which display the on-screen keyboard will appear.  
[text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-text.html) | Returns the text displayed by the input field of the keyboard.  
[type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard-type.html) | Returns the TouchScreenKeyboardType of the keyboard.  
### Static Methods
Method | Description  
---|---  
[Open](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html) | Opens the native keyboard provided by OS on the screen.  
* * *
