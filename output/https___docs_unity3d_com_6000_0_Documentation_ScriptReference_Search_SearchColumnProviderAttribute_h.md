* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnProviderAttribute.html

# SearchColumnProviderAttribute
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
The search column provider attribute is used to define new formats for a given column.
Search column formats are equivalent to formats in a spreadsheet application. They define how the data in a column cell is manipulated and displayed.
```
[SearchColumnProvider("Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)")]
public static void InitializeColorColumn(SearchColumn[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.html) column)
{
    column.drawer = args =>
    {
        if (args.value is Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) c)
            return EditorGUI.ColorField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ColorField.html)(args.rect, GUIContent.none[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-none.html), c, showEyedropper: false, showAlpha: true, hdr: false);
        return args.value;
    };
}

```

Here is an example using search column delegates to manipulate the data.
```
[SearchColumnProvider("GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)/Enabled")]
public static void InitializeObjectReferenceColumn(SearchColumn[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.html) column)
{
    column.getter = args => GetEnabled(args.item);
    column.drawer = args => DrawEnabled(args);
    column.setter = args => SetEnabled(args);
}

```

### Properties
Property | Description  
---|---  
[provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnProviderAttribute-provider.html) | Unique name of the search column provider.  
* * *
