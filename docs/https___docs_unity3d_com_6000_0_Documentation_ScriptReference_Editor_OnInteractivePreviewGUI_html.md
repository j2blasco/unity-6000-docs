* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInteractivePreviewGUI.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).OnInteractivePreviewGUI
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
public void OnInteractivePreviewGUI([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) r, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) background); 
### Parameters
Parameter | Description  
---|---  
r | Rectangle in which to draw the preview.  
background | Background image.  
### Description
Implement to create your own interactive custom preview. Interactive custom previews are used in the preview area of the inspector and the object selector.
Implement this method, instead of [OnPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnPreviewGUI.html), to display interactive custom previews. You can implement both methods when some previews are interactive and others are not. The overidden method should use the rectangle passed in and render a preview of the asset. The default implementation is a no-op.  
  
**Note:** Inspector previews are limited to the primary editor of persistent objects (assets). For example, GameObjectInspector, MaterialEditor, TextureInspector, and so on. This means that it is currently not possible for a component to have its own inspector preview.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Create an editor window which can display a chosen GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
// Use OnInteractivePreviewGUI to display the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and
// allow it to be interactive.  
  
public class ExampleClass: EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject;
    Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) gameObjectEditor;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)")]
    static void ShowWindow()
    {
        GetWindowWithRect<ExampleClass>(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 256, 256));
    }  
  
    void OnGUI()
    {
        gameObject = (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)) EditorGUILayout.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ObjectField.html)(gameObject, typeof(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)), true);  
  
        GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) bgColor = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)();
        bgColor.normal.background = EditorGUIUtility.whiteTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-whiteTexture.html);  
  
        if (gameObject != null)
        {
            if (gameObjectEditor == null)
                gameObjectEditor = Editor.CreateEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateEditor.html)(gameObject);  
  
            gameObjectEditor.OnInteractivePreviewGUI(GUILayoutUtility.GetRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutUtility.GetRect.html)(256, 256), bgColor);
        }
    }
}
```

* * *
