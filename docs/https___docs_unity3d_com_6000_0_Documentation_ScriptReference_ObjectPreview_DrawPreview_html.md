* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.DrawPreview.html

#  [ObjectPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.html).DrawPreview
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
public void DrawPreview([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) previewArea); 
### Parameters
Parameter | Description  
---|---  
previewArea | The available area to draw the preview.  
### Description
This is the first entry point for Preview Drawing.
The default implementation will draw a grid of previews if there are multiple targets available. Override this method if you want to change this behaviour.
* * *
