* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.GetPreviewTitle.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).GetPreviewTitle
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
public [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) GetPreviewTitle(); 
### Description
Override this method if you want to change the label of the Preview area.
If null is returned the default text "Preview" will be used.  
  
**Note:** Inspector previews are limited to the primary editor of persistent objects (assets), e.g., GameObjectInspector, MaterialEditor, TextureInspector. This means that it is currently not possible for a component to have its own inspector preview.
* * *
