* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.FloatField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).FloatField
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
public static float FloatField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, float value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
## Declaration
public static float FloatField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, float value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
## Declaration
public static float FloatField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, float value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the float field.  
label | Optional label to display in front of the float field.  
value | The value to edit.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
### Returns
**float** The value entered by the user. 
### Description
Makes a text field for entering floats.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIFloatField.png)   
_Float Field in an Editor Window._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class EditorGUIFloatField : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    float sizeMultiplier = 1;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html) selected Object")]
    static void Init()
    {
        var window = GetWindow<EditorGUIFloatField>();
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 210, 30);
        window.Show();
    }  
  
    void OnGUI()
    {
        sizeMultiplier = EditorGUI.FloatField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.FloatField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, 150, 20),
            "Increase scale by:",
            sizeMultiplier);  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(160, 3, 45, 20), "Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html)!"))
        {
            Selection.activeTransform.localScale = Selection.activeTransform.localScale * sizeMultiplier;
        }
    }
}

```

* * *
