* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.ResolveAlias.html

#  [SearchExpressionContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.html).ResolveAlias
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
public string ResolveAlias(string defaultLabel); 
## Declaration
public string ResolveAlias([Search.SearchExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html) expr, string defaultLabel); 
### Parameters
Parameter | Description  
---|---  
defaultLabel | If no exeuction frames are present this becomes the default alias to be resolved.  
expr | Default expression to look to resolve the alias. If null, use the runtime to resolve the alias.  
### Returns
**string** Returns a resolved alias. 
### Description
Try to resolve an alias value using the [SearchExpressionRuntime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionRuntime.html) attached to this context. Each frame if asked to resolve a [SearchExpression.alias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression-alias.html).
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
