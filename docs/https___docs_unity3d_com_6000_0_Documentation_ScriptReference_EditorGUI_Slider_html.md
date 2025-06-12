* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Slider.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).Slider
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
public static float Slider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, float value, float leftValue, float rightValue); 
## Declaration
public static float Slider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, float value, float leftValue, float rightValue); 
## Declaration
public static float Slider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, float value, float leftValue, float rightValue); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the slider.  
label | Optional label in front of the slider.  
value | The value the slider shows. This determines the position of the draggable thumb.  
leftValue | The value at the left end of the slider.  
rightValue | The value at the right end of the slider.  
### Returns
**float** The value that has been set by the user. 
### Description
Makes a slider the user can drag to change a value between a min and a max.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUISlider.png)   
_Slider in an Editor Window._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) script that lets you scale the selected GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) between 1 and 100  
  
class EditorGUISlider : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    float scale = 1.0f;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/EditorGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html) Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) usage")]
    static void Init()
    {
        var window = GetWindow<EditorGUISlider>();
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 150, 30);
        window.Show();
    }  
  
    void OnGUI()
    {
        scale = EditorGUI.Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Slider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(5, 5, 150, 20), scale, 1, 100);
    }  
  
    void OnInspectorUpdate()
    {
        if (Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html))
        {
            Selection.activeTransform.localScale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(scale, scale, scale);
        }
    }
}

```

* * *
## Declaration
public static void Slider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, float leftValue, float rightValue); 
## Declaration
public static void Slider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, float leftValue, float rightValue, string label); 
## Declaration
public static void Slider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, float leftValue, float rightValue, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the slider.  
label | Optional label in front of the slider.  
property | The value the slider shows. This determines the position of the draggable thumb.  
leftValue | The value at the left end of the slider.  
rightValue | The value at the right end of the slider.  
### Description
Makes a slider the user can drag to change a value between a min and a max.
* * *
