* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ImmediateModeElement.ImmediateRepaint.html

#  [ImmediateModeElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ImmediateModeElement.html).ImmediateRepaint
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
protected void ImmediateRepaint(); 
### Description
Invoked during the repaint phase. 
Here it is safe to use any rendering calls using the immediate Graphics api, eg: Graphics.DrawTexture(contentRect, image); Graphics.DrawMesh, etc The current transform matrix is set up so (0,0) correspond to the top-left corner of the element. For IMGUI usage, please use the [IMGUIContainer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMGUIContainer.html) element. 
* * *
