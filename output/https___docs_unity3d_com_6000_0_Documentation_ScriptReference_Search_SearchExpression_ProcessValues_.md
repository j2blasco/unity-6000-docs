* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.ProcessValues.html

#  [SearchExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html).ProcessValues
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
public static IEnumerable<SearchItem> ProcessValues(IEnumerable<SearchItem> items, string outputValueFieldName, Func<SearchItem,T> processHandler); 
### Parameters
Parameter | Description  
---|---  
items | Group of items to transform.  
outputValueFieldName | Name of the field in the [SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) to write the value to. If null, we write to the internal value of the item.  
processHandler | Transformer function that need to returns a new value for the item.  
### Returns
**IEnumerable <SearchItem>** Yield a new list of items that have been transformed. 
### Description
Take a group of SearchItems and apply a processHandler transformer function to the item in order to sets its internal value or an outputValueField. Note that these items are processed in the main thread thus allowing you to resolve any kind of selectors.
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
