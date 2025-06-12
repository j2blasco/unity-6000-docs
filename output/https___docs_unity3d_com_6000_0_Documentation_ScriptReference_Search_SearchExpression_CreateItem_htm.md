* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.CreateItem.html

#  [SearchExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html).CreateItem
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
public static [Search.SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) CreateItem(string label, object value, string description); 
## Declaration
public static [Search.SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) CreateItem(string value, string label); 
## Declaration
public static [Search.SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) CreateItem(double value, string label); 
## Declaration
public static [Search.SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) CreateItem(int value, string label); 
### Parameters
Parameter | Description  
---|---  
label | Optional label of the SearchItem. This will be displayed in the search Window.  
value | Initial value of the SearchItem.  
description | Optional description of the SearchItem. This will be displayed in the search Window.  
### Returns
**SearchItem** Returns a new SearchItem. 
### Description
Create a new [SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) from a value with an optional label.
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
