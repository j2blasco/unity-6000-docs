* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-activeEditorGameViewTarget.html

#  [Display](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html).activeEditorGameViewTarget
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
activeEditorGameViewTarget; 
### Description
Get the Editors active GameView display target.
Returns the last selected GameView's display target.  
  
At runtime will return -1 as there is no GameView. To get the display index at runtime you can use Display.RelativeMouseAt and look at the z value.
* * *
