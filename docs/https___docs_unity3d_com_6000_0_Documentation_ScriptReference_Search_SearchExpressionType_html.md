* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.html

# SearchExpressionType
enumeration
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
Type used to characterize an expression. An expression might have multiple types. For example a Set is also an iterable. A keyword is also considered a string value. [SearchExpressionType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.html) can be used with [SearchExpressionEvaluatorAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionEvaluatorAttribute.html) to describe the parameter list of an evaluator.
```
[SearchExpressionEvaluator(SearchExpressionType.Iterable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Iterable.html) | SearchExpressionType.Variadic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Variadic.html))]
[SearchExpressionEvaluatorSignatureOverload(SearchExpressionType.Number[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Number.html), SearchExpressionType.Iterable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Iterable.html) | SearchExpressionType.Variadic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Variadic.html))]
[Description("Extract and returns the X first results for each expression.")]
public static IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> TakeXFirst(SearchExpressionContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.html) c)
{
    var argIndex = 0;
    var takeNumber = 1;
    if (c.args[0].types.HasFlag(SearchExpressionType.Number[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Number.html)))
    {
        ++argIndex;
        takeNumber = Math.Max((int)(c.args[0].GetNumberValue(takeNumber)), 0);
    }

    for ( ; argIndex < c.args.Length; ++argIndex)
    {
        var iterable = c.args[argIndex].Execute(c);
        var taken = 0;
        foreach (var item in iterable)
        {
            if (item == null)
                yield return null;
            else
            {
                yield return item;
                ++taken;
                if (taken == takeNumber)
                {
                    c.Break();
                    break;
                }
            }
        }
    }
}

```

### Properties
Property | Description  
---|---  
[Nil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Nil.html) | Denote an invalid Expression.  
[Optional](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Optional.html) | Used in SearchExpressionEvaluatorAttribute to specify a aprameter to be Optional.  
[Variadic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Variadic.html) | Used in SearchExpressionEvaluatorAttribute to specify that a parameter can be used multiples times. For example count{Iterable1, Iterable2,... IterableN} can be executed with any number of iterables are parameters.  
[Boolean](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Boolean.html) | Denote a Literal expression of a boolean value.  
[Number](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Number.html) | Denote a Literal expression of a numerical value.  
[Text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Text.html) | Denote an expression representing a textual (string) value.  
[Selector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Selector.html) | Denote an expression representing a selector. All selector starts with @. For example @size in expression: select{t:material, @size}.  
[Keyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Keyword.html) | Denote an expression yielding a SearchExpressionKeyword.  
[Set](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Set.html) | Denote an iterable expression of a group of generally literal values. For example [1, 2, 3] or [material, shader, texture2d].  
[Function](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Function.html) | Denotes an expression of an evaluator function. For example: count{}.  
[QueryString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.QueryString.html) | Denote an expression representing a query string. For example: t:shader.  
[Expandable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Expandable.html) | Denotes an expression using the ... operator to tell it can be expanded.  
[Group](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Group.html) | Denote an expression of a group of items. Groups are generated by the groupBy{} evaluator.  
[Literal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Literal.html) | Denote an expression built from a literal values: boolean, number, text or keyword. For example in the set expression [1,"hello",true] all set values are literals.  
[Iterable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Iterable.html) | Denote an expression that can iterated to yield SearchItem. Set: [1, 2, 3], Query String: t:shader and evaluator: count{} are all example of iterables.  
[AnyValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.AnyValue.html) | Denote an expression with a value type: either Literal or Iterable.  
[AnyExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.AnyExpression.html) | Denote any expression of any type (Literal, Iterable or Selector).  
* * *
