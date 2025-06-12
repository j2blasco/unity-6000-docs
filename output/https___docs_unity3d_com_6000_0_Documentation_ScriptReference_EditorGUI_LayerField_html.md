* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LayerField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).LayerField
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
public static int LayerField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, int layer, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
## Declaration
public static int LayerField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, int layer, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
## Declaration
public static int LayerField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, int layer, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the field.  
label | Optional label in front of the field.  
layer | The layer shown in the field.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
### Returns
**int** The layer selected by the user. 
### Description
Makes a layer selection field.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUILayerField.png)   
_Layer field in an Editor Window._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  

// Change the Tag and/or the layer of the selected GameObjects.  
  
class EditorGUITagLayerField : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    string selectedTag = "";
    int selectedLayer = 0;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Tag - Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html) for Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html)")]
    static void Init()
    {
        var window = GetWindow<EditorGUITagLayerField>();
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 350, 70);
        window.Show();
    }  
  
    void OnGUI()
    {
        selectedTag = EditorGUI.TagField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.TagField.html)(
            new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, position.width / 2 - 6, 20),
            "New Tag:",
            selectedTag);  
  
        selectedLayer = EditorGUI.LayerField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LayerField.html)(
            new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(position.width / 2 + 3, 3, position.width / 2 - 6, 20),
            "New Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html):",
            selectedLayer);  
  
        if (Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html))
        {
            if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 25, 90, 17), "Change Tags"))
            {
                foreach (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go in Selection.gameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-gameObjects.html))
                {
                    go.tag = selectedTag;
                }
            }  
  
            if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(position.width - 96, 25, 90, 17), "Change Layers"))
            {
                foreach (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go in Selection.gameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-gameObjects.html))
                {
                    go.layer = selectedLayer;
                }
            }
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
