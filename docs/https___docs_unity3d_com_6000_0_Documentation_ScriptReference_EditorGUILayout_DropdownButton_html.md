* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.DropdownButton.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).DropdownButton
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
public static bool DropdownButton([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [FocusType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FocusType.html) focusType, params GUILayoutOption[] options); 
## Declaration
public static bool DropdownButton([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [FocusType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FocusType.html) focusType, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
content | Text, image and tooltip for this button.  
focusType | Whether the button should be selectable by keyboard or not.  
style | Optional style to use.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**bool** `true` when the user clicks the button. 
### Description
Make a button that reacts to mouse down, for displaying your own dropdown content.
This control does not do anything but returns true on mouse down when clicked, as opposed to regular buttons that return true on mouse up.  
  
This can be used for buttons that should open a [GenericMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html) or your own custom [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) in dropdown form.  
  
When used with a GenericMenu, use GenericMenu.Dropdown and pass the same rect to the method as was used for the button, which you can obtain using [GUILayoutUtility.GetLastRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutUtility.GetLastRect.html). Note that this will only return a valid rect when [EditorGUILayout.DropdownButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.DropdownButton.html) returns false. This happens because the last layout event is not used when the click goes through to open a menu.  
  
When used with a custom EditorWindow, use EditorWindow.ShowAsDropdown and pass the same rect to the method as was used for the button, which you can obtain using [GUILayoutUtility.GetLastRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutUtility.GetLastRect.html).
* * *
