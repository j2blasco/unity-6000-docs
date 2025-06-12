* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.HasPreviewGUI.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).HasPreviewGUI
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
public bool HasPreviewGUI(); 
### Returns
**bool** True if this component can be Previewed in its current state. 
### Description
Override this method in subclasses if you implement [OnPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnPreviewGUI.html).
You can also use it to disable or enable preview depending on the target asset. The default implementation simply returns false, so if you override [OnPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnPreviewGUI.html) you have to override this method as well.  
  
**Note:** Inspector previews are limited to the primary editor of persistent objects (assets), e.g., GameObjectInspector, MaterialEditor, TextureInspector. This means that it is currently not possible for a component to have its own inspector preview.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class GameObjectEditorWindow: EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject;
    Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) gameObjectEditor;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)")]
    static void ShowWindow()
    {
        GetWindow<GameObjectEditorWindow>("GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)");
    }  
  
    void OnGUI()
    {
        gameObject = (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)) EditorGUILayout.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ObjectField.html)(gameObject, typeof(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)), true);  
  
        if (gameObject != null)
        {
            if (gameObjectEditor == null)
                gameObjectEditor = Editor.CreateEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateEditor.html)(gameObject);  
  
            gameObjectEditor.OnPreviewGUI(GUILayoutUtility.GetRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutUtility.GetRect.html)(500, 500), EditorStyles.whiteLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-whiteLabel.html));
        }
    }
}

```

* * *
