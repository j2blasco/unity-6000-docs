* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.GetInheritedAlpha.html

#  [CanvasRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.html).GetInheritedAlpha
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
public float GetInheritedAlpha(); 
### Returns
**float** The calculated inherited alpha. 
### Description
Get the final inherited alpha calculated by including all the parent alphas from included parent CanvasGroups.
Alpha is calculated by getting the alpha from all parent CanvasGroups (if GetIgnoreParentGroups is false) and multiplying the original alpha.
* * *
