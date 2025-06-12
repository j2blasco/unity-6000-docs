* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginProperty.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).BeginProperty
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
public static [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) BeginProperty([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) totalPosition, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property); 
### Parameters
Parameter | Description  
---|---  
totalPosition | Rectangle on the screen to use for the control, including label if applicable.  
label | Optional label in front of the slider. Use null to use the name from the SerializedProperty. Use GUIContent.none to not display a label.  
property | The SerializedProperty to use for the control.  
### Returns
**GUIContent** The actual label to use for the control. 
### Description
Create a Property wrapper, useful for making regular GUI controls work with [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).
Most [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html) and [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html) GUI controls already have overloads that work with SerializedProperty. However, for GUI controls that don't handle SerializedProperty you can wrap them inside BeginProperty and EndProperty as shown in the example below. You can use this for your own custom GUI controls too.  
  
BeginProperty and EndProperty automatically handle default labels, bold font for Prefab overrides, revert to Prefab right click menu, and setting [showMixedValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI-showMixedValue.html) to true if the values of the property are different when multi-object editing.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  

class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // A slider function that takes a SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html)
    void Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html)(Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, float leftValue, float rightValue, GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label)
    {
        label = EditorGUI.BeginProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginProperty.html)(position, label, property);  
  
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        var newValue = EditorGUI.Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Slider.html)(position, label, property.floatValue, leftValue, rightValue);
        // Only assign the value back if it was actually changed by the user.
        // Otherwise a single value will be assigned to all objects when multi-object editing,
        // even when the user didn't touch the control.
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            property.floatValue = newValue;
        }
        EditorGUI.EndProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndProperty.html)();
    }
}

```

Additional resources: [EndProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndProperty.html).
* * *
