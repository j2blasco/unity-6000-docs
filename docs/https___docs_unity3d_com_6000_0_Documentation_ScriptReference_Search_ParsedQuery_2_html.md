* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ParsedQuery_2.html

# ParsedQuery<T0,T1>
class in UnityEditor.Search
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
Provides methods to define an operation that can be used to filter a data set.
<TData>: The filtered data type, <TPayload>: The payload type.
### Properties
Property | Description  
---|---  
[errors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ParsedQuery_2-errors.html) | A list of QueryErrors.  
[evaluationGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ParsedQuery_2-evaluationGraph.html) | Query evaluation graph used to evaluate the query.  
[queryGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ParsedQuery_2-queryGraph.html) | Query graph. This graph can be used to walk all the node of the query if you need to do a special type of evaluation.  
[text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ParsedQuery_2-text.html) | The text that generated the query.  
[tokens](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ParsedQuery_2-tokens.html) | The list of tokens found in the query.  
[valid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ParsedQuery_2-valid.html) | Indicates if the query is valid or not.  
### Public Methods
Method | Description  
---|---  
[Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ParsedQuery_2.Apply.html) | Applies the filtering on a payload.  
[GetNodeAtPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ParsedQuery_2.GetNodeAtPosition.html) | Get the query node located at the specified index position in the query.  
[Optimize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ParsedQuery_2.Optimize.html) | Optimizes the query by optimizing the underlying filtering graph.  
* * *
