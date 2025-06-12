* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.GetInfoString.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).GetInfoString
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
public string GetInfoString(); 
### Description
Implement this method to show asset information on top of the asset preview.
You will also have to implement [HasPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.HasPreviewGUI.html) and [OnPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnPreviewGUI.html) in addition to this method. The default implementation just returns an empty string, which disables the feature.  
  
**Note:** Inspector previews are limited to the primary editor of persistent objects (assets). For example, GameObjectInspector, MaterialEditor, TextureInspector, and so on. This means that it is currently not possible for a component to have its own inspector preview.
* * *
