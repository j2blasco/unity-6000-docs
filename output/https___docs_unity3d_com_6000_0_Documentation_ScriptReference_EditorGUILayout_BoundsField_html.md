* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BoundsField.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).BoundsField
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
public static [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) BoundsField([Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) value, params GUILayoutOption[] options); 
## Declaration
public static [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) BoundsField(string label, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) value, params GUILayoutOption[] options); 
## Declaration
public static [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) BoundsField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) value, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Label to display above the field.  
value | The value to edit.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**Bounds** The value entered by the user. 
### Description
Make Center & Extents field for entering a [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html).
* * *
