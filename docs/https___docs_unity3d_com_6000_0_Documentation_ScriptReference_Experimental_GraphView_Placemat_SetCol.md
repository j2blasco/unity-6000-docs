* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Placemat.SetCollapsedElements.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [Placemat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Placemat.html).SetCollapsedElements
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
protected void SetCollapsedElements(IEnumerable<GraphElement> collapsedElements); 
### Parameters
Parameter | Description  
---|---  
collapsedElements | The list of elements to mark as collapsed.  
### Description
Sets the list of collapsed elements. This method is not meant to be called.
The purpose of this method is to be overridden in a derived class. This method is called when a list of elements are collapsed.
* * *
