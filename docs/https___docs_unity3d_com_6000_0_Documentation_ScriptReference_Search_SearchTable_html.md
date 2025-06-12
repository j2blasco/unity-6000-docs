* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchTable.html

# SearchTable
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
A search table configuration is used to define the columns when search results are displayed in table view.
See [DisplayMode.Table](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.DisplayMode.Table.html).
```
static SearchTable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchTable.html) CreateDecalsTableConfiguration()
{
    var materialIcon = EditorGUIUtility.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.Load.html)("Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) Icon") as Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html);
    var shaderIcon = EditorGUIUtility.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.Load.html)("Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) Icon") as Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html);
    return new SearchTable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchTable.html)("decals", new SearchColumn[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.html)[]
    {
        new SearchColumn[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.html)("DecalsName0", "label", "name", new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Name", materialIcon)) { width = 160 },
        new SearchColumn[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.html)("DecalsShader1", "#shader", "name", new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html)", shaderIcon)) { width = 150 },
        new SearchColumn[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.html)("DecalsBaseColor1", "#_BaseColor", "color", new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)", shaderIcon)) { width = 130 },
    });
}

```

The previous example can be used when creating a [SearchViewState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewState.html).
```
var selectHandler = args.selectorClosedHandler;
var trackingHandler = args.trackingHandler;

var query = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)(CreateDecalProvider(), $"a={dbName} t={selectContext.requiredTypeNames.First()} shader=Decal");
var viewState = SearchViewState.CreatePickerState[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewState.CreatePickerState.html)("decals",
    query,
    selectHandler: (item, canceled) => selectHandler(item?.ToObject(), canceled),
    trackingHandler: (item) => trackingHandler(item?.ToObject()), null,
    SearchViewFlags.TableView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.TableView.html)
    );
viewState.tableConfig = CreateDecalsTableConfiguration();
var materialIcon = EditorGUIUtility.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.Load.html)("Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) Icon") as Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html);
viewState.windowTitle = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) Decals", materialIcon);
viewState.hideAllGroup = true;
viewState.position = SearchUtils.GetMainWindowCenteredPosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetMainWindowCenteredPosition.html)(new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(600, 400));
s_SearchView = SearchService.ShowPicker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowPicker.html)(viewState);

```

### Properties
Property | Description  
---|---  
[columns](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchTable-columns.html) | Search columns displayed in table view.  
[id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchTable-id.html) | Unique id of the search table used for persistance.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchTable-name.html) | Display name of the search table used for serialization.  
### Constructors
Constructor | Description  
---|---  
[SearchTable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchTable-ctor.html) | Creates a new search table configuration.  
### Public Methods
Method | Description  
---|---  
[Clone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchTable.Clone.html) | Creates a copy of the search table configuration.  
[InitFunctors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchTable.InitFunctors.html) | Initialize all search columns functors based on their format provider.  
### Static Methods
Method | Description  
---|---  
[LoadFromFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchTable.LoadFromFile.html) | Load a search table configuraiton from a JSON file.  
* * *
