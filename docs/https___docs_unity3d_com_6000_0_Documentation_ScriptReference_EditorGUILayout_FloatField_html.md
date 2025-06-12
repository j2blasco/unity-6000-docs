* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.FloatField.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).FloatField
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
public static float FloatField(float value, params GUILayoutOption[] options); 
## Declaration
public static float FloatField(float value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static float FloatField(string label, float value, params GUILayoutOption[] options); 
## Declaration
public static float FloatField(string label, float value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static float FloatField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, float value, params GUILayoutOption[] options); 
## Declaration
public static float FloatField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, float value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Optional label to display in front of the float field.  
value | The value to edit.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**float** The value entered by the user. 
### Description
Make a text field for entering float values.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUILayoutFloatField.png)   
_Multiply the scale of the selected GameObject._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Script that multiplies the scale of the current selected GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)  
  
public class FloatFieldExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    float sizeMultiplier = 1.0f;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html) selected Object")]
    static void Init()
    {
        var window = (FloatFieldExample)GetWindow(typeof(FloatFieldExample));
        window.Show();
    }  
  
    void OnGUI()
    {
        sizeMultiplier = EditorGUILayout.FloatField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.FloatField.html)("Increase scale by:", sizeMultiplier);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html)"))
        {
            if (!Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html))
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Select a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) first");
                return;
            }  
  
            Selection.activeTransform.localScale =
                Selection.activeTransform.localScale * sizeMultiplier;
        }
    }
}

```

* * *
