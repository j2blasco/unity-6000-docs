* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-isExpanded.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).isExpanded
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
isExpanded; 
### Description
Is this property expanded in the inspector?
Serialized properties with child properties (e.g., arrays, custom serializable structs, or custom serializable classes) may be either expanded or folded up in the inspector to reveal or hide their children. The following example displays a note in the inspector when users expand a [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) property.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[CustomPropertyDrawer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomPropertyDrawer.html)(typeof(Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)))]
public class QuaternionDrawer : PropertyDrawer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html)
{
    public override float GetPropertyHeight(SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label)
    {
        // use the default property height, which takes into account the expanded state
        return EditorGUI.GetPropertyHeight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.GetPropertyHeight.html)(property);
    }  
  
    public override void OnGUI(Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label)
    {
        // draw the default property editor
        EditorGUI.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PropertyField.html)(position, property, label, true);  
  
        // display a warning to discourage users from manually editing child properties on a quaternion
        if (property.isExpanded)
        {
            position.height = EditorGUIUtility.singleLineHeight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-singleLineHeight.html);
            position.xMin += EditorGUIUtility.labelWidth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-labelWidth.html);
            EditorGUI.HelpBox[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.HelpBox.html)(position, "Editing quaternions manually is inadvisable.", MessageType.Warning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MessageType.Warning.html));
        }
    }
}

```

![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/SerializedPropertyIsExpanded.png)   
_Displaying a message when a Quaternion property is expanded._  
  
Note that the value of this flag is shared across all instances of the serialized property in question that have the same property path and target type. For example, folding up a particular property in the inspector for a component will make the same property folded up in the inspector for all other instances of the same component type.
* * *
