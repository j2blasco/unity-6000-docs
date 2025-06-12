* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DropdownButton.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).DropdownButton
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
public static bool DropdownButton([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [FocusType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FocusType.html) focusType); 
## Declaration
public static bool DropdownButton([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [FocusType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FocusType.html) focusType, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the button.  
content | Text, image and tooltip for this button.  
focusType | Whether the button should be selectable by keyboard or not.  
style | Optional style to use.  
### Returns
**bool** `true` when the user clicks the button. 
### Description
Makes a button that reacts to mouse down, for displaying your own dropdown content.
This control does not do anything but returns true on mouse down when clicked, as opposed to regular buttons that return true on mouse up.  
  
This can be used for buttons that should open a [GenericMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html) or your own custom [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) in dropdown form.  
  
When used with a GenericMenu, use GenericMenu.Dropdown and pass the same rect to the method as was used for the button position.  
  
When used with a custom EditorWindow, use EditorWindow.ShowAsDropdown and pass the same rect to the method as was used for the button position.
* * *
