* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LayerField.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).LayerField
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
public static int LayerField(int layer, params GUILayoutOption[] options); 
## Declaration
public static int LayerField(int layer, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static int LayerField(string label, int layer, params GUILayoutOption[] options); 
## Declaration
public static int LayerField(string label, int layer, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static int LayerField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, int layer, params GUILayoutOption[] options); 
## Declaration
public static int LayerField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, int layer, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Optional label in front of the field.  
layer | The layer shown in the field.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**int** The layer selected by the user. 
### Description
Make a layer selection field.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUILayoutLayerField.png)   
_Set the layer of the selected GameObjects._
```
// Simple editor script that lets you set the layer for the
// selected GameObjects.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class LayerFieldExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    static int selectedLayer = 0;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html) Field usage")]
    static void Init()
    {
        LayerFieldExample window = (LayerFieldExample)GetWindow(typeof(LayerFieldExample));
        window.Show();
    }  
  
    // Disable menu if we dont have at least 1 gameobject selected
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html) Field usage", true)]
    static bool ValidateSelection()
    {
        return Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html) != null;
    }  
  
    void OnGUI()
    {
        selectedLayer = EditorGUILayout.LayerField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LayerField.html)("Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html) for Objects:", selectedLayer);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Set Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html)!"))
            SetLayer();
    }  
  
    static void SetLayer()
    {
        foreach (var go in Selection.gameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-gameObjects.html))
            go.layer = selectedLayer;
    }
}

```

* * *
