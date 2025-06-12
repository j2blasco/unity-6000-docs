* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-priority.html

#  [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html).priority
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
priority; 
### Description
Hint to sort the search provider. Affects the order of search results and the order in which search providers are shown in the FilterWindow.
The lowest priority is first.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class SearchProvider_priority
{
    static string typeColors = "example_colors_priority";
    static string displayNameColors = "example_Colors_priority";
    static string typeFruits = "example_fruits_priority";
    static string displayNameFruits = "example_Fruits_priority";

    static List<string> colors = new List<string> { "orange", "red", "green", "blue" };
    static List<string> fruits = new List<string> { "orange", "apple", "banana", "strawberry" };

    [SearchItemProvider]
    internal static SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) CreateProviderColors()
    {
        return new SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)(typeColors, displayNameColors)
        {
            priority = 99991,
            filterId = "c:",
            isExplicitProvider = false,
            fetchItems = (context, items, provider) =>
            {
                var expression = context.searchQuery;
                if (colors.Contains(expression))
                {
                    var id = expression + "(color)";
                    items.Add(provider.CreateItem(context, id, id, id, null, null));
                }
                return null;
            }
        };
    }

    [SearchItemProvider]
    internal static SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) CreateProviderFruits()
    {
        return new SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)(typeFruits, displayNameFruits)
        {
            priority = 99992,
            filterId = "f:",
            isExplicitProvider = false,
            fetchItems = (context, items, provider) =>
            {
                var expression = context.searchQuery;
                if (fruits.Contains(expression))
                {
                    var id = expression + "(fruit)";
                    items.Add(provider.CreateItem(context, id, id, id, null, null));
                }
                return null;
            }
        };
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)/priority")]
    public static void Run()
    {
        SearchService.SetActive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.SetActive.html)(typeColors);
        SearchService.SetActive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.SetActive.html)(typeFruits);

        using (var context = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)("orange"))
        {
            // For the purpose if this example, we use the flag synchronous to get the items immediately.
            var results = SearchService.GetItems[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.GetItems.html)(context, SearchFlags.Synchronous[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Synchronous.html));
            // Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) should be the first one (both items have the same score but color provider has the lowest priority).
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(results.Count);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(results[0].description); // "orange(color)";
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(results[1].description); // "orange(fruit)";
        }
    }
}

```

* * *
