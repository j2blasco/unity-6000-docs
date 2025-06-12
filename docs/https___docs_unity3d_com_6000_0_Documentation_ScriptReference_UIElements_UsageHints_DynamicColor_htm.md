* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.DynamicColor.html

#  [UsageHints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.html).DynamicColor
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
Optimizes rendering of a [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) for frequent color changes, such as a built-in style color being animated. 
This option fetches color from a GPU buffer to prevent re-tessellating geometry or CPU updates when colors change.  
  
Apply this option on a VisualElement that changes any of the following style properties: 
  * `background-color`
  * `border-color`
  * `color`
  * `border-bottom-color`
  * `border-left-color`
  * `border-right-color`
  * `border-top-color`
  * `text-color`
  * `unity-background-image-tint-color`


* * *
