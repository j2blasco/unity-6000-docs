* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Group.AcceptsElement.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [Group](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Group.html).AcceptsElement
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
public bool AcceptsElement([Experimental.GraphView.GraphElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphElement.html) element, ref string reasonWhyNotAccepted); 
### Parameters
Parameter | Description  
---|---  
element | The element to add.  
reasonWhyNotAccepted | The reason that indicates why the element is not accepted.  
### Returns
**bool** Returns false if the specified element is a scope or group. Otherwise returns true. 
### Description
Whether an element can be added to this group.
* * *
