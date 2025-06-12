* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.CollectElements.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [Node](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html).CollectElements
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
collectedElementSet | The set of matching edges.  
conditionFunc | A function that determines whether an edge is added to the set of matching edges.  
### Description
Retrieves the set of edges that match a specified condition. The tested edges are connected to this node.
* * *
