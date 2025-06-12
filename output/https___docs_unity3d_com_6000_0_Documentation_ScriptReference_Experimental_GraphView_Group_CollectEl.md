* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Group.CollectElements.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [Group](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Group.html).CollectElements
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
public void CollectElements(HashSet<GraphElement> collectedElementSet, Func<GraphElement,bool> conditionFunc); 
### Parameters
Parameter | Description  
---|---  
collectedElementSet | The set of matching graph elements.  
conditionFunc | A function that determines whether a graph element is added to the set of matching graph elements.  
### Description
Retrieves a set of graph elements that match a specified condition. The matching graph elements are selected from this group.
* * *
