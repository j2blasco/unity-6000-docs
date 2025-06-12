* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.CollectElements.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [GraphView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.html).CollectElements
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
public static void CollectElements(IEnumerable<GraphElement> elements, HashSet<GraphElement> collectedElementSet, Func<GraphElement,bool> conditionFunc); 
### Parameters
Parameter | Description  
---|---  
elements | The enumerable of graph elements to select from.  
collectedElementSet | The set of matching graph elements.  
conditionFunc | A function that determines whether a graph element is added to the set of matching graph elements.  
### Description
Retrieves the set of elements that match a specified condition. The matching elements are selected from an enumerable of graph elements.
* * *
