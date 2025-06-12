* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.ThrowError.html

#  [SearchExpressionContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.html).ThrowError
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
public void ThrowError(string message); 
## Declaration
public void ThrowError(string message, stringView errorPosition); 
### Description
Stop a [SearchExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html) evaluation by throwing a SearchExceptionEvaluatorException. User writing an evaluator can decide to throw thse exceptions if the parameters passed to evaluation are not valid or if a problem happens during evaluation.
* * *
