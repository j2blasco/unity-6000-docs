* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetNestedQueryHandler.html

#  [QueryEngine<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).SetNestedQueryHandler
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
public void SetNestedQueryHandler(Func<string,string,IEnumerable<TNestedQueryData>> handler); 
### Parameters
Parameter | Description  
---|---  
handler | The function that handles nested queries. It receives the nested query and the filter token on which the query is applied, and returns an IEnumerable.  
### Description
Sets the function that will handle nested queries. Only one handler can be set.
<typeparam name="TNestedQueryData">The type of data returned by the nested query.</typeparam>
* * *
