* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.DynamicTransform.html

#  [UsageHints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.html).DynamicTransform
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
Optimizes rendering of a [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) for frequent position and transformation changes. 
This option uses the GPU instead of CPU to perform the VisualElement's vertex transformation.  
  
Use this option on a VisualElement that changes any of the following style properties: 
  * `left`
  * `top`
  * `right`
  * `bottom`
  * `position`
  * `transform-origin`
  * `rotate`
  * `scale`
  * `translate`


* * *
