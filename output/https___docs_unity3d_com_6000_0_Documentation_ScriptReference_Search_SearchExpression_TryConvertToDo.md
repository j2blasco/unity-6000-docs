* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.TryConvertToDouble.html

#  [SearchExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html).TryConvertToDouble
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
public static bool TryConvertToDouble([Search.SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, out double value, string selector); 
### Parameters
Parameter | Description  
---|---  
item | SearchItem to extract the value from.  
value | Resulting value.  
selector | Selector use to access an item value. If null, we will use the internal item value.  
### Returns
**bool** Returns true if we were able to select the value and convert it to a double. 
### Description
Resolve a selector on an item and try to convert the selected value to a double.
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
