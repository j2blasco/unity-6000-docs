* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Foldout.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).Foldout
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
public static bool Foldout(bool foldout, string content, bool toggleOnLabelClick, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.foldout); 
## Declaration
public static bool Foldout(bool foldout, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, bool toggleOnLabelClick, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.foldout); 
## Declaration
public static bool Foldout(bool foldout, string content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.foldout); 
## Declaration
public static bool Foldout(bool foldout, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.foldout); 
### Parameters
Parameter | Description  
---|---  
foldout | The shown foldout state.  
content | The label to show.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
toggleOnLabelClick | Specifies whether clicking the label toggles the foldout state. The default value is false. Set to true to include the label in the clickable area.  
### Returns
**bool** The foldout state selected by the user. If true, you should render sub-objects. 
### Description
Make a label with a foldout arrow to the left of it.
This is useful for creating tree or folder like structures where child objects are only shown if the parent is folded out.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/FoldoutUsageScreenshot.png)  
_Foldout in an Editor Window._
```
// Create a foldable menu that hides/shows the selected transform position.
// If no Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) is selected, the Foldout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Foldout.html) item will be folded until
// a transform is selected.  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class FoldoutUsage : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    bool showPosition = true;
    string status = "Select a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Foldout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Foldout.html) Usage")]
    static void Init()
    {
        FoldoutUsage window = (FoldoutUsage)GetWindow(typeof(FoldoutUsage));
        window.Show();
    }  
  
    public void OnGUI()
    {
        showPosition = EditorGUILayout.Foldout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Foldout.html)(showPosition, status);
        if (showPosition)
            if (Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html))
            {
                Selection.activeTransform.position =
                    EditorGUILayout.Vector3Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Vector3Field.html)("Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)", Selection.activeTransform.position);
                status = Selection.activeTransform.name;
            }  
  
        if (!Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html))
        {
            status = "Select a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)";
            showPosition = false;
        }
    }  
  
    public void OnInspectorUpdate()
    {
        this.Repaint();
    }
}

```

* * *
