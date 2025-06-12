* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Foldout.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).Foldout
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
public static bool Foldout([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool foldout, string content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.foldout); 
## Declaration
public static bool Foldout([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool foldout, string content, bool toggleOnLabelClick, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.foldout); 
## Declaration
public static bool Foldout([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool foldout, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.foldout); 
## Declaration
public static bool Foldout([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool foldout, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, bool toggleOnLabelClick, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.foldout); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the arrow and label.  
foldout | The shown foldout state.  
content | The label to show.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
toggleOnLabelClick | Should the label be a clickable part of the control?  
### Returns
**bool** The foldout state selected by the user. If true, you should render sub-objects. 
### Description
Makes a label with a foldout arrow to the left of it.
This is useful for creating tree or folder like structures where child objects are only shown if the parent is folded out.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/FoldoutUsageScreenshot.png)  
_Foldout in an Editor Window._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;  
  
// Create a foldable menu that hides/shows the selected transform position.
// if no Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) is selected, the Foldout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Foldout.html) item will be folded until a transform is selected.
public class EditorGUIFoldout : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    public bool showPosition = true;
    public string status = "Select a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)";
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Foldout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Foldout.html) Usage")]
    static void Init()
    {
        UnityEditor.EditorWindow window = GetWindow(typeof(EditorGUIFoldout));
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 150, 60);
        window.Show();
    }  
  
    void OnGUI()
    {
        showPosition = EditorGUI.Foldout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Foldout.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, position.width - 6, 15), showPosition, status);
        if (showPosition)
            if (Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html))
            {
                Selection.activeTransform.position = EditorGUI.Vector3Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector3Field.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 25, position.width - 6, 40), "Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)", Selection.activeTransform.position);
                status = Selection.activeTransform.name;
            }  
  
        if (!Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html))
        {
            status = "Select a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)";
            showPosition = false;
        }
    }  
  
    void OnInspectorUpdate()
    {
        Repaint();
    }
}

```

* * *
