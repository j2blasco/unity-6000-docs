* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.MaskContainer.html

#  [UsageHints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.html).MaskContainer
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
Optimizes rendering of a [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) that has multiple descendants with nested masks. 
This option reduces stencil state changes and capitalizes on consecutive mask push/pop operations for efficiency.  
  
Apply this option to a VisualElement with multiple nested masks among its descendants. For example, a child element has the `overflow: hidden;` style with rounded corners or SVG background.  
  
The following illustration shows the number of batches in a single-level masking, a nested masking, and a nested masking with MaskContainer. The yellow color indicates the masking elements. The orange color indicates the masking element with MaskContainer applied. The numbers indicate the number of batches.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/MaskContainer.png)  
A: Single-level masking (1 batch)  
B: Nested masking (5 batches)  
C: Nested masking with MaskContainer (2 batches)  
  
**Note** : Don't use GroupTransform in scenarios with many subtrees, where each subtree uses two or more levels of masking. This helps minimize consecutive push/push or pop/pop operations. 
* * *
