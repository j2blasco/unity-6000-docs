* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.RemoveOperator.html

#  [QueryEngine<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).RemoveOperator
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
public void RemoveOperator(string op); 
### Parameters
Parameter | Description  
---|---  
op | The operator identifier.  
### Description
Removes a custom operator that was added on the [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).
```
// Remove an operator based on its token
var operatorToken = "%";
queryEngine.RemoveOperator(operatorToken);

```

* * *
