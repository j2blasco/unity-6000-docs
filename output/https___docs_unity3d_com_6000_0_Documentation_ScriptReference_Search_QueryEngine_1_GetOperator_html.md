* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.GetOperator.html

#  [QueryEngine<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).GetOperator
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
public [Search.QueryFilterOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryFilterOperator.html) GetOperator(string op); 
### Parameters
Parameter | Description  
---|---  
op | The operator identifier.  
### Returns
**QueryFilterOperator** The global [QueryFilterOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryFilterOperator.html). 
### Description
Get a custom operator added on the [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).
This method returns a [QueryFilterOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryFilterOperator.html) that was added on the [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html). If the operator does not exist, the [QueryFilterOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryFilterOperator.html) will be invalid (see [QueryFilterOperator.valid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryFilterOperator-valid.html)).
```
// Get an operator based on its token and add some handlers on it.
var operatorToken = "%";
var operatorObject = queryEngine.GetOperator(operatorToken);
if (operatorObject.valid)
    operatorObject.AddHandler((float ev, float fv) => Math.Abs(ev % fv) < 0.0000001f);

```

See [AddOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddOperator.html) for a complete example.
* * *
