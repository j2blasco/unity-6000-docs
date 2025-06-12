* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.GroupTransform.html

#  [UsageHints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.html).GroupTransform
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
Optimizes rendering of a [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) that changes its transformation and position frequently, and has many descendants that have their hints set to DynamicTransform. 
This option is similar to DynamicTransform in that it allows GPU transformation of the vertices of the descendants. However it breaks the batch, and adds an extra draw call. The purpose of this hint is to avoid having to update the stored matrix of many elements that have DynamicTransform set when a common ancestor changes its transformation or position. In other words, this is an optimisation for DynamicTransform.  
  
An example use case is that in Shader Graph, you can set individual nodes with DynamicTransform, and set the ancestor panner/zoomer with `GroupTransform`, so that when you pan/zoom, you avoid the need to update hundreds of dynamic transforms.  
  
**Note** : Don't use both DynamicTransform and GroupTransform at the same time on a single VisualElement. 
* * *
