* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContextAttribute-ctor.html

# SearchContextAttribute Constructor
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
public SearchContextAttribute(string query); 
## Declaration
public SearchContextAttribute(string query, [Search.SearchViewFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.html) flags); 
## Declaration
public SearchContextAttribute(string query, string providerIdsCommaSeparated); 
## Declaration
public SearchContextAttribute(string query, string providerIdsCommaSeparated, [Search.SearchViewFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.html) flags); 
## Declaration
public SearchContextAttribute(string query, params Type[] instantiableProviders); 
## Declaration
public SearchContextAttribute(string query, [Search.SearchViewFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.html) flags, params Type[] instantiableProviders); 
## Declaration
public SearchContextAttribute(string query, [Search.SearchViewFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.html) flags, string providerIdsCommaSeparated, params Type[] instantiableProviders); 
### Parameters
Parameter | Description  
---|---  
query | Initial search query text used to open the Object Picker window.  
flags | Search view flags used to open the Object Picker in various states.  
providerIdsCommaSeparated | A list of Search Provider IDs that will be used to create the search context.  
instantiableProviders | Search provider concrete types that will be instantiated and assigned to the Object Picker search context.  
### Description
Search context constructor used to add some search context to an object field.
```
const string assetProviders = "adb;asset";
const string objectProviders = "adb,asset,scene";
const SearchViewFlags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.html) pickerMinimalUIFlags = SearchViewFlags.Packages[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.Packages.html) |
    SearchViewFlags.IgnoreSavedSearches[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.IgnoreSavedSearches.html) |
    SearchViewFlags.DisableSavedSearchQuery[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.DisableSavedSearchQuery.html) |
    SearchViewFlags.OpenInBuilderMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.OpenInBuilderMode.html) |
    SearchViewFlags.DisableBuilderModeToggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.DisableBuilderModeToggle.html) |
    SearchViewFlags.IgnoreSavedSearches[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.IgnoreSavedSearches.html);

[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("cub", "adb", SearchViewFlags.ObjectPickerAdvancedUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.ObjectPickerAdvancedUI.html) | SearchViewFlags.ListView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.ListView.html) | SearchViewFlags.IgnoreSavedSearches[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.IgnoreSavedSearches.html))] public MonoScript[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) myProjectScript;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("script", "adb", SearchViewFlags.Packages[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.Packages.html) | SearchViewFlags.CompactView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.CompactView.html))] public MonoScript[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) myPackageScript;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("t:texture", assetProviders, SearchViewFlags.ObjectPickerAdvancedUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.ObjectPickerAdvancedUI.html) | SearchViewFlags.GridView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.GridView.html))] public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) myTexture;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("t:texture", assetProviders, SearchViewFlags.ObjectPickerAdvancedUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.ObjectPickerAdvancedUI.html) | SearchViewFlags.GridView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.GridView.html))] public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)[] myTextureArray;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("t:texture", assetProviders, SearchViewFlags.ObjectPickerAdvancedUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.ObjectPickerAdvancedUI.html) | SearchViewFlags.GridView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.GridView.html))] public List<Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)> myTextureList;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("t:texture", "adb", SearchViewFlags.OpenInspectorPreview[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.OpenInspectorPreview.html))] public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) myTextureWithInspector;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("non_mobile", SearchViewFlags.Centered[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.Centered.html))] public UnityEngine.Object myAnyObject;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("non_mobile", SearchViewFlags.Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.Debug.html))] public UnityEngine.Object myDebugObject;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("t:mesh is:nested mesh", "asset")] public UnityEngine.Object assetMesh;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("h: cube", "scene")] public MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html) sceneMesh;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("shader:standard", assetProviders, SearchViewFlags.HideSearchBar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.HideSearchBar.html))] public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) materialNoSearchBar;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("select{p:t:material, @label, @size}", objectProviders, SearchViewFlags.TableView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.TableView.html))] public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) selectMaterial;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("Assets/Queries[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Queries.html)/textures.asset", assetProviders)] public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) searchQueryPathTexture;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("3c7f5dff3fb5d724688dfcecfb131b2a", assetProviders)] public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) searchQueryGuidTexture;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("non_mobile", SearchViewFlags.ObjectPickerAdvancedUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.ObjectPickerAdvancedUI.html) | SearchViewFlags.EnableSearchQuery[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.EnableSearchQuery.html))] public UnityEngine.Object myObjectWithSearchQueryEnabled;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("non_mobile", SearchViewFlags.ObjectPickerAdvancedUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.ObjectPickerAdvancedUI.html) | SearchViewFlags.DisableInspectorPreview[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.DisableInspectorPreview.html))] public UnityEngine.Object myObjectWithInspectorDisabled;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("p: t:texture", "asset", SearchViewFlags.ObjectPickerAdvancedUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.ObjectPickerAdvancedUI.html) | SearchViewFlags.OpenInBuilderMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.OpenInBuilderMode.html))] public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) myTextureWithBuilder;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("p: t:texture", "asset", SearchViewFlags.OpenInBuilderMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.OpenInBuilderMode.html) | SearchViewFlags.DisableBuilderModeToggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.DisableBuilderModeToggle.html))] public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) myTextureWithBuilderNoToggle;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("p: t:texture", "asset", SearchViewFlags.OpenInTextMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.OpenInTextMode.html) | SearchViewFlags.DisableBuilderModeToggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.DisableBuilderModeToggle.html))] public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) myTextureNoBuilderNoToggle;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("t:currentobject{@type, 'texture'}", "asset")] public UnityEngine.Object myObjectWithContext;

[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("light")] public UnityEngine.GameObject lightSearch;
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("camera", SearchViewFlags.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.None.html))] public UnityEngine.GameObject cameraSearch;

public UnityEngine.GameObject noSearchContext;

#if USE_QUERY_BUILDER
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("p: t:<$list:Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html), [Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html), Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html), Prefab]$>", "asset", SearchViewFlags.OpenInBuilderMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.OpenInBuilderMode.html) | SearchViewFlags.DisableBuilderModeToggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.DisableBuilderModeToggle.html))] public UnityEngine.Object myObjectOfConstrainedTypes;
#endif

```

* * *
