* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html

# SearchItem
class in UnityEditor.Search
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
Search items are returned by the search provider to show to the user after a search is performed. The search item holds all the data that is used to sort and present the search results. Some members of a SearchItem can be specified in an asynchronous callback (see SearchItem.fetchThumbnail, SearchItem.fetchDescription, etc).
SearchItems are generally created using the [SearchProvider.CreateItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.CreateItem.html) function. This example shows how to create a SearchItem with all the members.
```
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

```

### Static Properties
Property | Description  
---|---  
[clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-clear.html) | A search item representing none, usually used to clear the selection.  
### Properties
Property | Description  
---|---  
[context](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-context.html) | Context used to create that item.  
[data](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-data.html) | Search provider defined content. It can be used to transport any data to custom search provider handlers (i.e. `fetchDescription`).  
[description](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-description.html) | If no description is provided, SearchProvider.fetchDescription will be called when the item is first displayed.  
[id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-id.html) | Unique ID of the search item for the search provider.  
[label](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-label.html) | Display name of the search item.  
[options](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-options.html) | Flags that dictate how the search item is displayed and used.  
[preview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-preview.html) | Large preview of the search item. Usually cached by fetchPreview.  
[provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-provider.html) | Back pointer to the search provider.  
[score](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-score.html) | The item relevance score will affect how the item gets sorted by the search provider. Lower scored items have more relevance and are prioritzed.  
[this[string]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.Index_operator.html) | Operator used to get an item field value.  
[thumbnail](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-thumbnail.html) | If no thumbnail is provided, SearchProvider.fetchThumbnail is called when the item is first displayed.  
[value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-value.html) | Value set by the search expression system when selecting fields.  
### Constructors
Constructor | Description  
---|---  
[SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-ctor.html) | Construct a search item. A search item needs to have at least a unique ID for a given search query.  
### Public Methods
Method | Description  
---|---  
[CompareTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.CompareTo.html) | Check if two SearchItems have the same ID.  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.Equals.html) | Check if two SearchItems have the same ID.  
[GetDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.GetDescription.html) | Fetch and format description.  
[GetFieldCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.GetFieldCount.html) | Returns the amount of field stored in the search item.  
[GetFieldNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.GetFieldNames.html) | Returns a list of all field names.  
[GetFields](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.GetFields.html) | Enumerate all search items fields.  
[GetHashCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.GetHashCode.html) | Default Hash of a SearchItem.  
[GetLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.GetLabel.html) | Fetch and format label.  
[GetPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.GetPreview.html) | Gets the search item preview if available, otherwise the preview is fetched at this time.  
[GetThumbnail](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.GetThumbnail.html) | Gets the search item thumbnail if available, otherwise the thumbnail is fetched at this time. The thumbnail is usually used in list view compared to the grid view.  
[GetValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.GetValue.html) | Get the default search item value of a given field.  
[RemoveField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.RemoveField.html) | Removes an item field.  
[SetField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.SetField.html) | Sets a field value and alias.  
[ToObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.ToObject.html) | Returns any valid Unity Object held by the search item.  
[TryGetField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.TryGetField.html) | Returns an item field if available.  
[TryGetValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.TryGetValue.html) | Returns' a field's value if any. Compared to SearchItem.TryGetField this method also resolved built-in field such as id, label, description, value, etc.  
* * *
