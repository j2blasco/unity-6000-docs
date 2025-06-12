* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.GetFormatString.html

#  [SearchExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html).GetFormatString
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
public static bool GetFormatString([Search.SearchExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html) expr, out string formatStr); 
### Parameters
Parameter | Description  
---|---  
expr | Expression to convert to a format string.  
formatStr | Extracted format string.  
### Returns
**bool** Returns true if the SearchExpression was succesfully converted to a format string. 
### Description
Extract a format string from a given expression. This function should be used to extract a format string from an input parameter of a SearchExpression. For example: the evaluator print{"this is it: @label"} takes a format string as its first parameter.
```
[Description("Convert arguments to a string allowing you to format the result.")]
[SearchExpressionEvaluator(SearchExpressionType.Selector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Selector.html) | SearchExpressionType.Text[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Text.html), SearchExpressionType.Iterable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Iterable.html) | SearchExpressionType.Literal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Literal.html) | SearchExpressionType.Variadic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Variadic.html))]
[SearchExpressionEvaluatorSignatureOverload(SearchExpressionType.Iterable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Iterable.html) | SearchExpressionType.Literal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Literal.html) | SearchExpressionType.Variadic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Variadic.html))]
public static IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> FormatItems(SearchExpressionContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.html) c)
{
    var skipCount = 0;
    if (SearchExpression.GetFormatString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.GetFormatString.html)(c.args[0], out var formatStr))
        skipCount++;
    var items = c.args.Skip(skipCount).SelectMany(e => e.Execute(c));
    var dataSet = SearchExpression.ProcessValues[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.ProcessValues.html)(items, null, item => SearchExpression.FormatItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.FormatItem.html)(c.search, item, formatStr));
    return dataSet;
}

```

* * *
