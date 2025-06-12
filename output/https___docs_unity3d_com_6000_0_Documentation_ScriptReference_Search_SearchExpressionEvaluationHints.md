* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionEvaluationHints.ThreadNotSupported.html

#  [SearchExpressionEvaluationHints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionEvaluationHints.html).ThreadNotSupported
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
Specifies that an evaluator does not support worker thread evaluation and should only be evaluated in the main thread. This could be the case if an evaluator is using non-tread safe Unity API (like [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)).
```
[Description("Returns asset paths corresponding to a list of instance ids")]
[SearchExpressionEvaluator("IdsToPaths", SearchExpressionEvaluationHints.ThreadNotSupported[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionEvaluationHints.ThreadNotSupported.html), SearchExpressionType.Iterable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Iterable.html))]
public static IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> IdsToPath(SearchExpressionContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.html) c)
{
    foreach (var idItem in c.args[0].Execute(c))
    {
        if (SearchExpression.TryConvertToDouble[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.TryConvertToDouble.html)(idItem, out var idNum))
        {
            var id = (int)idNum;
            var path = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(id);
            if (!string.IsNullOrEmpty(path))
            {
                yield return SearchExpression.CreateItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.CreateItem.html)(path, c.ResolveAlias("asset path"));
            }
        }
    }
}

```

* * *
