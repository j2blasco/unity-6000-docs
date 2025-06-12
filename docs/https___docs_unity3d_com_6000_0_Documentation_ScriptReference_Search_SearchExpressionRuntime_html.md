* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionRuntime.html

# SearchExpressionRuntime
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
Encapsulate all the runtime data needed to evaluate a root expression and all its parameters. This class contains the [SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) that created the root [SearchExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html) and all the stack frames needed to evaluate all the nested [SearchExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html).
### Properties
Property | Description  
---|---  
[current](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionRuntime-current.html) | Current SearchExpressionContext corresponding to the stack frame being evaluated.  
[frames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionRuntime-frames.html) | The stack of all SearchExpressionContext being evaluated.  
[items](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionRuntime-items.html) | The stack of SearchItems that have been yielded by each execution frame.  
[search](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionRuntime-search.html) | Initial SearchContext contaning the text that was used to parse the initial root SearchExpression.  
[valid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionRuntime-valid.html) | Is the current runtime valid. This means are there any SearchExpressionContext being evaluated.  
### Public Methods
Method | Description  
---|---  
[Push](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionRuntime.Push.html) | Push a new SearchExpression with its arguments to be evaluated. This is useful if a user defined evaluator needs to generate a new Context of evaluation.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionRuntime.ToString.html) | Get a string representation of the current SearchExpressionRuntime.  
* * *
