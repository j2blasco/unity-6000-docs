* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryGraphOptimizationOptions.html

# QueryGraphOptimizationOptions
struct in UnityEditor.Search
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
Structure containing the different options used to optimize a query graph.
### Properties
Property | Description  
---|---  
[propagateNotToLeaves](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryGraphOptimizationOptions-propagateNotToLeaves.html) | Propagate "Not" operations to leaves, so only leaves can have "Not" operations as parents.  
[swapFilterFunctionsToRightHandSide](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryGraphOptimizationOptions-swapFilterFunctionsToRightHandSide.html) | Swaps filter functions to the right-hand side of combining operations (i.e. "And", "Or"). Useful if those filter operations are slow.  
[swapNotToRightHandSide](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryGraphOptimizationOptions-swapNotToRightHandSide.html) | Swaps "Not" operations to the right-hand side of combining operations (i.e. "And", "Or"). Useful if a "Not" operation is slow.  
* * *
