* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.html

# ObjectPreview
class in UnityEditor
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
### Description
Base Class to derive from when creating Custom Previews.
You specify which type is the preview for by using the CustomPreview attribute derived from [ObjectPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.html). Below you can see an small example that will display the name of the object being inspected. The preview window will appear at the bottom of the Inspector window.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[CustomPreview(typeof(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)))]
public class MyPreview : ObjectPreview[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.html)
{
    public override bool HasPreviewGUI()
    {
        return true;
    }  
  
    public override void OnPreviewGUI(Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) r, GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) background)
    {
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(r, target.name + " is being previewed");
    }
}

```

### Properties
Property | Description  
---|---  
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview-target.html) | The object currently being previewed.  
### Public Methods
Method | Description  
---|---  
[Cleanup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.Cleanup.html) | Use this function to release resources allocated by the ObjectPreview implementation.  
[CreatePreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.CreatePreview.html) | See Editor.CreatePreview.  
[DrawPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.DrawPreview.html) | This is the first entry point for Preview Drawing.  
[GetInfoString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.GetInfoString.html) | Implement this method to show object information on top of the object preview.  
[GetPreviewTitle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.GetPreviewTitle.html) | Override this method if you want to change the label of the Preview area.  
[HasPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.HasPreviewGUI.html) | Can this component be Previewed in its current state?  
[Initialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.Initialize.html) | Called when the Preview gets created with the objects being previewed.  
[MoveNextTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.MoveNextTarget.html) | Called to iterate through the targets, this will be used when previewing more than one target.  
[OnInteractivePreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.OnInteractivePreviewGUI.html) | Implement to create your own interactive custom preview. Interactive custom previews are used in the preview area of the inspector and the object selector.  
[OnPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.OnPreviewGUI.html) | Implement to create your own custom preview for the preview area of the inspector, primary editor headers and the object selector.  
[OnPreviewSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.OnPreviewSettings.html) | Override this method if you want to show custom controls in the preview header.  
[ResetTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.ResetTarget.html) | Called to Reset the target before iterating through them.  
* * *
