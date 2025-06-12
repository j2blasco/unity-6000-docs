* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.SetInsetAndSizeFromParentEdge.html

#  [RectTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html).SetInsetAndSizeFromParentEdge
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
public void SetInsetAndSizeFromParentEdge([RectTransform.Edge](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.Edge.html) edge, float inset, float size); 
### Parameters
Parameter | Description  
---|---  
edge | The edge of the parent rectangle to inset from.  
inset | The inset distance.  
size | The size of the rectangle along the same direction of the inset.  
### Description
Set the distance of this rectangle relative to a specified edge of the parent rectangle, while also setting its size.
Calling this method sets both the anchors, anchoredPosition, and sizeDelta, though only either the horizontal or vertical components, depending on which edge is specified for the inset.  
  
The method can particularly be useful when scripting layout behaviours, since it makes it simple to specify positions relative to the parent edges without needing to be concerned with anchoring functionality.
* * *
