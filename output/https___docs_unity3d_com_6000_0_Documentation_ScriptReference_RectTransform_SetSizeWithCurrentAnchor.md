* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.SetSizeWithCurrentAnchors.html

#  [RectTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html).SetSizeWithCurrentAnchors
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
public void SetSizeWithCurrentAnchors([RectTransform.Axis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.Axis.html) axis, float size); 
### Parameters
Parameter | Description  
---|---  
axis | The axis to specify the size along.  
size | The desired size along the specified axis.  
### Description
Makes the RectTransform calculated rect be a given size on the specified axis.
This method produces the given size with the current anchoring. If the parent RectTransform changes size, the size of the rect may change. If the size is meant to stay, either the RectTransform anchors should be set not to stretch, or this method should be invoked again whenever the parent size changes.
* * *
