* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnPreviewGUI.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).OnPreviewGUI
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
public void OnPreviewGUI([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) r, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) background); 
### Parameters
Parameter | Description  
---|---  
r | The rectangle in which to draw the preview.  
background | Background image.  
### Description
Creates a custom preview for the preview area of the Inspector, the headers of the primary Editor, and the object selector.  
  
You must implement [Editor.HasPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.HasPreviewGUI.html) for this method to be called.
If you implement [OnInteractivePreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInteractivePreviewGUI.html), then this method is only called for non-interactive custom previews. The overidden method should render a preview of the asset in the specified rectangle (r). The default implementation is a no-op.  
  
**Note:** Inspector previews are limited to the primary Editor of persistent objects, such as GameObjectInspector, MaterialEditor, and TextureInspector. A component cannot have its own Inspector preview.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[CreateAssetMenu]
class MyObject : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public string text;
}  
  
// Show a preview of the text saved in MyObject.
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(MyObject))]
public class MyObjectEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    public override bool HasPreviewGUI() => true;  
  
    public override void OnPreviewGUI(Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) r, GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) background)
    {
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(r, (target as MyObject).text);
    }
}

```

Additional resources: [OnInteractivePreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInteractivePreviewGUI.html).
* * *
