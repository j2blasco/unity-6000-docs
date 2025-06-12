* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelectorAttribute.html

# SearchSelectorAttribute
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
Search selector attribute used to define how a custom value can be selected from a search item.
Here's an example to select the number of line of code of text assets. > select{p: *.cs, @path, @loc}.
```
[SearchSelector("loc", provider: "asset")]
static object SelectLineOfCode(SearchSelectorArgs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelectorArgs.html) args)
{
    TextAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html) textAsset = args.current.ToObject<TextAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html)>();
    if (textAsset)
        return textAsset.text.Split('\n').Length[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.html);  
  
    return null;
}
```

### Properties
Property | Description  
---|---  
[cacheable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelectorAttribute-cacheable.html) | Set the cacheable property if you do not want the search backend to pull cached values from the property database.  
* * *
