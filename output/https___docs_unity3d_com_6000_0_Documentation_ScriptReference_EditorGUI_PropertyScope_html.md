* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PropertyScope.html

# PropertyScope
class in UnityEditor
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
Create a Property wrapper, useful for making regular GUI controls work with [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).
Most [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html) and [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html) GUI controls already have overloads that work with SerializedProperty. However, for GUI controls that don't handle SerializedProperty you can wrap them inside BeginProperty and EndProperty as shown in the example below. You can use this for your own custom GUI controls too.  
  
BeginProperty and EndProperty automatically handle default labels, bold font for Prefab overrides, revert to Prefab right click menu, and setting [showMixedValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI-showMixedValue.html) to true if the values of the property are different when multi-object editing.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // A slider function that takes a SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html)
    void Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html)(Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) prop, float leftValue, float rightValue, GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label)
    {
        using (var scope = new EditorGUI.PropertyScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PropertyScope.html)(position, label, prop))
        {
            label = scope.content;
            EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
            var newValue = EditorGUI.Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Slider.html)(position, label, prop.floatValue, leftValue, rightValue);
            // Only assign the value back if it was actually changed by the user.
            // Otherwise a single value will be assigned to all objects when multi-object editing,
            // even when the user didn't touch the control.
            if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
                prop.floatValue = newValue;
        }
    }
}

```

Additional resources: [BeginProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginProperty.html).
### Properties
Property | Description  
---|---  
[content](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PropertyScope-content.html) | The actual label to use for the control.  
### Constructors
Constructor | Description  
---|---  
[EditorGUI.PropertyScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PropertyScope-ctor.html) | Create a new PropertyScope and begin the corresponding property.  
* * *
