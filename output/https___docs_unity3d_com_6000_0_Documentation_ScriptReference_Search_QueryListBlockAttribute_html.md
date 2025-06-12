* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryListBlockAttribute.html

# QueryListBlockAttribute
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
This attribute can be used on a class deriving from [QueryListBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryListBlock.html) to display in query builder mode a special block that will propose a fixed set of values when clicked.
The following example shows how to display a custom list block for the `shader` filter block.
```
[QueryListBlock[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryListBlock.html)("Decal", "Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html)", "shader")]
class ShaderDecalBlockList : QueryListBlock[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryListBlock.html)
{
    public ShaderDecalBlockList(IQuerySource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IQuerySource.html) source, string id, string value, QueryListBlockAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryListBlockAttribute.html) attr)
        : base(source, id, value, attr)
    {
    }

    public override IEnumerable<SearchProposition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProposition.html)> GetPropositions(SearchPropositionFlags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchPropositionFlags.html) flags = SearchPropositionFlags.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchPropositionFlags.None.html))
    {
        var shaderIcon = EditorGUIUtility.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.Load.html)("Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) Icon") as Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html);
        yield return new SearchProposition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProposition.html)(category: null, "HDRP Decal", "Decal", icon: shaderIcon);
        yield return new SearchProposition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProposition.html)(category: null, "URP Decal", "DecalURP", icon: shaderIcon);
    }
}

```

### Properties
Property | Description  
---|---  
[category](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryListBlockAttribute-category.html) | Category.  
[id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryListBlockAttribute-id.html) | Filter id of the block.  
[ids](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryListBlockAttribute-ids.html) | A set of IDs for which the list block will be displayed.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryListBlockAttribute-name.html) | Displayed name of the block.  
[op](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryListBlockAttribute-op.html) | Default operator assigned to the filter when the value changes.  
[type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryListBlockAttribute-type.html) | The list block type is used to get the the icon to be displayed instead of the block name.  
### Constructors
Constructor | Description  
---|---  
[QueryListBlockAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryListBlockAttribute-ctor.html) | Register a list block for a given filter.  
* * *
