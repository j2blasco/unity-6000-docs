* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.html

# SearchExpressionContext
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
This context encapsulate all the datas needed to evaluate a [SearchExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html) and it allows user to interact with the evaluation runtime of an expression. A SearchExpressionContext is created automatically with a [SearchExpressionRuntime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionRuntime.html) anytime [SearchExpression.Execute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.Execute.html) is called.
Here is an example showing ow the SearchExpressionContext is used during evaluation:
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
[args](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext-args.html) | Arguments of passed to the SearchExpression being evaluated.  
[expression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext-expression.html) | [[]SearchExpression] being evaluated.  
[items](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext-items.html) |  SearchItems yielded by the evaluation of a searchExpression.  
[runtime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext-runtime.html) |  SearchExpressionRuntime associated with this context. The runtime stores all runtime data (stack frames, stack of contex and items) necessary for evaluation of a SearchExpression.  
[search](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext-search.html) | SearchContex containing the search query that was parsed to create the SearchExpression.  
[valid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext-valid.html) | Is the current context valid or not. If invalid it means the associated SearchExpression is null or the SearchExiressionRuntime is invalid.  
### Public Methods
Method | Description  
---|---  
[Break](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.Break.html) | Break the evaluation of a SearchExpression meaning items won't be yielded anymore.  
[Continue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.Continue.html) | Tell SearchExpression evaluation to continue.  
[IsBreaking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.IsBreaking.html) | Has the current context being flagged to break execution?  
[IsContinuing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.IsContinuing.html) | Has the current context being flagged to continue execution?  
[ResetIterationControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.ResetIterationControl.html) | Restart evaluation and iteration of SearchExpression.  
[ResolveAlias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.ResolveAlias.html) | Try to resolve an alias value using the SearchExpressionRuntime attached to this context. Each frame if asked to resolve a SearchExpression.alias.  
[ThrowError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.ThrowError.html) | Stop a SearchExpression evaluation by throwing a SearchExceptionEvaluatorException. User writing an evaluator can decide to throw thse exceptions if the parameters passed to evaluation are not valid or if a problem happens during evaluation.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.ToString.html) | Get string representation of a context.  
* * *
