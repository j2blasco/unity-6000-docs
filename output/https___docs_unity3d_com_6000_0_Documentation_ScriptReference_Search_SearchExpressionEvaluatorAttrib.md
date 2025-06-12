* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionEvaluatorAttribute-ctor.html

# SearchExpressionEvaluatorAttribute Constructor
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
public SearchExpressionEvaluatorAttribute(params SearchExpressionType[] signatureArgumentTypes); 
## Declaration
public SearchExpressionEvaluatorAttribute(string name, params SearchExpressionType[] signatureArgumentTypes); 
## Declaration
public SearchExpressionEvaluatorAttribute([Search.SearchExpressionEvaluationHints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionEvaluationHints.html) hints, params SearchExpressionType[] signatureArgumentTypes); 
## Declaration
public SearchExpressionEvaluatorAttribute(string name, [Search.SearchExpressionEvaluationHints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionEvaluationHints.html) hints, params SearchExpressionType[] signatureArgumentTypes); 
### Parameters
Parameter | Description  
---|---  
signatureArgumentTypes | Array of types corresponding to the type of the parameters used with this evaluator.  
name | N ame of the evaluator. If no name are specified the name of the evaluator functio will be used.  
hints | Hints to specify to the evaluator runtime how function should be run.  
### Description
Use this attribute to register a static C# function as a new evaluator. SearchExpressionEvaluator when use within a [SearchExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html) can have a signature that is validated against the passed parameters.
Here is an example using a Variadic paramater.
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
Here is an example not supporting thread evaluation.
```
[Description("Returns ids of current selection")]
[SearchExpressionEvaluator(SearchExpressionEvaluationHints.ThreadNotSupported[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionEvaluationHints.ThreadNotSupported.html))]
public static IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> SelectionIds(SearchExpressionContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.html) c)
{
    var instanceIds = UnityEditor.Selection.instanceIDs;
    foreach (var id in instanceIds)
    {
        yield return SearchExpression.CreateItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.CreateItem.html)(id, c.ResolveAlias("selected id"));
    }
}

```

* * *
