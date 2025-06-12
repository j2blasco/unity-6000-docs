* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.OnPreviewGUI.html

#  [ObjectPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.html).OnPreviewGUI
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
r | Rectangle in which to draw the preview.  
background | Background image.  
### Description
Implement to create your own custom preview for the preview area of the inspector, primary editor headers and the object selector.
If you implement [OnInteractivePreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.OnInteractivePreviewGUI.html) then this will only be called for non-interactive custom previews. The overidden method should use the rectangle passed in and render a preview of the asset into it. The default implementation is a no-op.  
  
Additional resources: OnInteractivePreviewGUI.
* * *
