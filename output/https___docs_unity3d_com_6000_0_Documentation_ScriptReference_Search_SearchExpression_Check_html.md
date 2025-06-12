* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.Check.html

#  [SearchExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html).Check
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
public static bool Check([Search.SearchExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html) e, [Search.SearchExpressionContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.html) c); 
### Parameters
Parameter | Description  
---|---  
e | SearchExpression to test.  
c | Execute context of the expression.  
### Returns
**bool** Returns true if the SearchExpression yields more than one item or if the sole item is true. 
### Description
Execute a [SearchExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html) and checks if the internal value of the first yielded [SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) is truish. Not 0, not null, not "" and not false.
* * *
