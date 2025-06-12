* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntSlider.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).IntSlider
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
public static int IntSlider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, int value, int leftValue, int rightValue); 
## Declaration
public static int IntSlider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, int value, int leftValue, int rightValue); 
## Declaration
public static int IntSlider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, int value, int leftValue, int rightValue); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the slider.  
label | Optional label in front of the slider.  
value | The value the slider shows. This determines the position of the draggable thumb.  
leftValue | The value at the left end of the slider.  
rightValue | The value at the right end of the slider.  
### Returns
**int** The value that has been set by the user. 
### Description
Makes a slider the user can drag to change an integer value between a min and a max.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIIntSlider.png)   
_Int Slider in an Editor Window._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;  
  
// Simple editor script that lets you clone your object in a grid  
  
public class EditorGUIIntSlider : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    int cloneTimesX = 1;
    int cloneTimesY = 1;
    int cloneTimesZ = 1;
    int spacing = 2;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) int slider usage")]
    static void Init()
    {
        UnityEditor.EditorWindow window = GetWindow(typeof(EditorGUIIntSlider));
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 100, 250, 100);
        window.Show();
    }  
  
    void OnGUI()
    {
        cloneTimesX = EditorGUI.IntSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, position.width, 20), cloneTimesX.ToString(), cloneTimesX, 1, 10);
        cloneTimesY = EditorGUI.IntSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 25, position.width, 20), cloneTimesY.ToString(), cloneTimesY, 1, 10);
        cloneTimesZ = EditorGUI.IntSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 50, position.width, 20), cloneTimesZ.ToString(), cloneTimesZ, 1, 10);  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 75, position.width, 15), "Make Grid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Grid.html)!"))
        {
            CloneSelected();
        }
    }  
  
    void CloneSelected()
    {
        if (!Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Select a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) first");
            return;
        }  
  
        for (int i = 0; i < cloneTimesX; i++)
        {
            for (int j = 0; j < cloneTimesY; j++)
            {
                for (int k = 0; k < cloneTimesZ; k++)
                {
                    Instantiate(Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html),
                        new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(i, j, k) * spacing,
                        Selection.activeGameObject.transform.rotation);
                }
            }
        }
    }
}

```

* * *
## Declaration
public static void IntSlider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, int leftValue, int rightValue); 
## Declaration
public static void IntSlider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, int leftValue, int rightValue, string label); 
## Declaration
public static void IntSlider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, int leftValue, int rightValue, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label); 
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
