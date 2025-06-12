* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginFoldoutHeaderGroup.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).BeginFoldoutHeaderGroup
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
public static bool BeginFoldoutHeaderGroup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool foldout, string content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.foldoutHeader, Action<Rect> menuAction, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) menuIcon); 
## Declaration
public static bool BeginFoldoutHeaderGroup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool foldout, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.foldoutHeader, Action<Rect> menuAction, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) menuIcon); 
### Parameters
Parameter | Description  
---|---  
foldout | The shown foldout state.  
content | The label to show.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
menuAction | The action that happens when you click the icon.  
menuIcon | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) for icon.  
position | Rectangle on the screen to use for the control.  
### Returns
**bool** The foldout state selected by the user. If true, you should render sub-objects. 
### Description
Make a label with a foldout arrow to the left of it.
This is useful for folder-like structures, where child objects only appear if you've unfolded the parent folder. This control cannot be nested in another BeginFoldoutHeaderGroup. To use multiple of these foldouts, you must end each method with EndFoldoutHeaderGroup.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIFoldoutHeader.png)  
_Create a foldable header menu that hides or shows the selected Transform._
```
// Create a foldable header menu that hides or shows the selected Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) position.
// If you have not selected a Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html), the Foldout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Foldout.html) item stays folded until
// you select a Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class FoldoutHeaderUsage : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    bool showPosition = true;
    string status = "Select a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Foldout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Foldout.html) Header Usage")]
    static void CreateWindow()
    {
        GetWindow<FoldoutHeaderUsage>();
    }  
  
    public void OnGUI()
    {
        // An absolute-positioned example: We make foldout header group and put it in a small rect on the screen.
        showPosition = EditorGUI.BeginFoldoutHeaderGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginFoldoutHeaderGroup.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 200, 100), showPosition, status);  
  
        if (showPosition)
            if (Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html))
            {
                Selection.activeTransform.position =
                    EditorGUI.Vector3Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector3Field.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 30, 200, 100), "Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)", Selection.activeTransform.position);
                status = Selection.activeTransform.name;
            }  
  
        if (!Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html))
        {
            status = "Select a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)";
            showPosition = false;
        }
        // End the Foldout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Foldout.html) Header that we began above.
        EditorGUI.EndFoldoutHeaderGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndFoldoutHeaderGroup.html)();
    }
}

```

![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIFoldoutHeaderMenu.png)   
_Create a menu item action that moves the selected object to 0,0,0 when you click it._
```
// Create a foldable header menu that hides or shows the selected Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) position.
// If you have not selected a Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html), the Foldout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Foldout.html) item stays folded until
// you select a Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class FoldoutHeaderUsage : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    bool showPosition = true;
    string status = "Select a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Foldout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Foldout.html) Header Usage")]
    static void CreateWindow()
    {
        GetWindow<FoldoutHeaderUsage>();
    }  
  
    public void OnGUI()
    {
        // An absolute-positioned example: We make foldout header group and put it in a small rect on the screen.
        showPosition = EditorGUI.BeginFoldoutHeaderGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginFoldoutHeaderGroup.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 200, 100), showPosition, status, null, ShowHeaderContextMenu);  
  
        if (showPosition)
            if (Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html))
            {
                Selection.activeTransform.position =
                    EditorGUI.Vector3Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector3Field.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 30, 200, 100), "Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)", Selection.activeTransform.position);
                status = Selection.activeTransform.name;
            }  
  
        if (!Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html))
        {
            status = "Select a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)";
            showPosition = false;
        }
        // End the Foldout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Foldout.html) Header that we began above.
        EditorGUI.EndFoldoutHeaderGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndFoldoutHeaderGroup.html)();
    }  
  
    void ShowHeaderContextMenu(Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position)
    {
        var menu = new GenericMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html)();
        menu.AddItem(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Move to (0,0,0)"), false, OnItemClicked);
        menu.DropDown(position);
    }  
  
    void OnItemClicked()
    {
        Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html)(Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html), "Moving to center of world");
        Selection.activeTransform.position = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
    }
}

```

* * *
