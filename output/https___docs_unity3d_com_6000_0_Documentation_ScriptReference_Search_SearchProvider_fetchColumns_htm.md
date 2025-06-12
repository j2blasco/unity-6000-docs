* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchColumns.html

#  [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html).fetchColumns
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
fetchColumns; 
### Description
Handler used to enumerate search columns to be used in the Search Table view.
See [SearchColumnProviderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnProviderAttribute.html) if you need to define new column formats to display your custom values.
```
static IEnumerable<SearchColumn[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.html)> FetchColumns(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> items)
{
    yield return new SearchColumn[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.html)("Performance/Sample[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.UI.Sample.html) Count", "count", nameof(PerformanceMetric));
    yield return new SearchColumn[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.html)("Performance/Peak Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html)", "peak", nameof(PerformanceMetric));
    yield return new SearchColumn[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.html)("Performance/Average Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html)", "avg", nameof(PerformanceMetric));
    yield return new SearchColumn[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.html)("Performance/Total Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html)", "total", nameof(PerformanceMetric));
}  
  
[SearchColumnProvider(nameof(PerformanceMetric))]
public static void PerformanceMetric(SearchColumn[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.html) column)
{
    column.getter = args =>
    {
        switch (column.selector)
        {
            case "count": return EditorPerformanceTracker.GetSampleCount(args.item.id);
            case "peak": return EditorPerformanceTracker.GetPeakTime(args.item.id);
            case "avg": return EditorPerformanceTracker.GetAverageTime(args.item.id);
            case "total": return EditorPerformanceTracker.GetTotalTime(args.item.id);
            case "age": return EditorPerformanceTracker.GetTimestamp(args.item.id);
        }  
  
        return null;
    };  
  
    if (column.selector != "count")
    {
        column.drawer = args =>
        {
            GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(args.rect, GetTimeLabel((double)args.value, 0.5d, 2.0d), ItemSelectors.GetItemContentStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ItemSelectors.GetItemContentStyle.html)(column));
            return args.value;
        };
    }
}

```

* * *
