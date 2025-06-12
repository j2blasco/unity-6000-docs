* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.RectField.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).RectField
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
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) RectField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) value, params GUILayoutOption[] options); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) RectField(string label, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) value, params GUILayoutOption[] options); 
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) RectField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) value, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Label to display above the field.  
value | The value to edit.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**Rect** The value entered by the user. 
### Description
Make an X, Y, W & H field for entering a [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html).
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/MoveResizeSelectedWindow2.png)  
_Capture the RectField sizes._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class RectFieldExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    static Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) pos;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/RectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RectField.html) Example")]
    static void rectFieldExample()
    {
        RectFieldExample window =
            EditorWindow.GetWindowWithRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindowWithRect.html)<RectFieldExample>(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 250, 100));
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUILayout.BeginVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginVertical.html)();
        pos =  EditorGUILayout.RectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.RectField.html)("Internal input:", pos);  
  
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();
        GUILayout.FlexibleSpace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.FlexibleSpace.html)();
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("x: " + (pos.x).ToString());
        GUILayout.FlexibleSpace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.FlexibleSpace.html)();
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("y: " + (pos.y).ToString());
        GUILayout.FlexibleSpace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.FlexibleSpace.html)();
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("w: " + (pos.width).ToString());
        GUILayout.FlexibleSpace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.FlexibleSpace.html)();
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("h: " + (pos.height).ToString());
        GUILayout.FlexibleSpace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.FlexibleSpace.html)();
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();
        EditorGUILayout.EndVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndVertical.html)();  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Close"))
        {
            this.Close();
        }
    }
}

```

* * *
