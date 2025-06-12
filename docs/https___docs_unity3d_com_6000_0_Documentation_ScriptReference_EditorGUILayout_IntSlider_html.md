* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntSlider.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).IntSlider
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
public static int IntSlider(int value, int leftValue, int rightValue, params GUILayoutOption[] options); 
## Declaration
public static int IntSlider(string label, int value, int leftValue, int rightValue, params GUILayoutOption[] options); 
## Declaration
public static int IntSlider([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, int value, int leftValue, int rightValue, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Optional label in front of the slider.  
value | The value the slider shows. This determines the position of the draggable thumb.  
leftValue | The value at the left end of the slider.  
rightValue | The value at the right end of the slider.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**int** The value that has been set by the user. 
### Description
Make a slider the user can drag to change an integer value between a min and a max.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUILayoutIntSlider.png)   
_Create a grid of cloned Objects._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
// Simple editor script that lets you clone your object in a grid  
  
public class IntSliderExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    int cloneTimesX  = 1;
    int cloneTimesY  = 1;
    int cloneTimesZ  = 1;
    int spacing   = 2;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) GUILayout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html) IntSlider usage")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow(typeof(IntSliderExample));
        window.Show();
    }  
  
    void OnGUI()
    {
        cloneTimesX = EditorGUILayout.IntSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntSlider.html)(cloneTimesX, 1, 10);
        cloneTimesY = EditorGUILayout.IntSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntSlider.html)(cloneTimesY, 1, 10);
        cloneTimesZ = EditorGUILayout.IntSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntSlider.html)(cloneTimesZ, 1, 10);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Duplicate object"))
            CloneSelected();
    }  
  
    void CloneSelected()
    {
        if (!Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html))
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Select a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) first");
            return;
        }  
  
        for (int i = 0; i < cloneTimesX; i++)
            for (int j = 0; j < cloneTimesY; j++)
                for (int k = 0; k < cloneTimesZ; k++)
                    Instantiate(Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(i, j, k) * spacing, Selection.activeGameObject.transform.rotation);
    }
}

```

* * *
## Declaration
public static void IntSlider([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, int leftValue, int rightValue, params GUILayoutOption[] options); 
## Declaration
public static void IntSlider([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, int leftValue, int rightValue, string label, params GUILayoutOption[] options); 
## Declaration
public static void IntSlider([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, int leftValue, int rightValue, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Optional label in front of the slider.  
property | The value the slider shows. This determines the position of the draggable thumb.  
leftValue | The value at the left end of the slider.  
rightValue | The value at the right end of the slider.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Description
Make a slider the user can drag to change an integer value between a min and a max.
* * *
