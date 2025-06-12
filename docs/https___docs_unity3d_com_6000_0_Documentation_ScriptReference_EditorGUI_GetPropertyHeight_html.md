* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.GetPropertyHeight.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).GetPropertyHeight
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
public static float GetPropertyHeight([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, bool includeChildren); 
## Declaration
public static float GetPropertyHeight([SerializedPropertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.html) type, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label); 
## Declaration
public static float GetPropertyHeight([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label = null, bool includeChildren = true); 
### Parameters
Parameter | Description  
---|---  
property | Height of the property area.  
label | Descriptive text or image.  
includeChildren | Should the returned height include the height of child properties?  
### Description
Get the height needed for a [PropertyField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PropertyField.html) control.
The height is based on the type of the SerializedProperty, and inclues the height of all expanded children if the includeChildren parameter is set to true, which is the default. If the property has a custom PropertyDrawer, the function will return the height returned by that drawer. The includeChildren parameter is ignored in that case, as PropertyDrawers always include children.
* * *
