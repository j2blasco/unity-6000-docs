* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-pixelPerfect.html

#  [Canvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html).pixelPerfect
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
pixelPerfect; 
### Description
Forces pixel alignment for elements in the canvas. It only applies when [Canvas.renderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-renderMode.html) is set to Screen Space.
Enabling pixelPerfect can make elements appear sharper and prevent blurriness. However, if many elements are scaled or rotated, or use subtle animated position or scaling, it may be advantageous to disable pixelPerfect, since the movement will be smoother without.
* * *
