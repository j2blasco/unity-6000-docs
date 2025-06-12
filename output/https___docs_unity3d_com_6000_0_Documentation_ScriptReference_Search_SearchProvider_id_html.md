* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-id.html

#  [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html).id
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
id; 
### Description
Search provider unique ID.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class SearchProvider_id
{
    internal static string id = "example_colors";
    internal static string name = "example_Colors";

    [SearchItemProvider]
    internal static SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) CreateProvider()
    {
        return new SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)(id, name)
        {
            filterId = "hex:",
            priority = 99999, // put example provider at a low priority
            showDetailsOptions = ShowDetailsOptions.Description[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Description.html) | ShowDetailsOptions.Preview[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Preview.html),
            fetchItems = (context, items, provider) =>
            {
                var expression = context.searchQuery;
                if (expression.Length == 6 && IsHex(expression))
                {
                    expression = "#" + expression;
                    items.Add(provider.CreateItem(context, expression, GetColorName(expression),
                        "Look at this " + GetColorName(expression) + " color!",
                        CreateTextureFromColor(expression, 64, 64), null));
                }
                return null;
            },
            fetchPreview = (item, context, size, options) =>
            {
                return CreateTextureFromColor(item.id, (int)size.x, (int)size.y);
            },
        };
    }


    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)/id")]
    public static void Run()
    {
        var context = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)(SearchService.GetProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.GetProvider.html)(id));

        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(context.providers.First().id);
    }

    private static Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) CreateTextureFromColor(string color, int width, int height)
    {
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) fillColor;
        if (!ColorUtility.TryParseHtmlString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorUtility.TryParseHtmlString.html)(color, out fillColor))
            return null;
        var texture = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(width, height, TextureFormat.ARGB32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.ARGB32.html), false);
        var fillColorArray = texture.GetPixels32();

        for (var i = 0; i < fillColorArray.Length; ++i)
            fillColorArray[i] = fillColor;

        texture.SetPixels32(fillColorArray);

        texture.Apply();
        return texture;
    }

    private static bool IsHex(string expression)
    {
        foreach (var c in expression)
        {
            if (!Uri.IsHexDigit(c))
                return false;
        }
        return true;
    }

    private static string GetColorName(string color)
    {
        if (color[1] > color[3] && color[1] > color[5])
            return "reddish";
        else if (color[3] > color[1] && color[3] > color[5])
            return "greenish";
        else if (color[5] > color[1] && color[5] > color[3])
            return "bluish";
        return "undefined";
    }
}

```

* * *
