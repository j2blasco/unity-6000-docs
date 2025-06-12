* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.FramePrev.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [GraphView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.html).FramePrev
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
public [Experimental.GraphView.EventPropagation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.EventPropagation.html) FramePrev(); 
## Declaration
public [Experimental.GraphView.EventPropagation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.EventPropagation.html) FramePrev(Func<GraphElement,bool> predicate); 
### Parameters
Parameter | Description  
---|---  
predicate | The predicate used to sort the list of all existing graph element.  
### Returns
**EventPropagation** Continue if no elements in graph, Stop otherwise. 
### Description
Focus view on the previous element before the one currently selected.
* * *
