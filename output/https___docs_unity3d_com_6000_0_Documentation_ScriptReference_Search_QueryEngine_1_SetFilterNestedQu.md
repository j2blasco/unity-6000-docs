* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetFilterNestedQueryTransformer.html

#  [QueryEngine<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).SetFilterNestedQueryTransformer
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
public void SetFilterNestedQueryTransformer(string filterToken, Func<TNestedQueryData,TRhs> transformer); 
### Parameters
Parameter | Description  
---|---  
filterToken | The identifier of the filter. Typically what precedes the operator in a filter (for example, "id" in "id>=2").  
transformer | The transformer function.  
### Description
Sets a filter's nested query transformer function. This function takes the result of a nested query and extracts the necessary data to compare with the filter.
<typeparam name="TNestedQueryData">The type of data returned by the nested query.</typeparam> <typeparam name="TRhs">The type expected on the right-hand side of the filter.</typeparam>
* * *
