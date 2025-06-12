* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-isExplicitProvider.html

#  [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html).isExplicitProvider
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
isExplicitProvider; 
### Description
This search provider is only active when specified explicitly using the filterId.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class SearchProvider_isExplicitProvider
{
    internal static string type = "example_uppercase_isExplicitProvider";
    internal static string displayName = "example_UpperCase_isExplicitProvider";

    [SearchItemProvider]
    internal static SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) CreateProvider()
    {
        return new SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)(type, displayName)
        {
            filterId = "+",
            priority = 99999, // put example provider at a low priority
            isExplicitProvider = true,
            fetchItems = (context, items, provider) =>
            {
                var expression = context.searchQuery;
                expression += " -> " + expression.ToUpper();

                items.Add(provider.CreateItem(context, context.searchQuery.ToUpper(), context.searchQuery.ToUpper(), expression, null, null));
                return null;
            }
        };
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)/isExplicitProvider")]
    public static void Run()
    {
        SearchService.SetActive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.SetActive.html)(type);
        using (var context = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)(""))
        {
            // For the context of this example, we set the flag synchronous so we can get the results right away.
            context.options |= SearchFlags.Synchronous[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.Synchronous.html);
            // If we don't specify the filterId for an explicit provider, there will be no results.
            context.searchText = "uppercase String";

            var results = SearchService.GetItems[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.GetItems.html)(context);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(results.Count); // 0;

            // Use the filterId for an explicit provider
            context.searchText = "+uppercase String";
            results = SearchService.GetItems[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.GetItems.html)(context);
            // There should be only one result with that specific description
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(results.Count); // 1;
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(results[0].description); // "uppercase String -> UPPERCASE STRING";
        }
    }
}

```

* * *
