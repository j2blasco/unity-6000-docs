* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.StackNode.AcceptsElement.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [StackNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.StackNode.html).AcceptsElement
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
protected bool AcceptsElement([Experimental.GraphView.GraphElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphElement.html) element, ref int proposedIndex, int maxIndex); 
### Parameters
Parameter | Description  
---|---  
element | The element to add.  
proposedIndex | The index where the element would be added. This index can be overwritten.  
maxIndex | The maximum value of the index.  
### Returns
**bool** Returns true if the specified GraphElement can be added. Returns false otherwise. 
### Description
Checks whether the specified GraphElement can be added to this StackNode.
* * *
