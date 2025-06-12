* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue.SetupEngine.html

#  [SearchValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue.html).SetupEngine
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
public static void SetupEngine(QueryEngine<T> queryEngine); 
### Parameters
Parameter | Description  
---|---  
queryEngine | Query engine to add extended search value filters and parsers.  
### Description
Extended a query engine to work with dynamic search values.
Here's a few example of custom providers that use the extended search value when setting up a [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html).
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;  
  
static class EasySearchProviderExample
{
    enum ExampleProvider { win, material, shader, folder, component, project, res }  
  
    /// <summary>
    /// Search opened editor windows
    /// </summary>
    [SearchItemProvider]
    public static SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) ExampleWindows()
    {
        return EasySearchProvider.Create(ExampleProvider.win.ToString(), _ => Resources.FindObjectsOfTypeAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html)<EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)>())
            .AddAction("select", win => win.Focus())
            .AddFilter("floating", "Floating", win => !win.docked)
            .AddOption(ShowDetailsOptions.Inspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Inspector.html))
            .AddOption(EasyOptions.DisplayFilterValueInDescription)
            .AddByReflectionActions();
    }  
  
    /// <summary>
    /// Search any loaded material and select them in the inspector.
    /// </summary>
    [SearchItemProvider]
    public static SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) ExampleMaterials()
    {
        return EasySearchProvider.Create(_ => Resources.FindObjectsOfTypeAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html)<Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)>())
            .AddAction("select", o => Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) = o)
            .AddOption(ShowDetailsOptions.Actions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Actions.html) | ShowDetailsOptions.Inspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Inspector.html))
            .RemoveOption(ShowDetailsOptions.Description[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Description.html));
    }  
  
    /// <summary>
    /// Search any loaded shader.
    /// Select them in the inspector.
    /// View the shader source in the preview inspector.
    /// </summary>
    [SearchItemProvider]
    public static SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) ExampleShaders()
    {
        static string ReadSource(Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader)
        {
            var shaderPath = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(shader);
            if (string.IsNullOrEmpty(shaderPath))
                return ShaderUtil.GetShaderData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.GetShaderData.html)(shader).ToString();
            if (System.IO.File.Exists(shaderPath))
                return $"<size=8>{System.IO.File.ReadAllText(shaderPath)}</size>";
            return shaderPath;
        }  
  
        static string FetchShaderSource(Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader, SearchItemOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.html) options)
        {
            if ((options & SearchItemOptions.FullDescription[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.FullDescription.html)) != 0)
                return ReadSource(shader) ?? shader.ToString();
            return AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(shader);
        }  
  
        return EasySearchProvider.Create(_ => Resources.FindObjectsOfTypeAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html)<Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html)>())
            .AddAction("select", o => Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) = o)
            .AddOption(ShowDetailsOptions.Actions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Actions.html) | ShowDetailsOptions.Inspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Inspector.html) | ShowDetailsOptions.Description[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Description.html))
            .AddFilter("source", "Source Code", s => ReadSource(s))
            .SetDescriptionHandler(FetchShaderSource);
    }  
  
    /// <summary>
    /// Search any active game object component.
    /// </summary>
    [SearchItemProvider]
    public static SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) ExampleComponents()
    {
        return EasySearchProvider.Create(_ => Resources.FindObjectsOfTypeAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html)<Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html)>())
            .SetDescriptionHandler((obj, options) => obj.GetType().FullName)
            .AddAction("ping", o => EditorGUIUtility.PingObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.PingObject.html)(o.gameObject))
            .AddAction("select", o => Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) = o)
            .AddOption(ShowDetailsOptions.Actions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Actions.html) | ShowDetailsOptions.Inspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Inspector.html))
            .RemoveOption(ShowDetailsOptions.Description[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Description.html));
    }  
  
    /// <summary>
    /// Search all project folders.
    /// </summary>
    /// <returns></returns>
    [SearchItemProvider]
    public static SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) ExampleFolders()
    {
        var folderIcon = EditorGUIUtility.FindTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.FindTexture.html)("Folder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Folder.html) Icon");
        return EasySearchProvider.Create(ExampleProvider.folder.ToString(), "Folders",
            _ => System.IO.Directory.EnumerateDirectories("Assets", "*", System.IO.SearchOption.AllDirectories).Select(d => d.Replace("  
", "/")))
            .SetThumbnailHandler(dir => folderIcon)
            .AddAction("open", dir => EditorUtility.RevealInFinder(dir))
            .AddAction("select", dir => Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) =AssetDatabase.LoadMainAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html)(dir))
            .AddOption(EasyOptions.DescriptionSameAsLabel | EasyOptions.SortByName);
    }  
  
    /// <summary>
    /// Search editor bundle resources.
    /// Note: that bundle resources are cached once.
    /// </summary>
    /// <returns></returns>
    [SearchItemProvider]
    public static SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) ExampleEditorBundles()
    {
        Func<UnityEngine.Object, bool> FR = r => string.Equals(AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(r), "Library/unity editor resources", StringComparison.Ordinal);
        return EasySearchProvider.Create(ExampleProvider.res.ToString(), "Resources[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html)", Resources.FindObjectsOfTypeAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html)<UnityEngine.Object>().Where(FR))
            .SetDescriptionHandler(r => $"{r.GetType().FullName} ({r.GetInstanceID()})")
            .AddAction("select", o => Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) = o)
            .AddAction("copy", "Copy Name", r => EditorGUIUtility.systemCopyBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-systemCopyBuffer.html) = r.name)
            .AddOption(ShowDetailsOptions.Actions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Actions.html) | ShowDetailsOptions.Inspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Inspector.html))
            .AddOption(EasyOptions.YieldAllItemsIfSearchQueryEmpty);
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/Search/Easy")]
    public static void ShowProvider()
    {
        SearchService.ShowContextual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowContextual.html)(Enum.GetValues(typeof(ExampleProvider)).Cast<ExampleProvider>().Select(e => e.ToString()).ToArray());
    }
}

```

Easy search providers.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEditor.Search.Providers;
using UnityEngine;  
  
[Flags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)]
enum EasyOptions
{
    None = 0,  
  
    YieldAllItemsIfSearchQueryEmpty = 1 << 5,
    DescriptionSameAsLabel = 1 << 6,
    SortByName = 1 << 7,
    DisplayFilterValueInDescription = 1 << 8,
}  
  
static class EasyOptionsExtensions
{
    public static bool HasAny(this EasyOptions flags, in EasyOptions f) => (flags & f) != 0;
    public static bool HasAll(this EasyOptions flags, in EasyOptions all) => (flags & all) == all;
}  
  
static class EasySearchProvider
{
    public static EasySearchProvider<T> Create<T>(string id, Func<SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html), IEnumerable<T>> fetchObjects)
    {
        return Create(id, null, fetchObjects);
    }  
  
    public static EasySearchProvider<T> Create<T>(Func<SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html), IEnumerable<T>> fetchObjects)
    {
        return Create(typeof(T).Name.ToLowerInvariant(), null, fetchObjects);
    }  
  
    public static EasySearchProvider<T> Create<T>(string id, string label, Func<SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html), IEnumerable<T>> fetchObjects)
    {
        return new EasySearchProvider<T>(id, label, fetchObjects);
    }  
  
    public static EasySearchProvider<T> Create<T>(string id, string label, IEnumerable<T> objects)
    {
        return new EasySearchProvider<T>(id, label, objects);
    }
}  
  
readonly struct EasyFilter
{
    public readonly string name;
    public readonly string label;
    public readonly Func<object, object> func;  
  
    public EasyFilter(string name, string label, Func<object, object> func)
    {
        this.name = name;
        this.label = label;
        this.func = func;
    }
}  
  
class EasySearchProvider<T> : SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)
{
    private bool m_FiltersAdded;
    private EasyOptions m_Options;
    private QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<T> m_QueryEngine;
    private List<EasyFilter> m_Filters;  
  
    private T[] m_CachedObjects;
    private Func<SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html), IEnumerable<T>> m_FetchObjects;  
  
    public EasySearchProvider(string id, string displayName, IEnumerable<T> objects)
        : this(id, displayName, null as Func<SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html), IEnumerable<T>>)
    {
        m_CachedObjects = objects.ToArray();
        m_FetchObjects = _ => m_CachedObjects;
    }  
  
    public EasySearchProvider(string id, string displayName, Func<SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html), IEnumerable<T>> fetchObjects)
        : base(id, displayName ?? ObjectNames.NicifyVariableName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.NicifyVariableName.html)(typeof(T).Name))
    {
        active = false;
        m_FetchObjects = fetchObjects;
        m_Filters = new List<EasyFilter>();  
  
        showDetails = false;
        showDetailsOptions = ShowDetailsOptions.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.None.html);
        fetchItems = (context, items, provider) => FetchItems(context);
        fetchPropositions = FetchPropositions;
        fetchDescription = FetchDescription;
        fetchThumbnail = FetchThumbnail;
        startDrag = StartDrag;
        toObject = ToObject;  
  
        m_QueryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<T>();
        m_QueryEngine.SetSearchDataCallback(SearchWords, s => s.ToLowerInvariant(), StringComparison.Ordinal);
        SearchValue.SetupEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue.SetupEngine.html)(m_QueryEngine);  
  
        var dataType = typeof(T);
        if (!dataType.IsPrimitive && dataType != typeof(string))
        {
            AddByReflectionFilters();
            AddFilter("t", "Object Type", obj => obj.GetType().Name);
        }
    }  
  
    public EasySearchProvider<T> AddOption(in EasyOptions options)
    {
        m_Options |= options;
        return this;
    }  
  
    public EasySearchProvider<T> AddOption(ShowDetailsOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.html) showDetailsOptions)
    {
        this.showDetailsOptions |= showDetailsOptions;
        this.showDetails = this.showDetailsOptions != ShowDetailsOptions.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.None.html);
        return this;
    }  
  
    public EasySearchProvider<T> AddAction(string name, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<T> handler)
    {
        actions.Insert(0, new SearchAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction.html)(id, name,
            new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)(ObjectNames.NicifyVariableName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.NicifyVariableName.html)(name)),
            (items) => ActionToDataHandler(items, handler)));
        return this;
    }  
  
    public EasySearchProvider<T> AddAction(string name, string label, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<T> handler)
    {
        actions.Insert(Math.Min(1, actions.Count), new SearchAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction.html)(id, name, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)(label),
            (items) => ActionToDataHandler(items, handler)));
        return this;
    }  
  
    public EasySearchProvider<T> RemoveOption(ShowDetailsOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.html) showDetailsOptions)
    {
        this.showDetailsOptions &= ~showDetailsOptions;
        this.showDetails = this.showDetailsOptions != ShowDetailsOptions.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.None.html);
        return this;
    }  
  
    public EasySearchProvider<T> SetDescriptionHandler(Func<T, SearchItemOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.html), string> handler)
    {
        fetchDescription = (item, context) => FetchObjectDescription(item, context, handler);
        return AddOption(ShowDetailsOptions.Description[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Description.html));
    }  
  
    public EasySearchProvider<T> SetDescriptionHandler(Func<T, string> handler)
    {
        return SetDescriptionHandler((T o, SearchItemOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.html) options) => handler(o));
    }  
  
    public EasySearchProvider<T> SetThumbnailHandler(Func<T, Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)> handler)
    {
        this.fetchThumbnail = (item, context) => FetchObjectThumbnail(item, context, handler);
        return this;
    }  
  
    public EasySearchProvider<T> AddFilter<TResult>(string filter, in string label, Func<T, TResult> func)
    {
        if (m_Filters.Any(f => string.Equals(f.name, filter, StringComparison.Ordinal)))
            return this;  
  
        m_Filters.Add(new EasyFilter(filter, label, o => func((T)o)));
        m_QueryEngine.AddFilter(filter, func);
        return this;
    }  
  
    public EasySearchProvider<T> AddByReflectionActions()
    {
        foreach (var m in typeof(T).GetMethods().OrderBy(m => m.Name))
        {
            if (m.GetParameters().Length[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.html) > 0 || m.IsStatic)
                continue;  
  
            actions.Add(new SearchAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction.html)(id, m.Name) { handler = item => HandleMethod(item, m), closeWindowAfterExecution = false });
        }
        return this;
    }  
  
    void StartDrag(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context)
    {
        var data = (T)item.data;
        DragAndDrop.PrepareStartDrag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.PrepareStartDrag.html)();
        if (data is UnityEngine.Object uo)
            DragAndDrop.objectReferences[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop-objectReferences.html) = new [] { uo };
        else
            DragAndDrop.SetGenericData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.SetGenericData.html)(item.data.GetType().Name, item.data);
        DragAndDrop.StartDrag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.StartDrag.html)(GetName(data));
    }  
  
    string FetchObjectDescription(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, Func<T, SearchItemOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.html), string> handler)
    {
        if (item.data is T obj)
            return handler(obj, item.options);
        return null;
    }  
  
    Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) FetchObjectThumbnail(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, Func<T, Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)> handler)
    {
        if (item.data is T obj)
            return handler(obj);
        return null;
    }  
  
    void ActionToDataHandler(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)[] items, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<T> handler)
    {
        foreach (var item in items)
        {
            if (item.data is T obj)
                handler(obj);
        }
    }  
  
    void AddByReflectionFilters()
    {
        foreach (var prop in typeof(T).GetProperties())
        {
            var type = Nullable.GetUnderlyingType(prop.PropertyType) ?? prop.PropertyType;
            var filterName = ObjectNames.NicifyVariableName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.NicifyVariableName.html)(prop.Name).Replace(" ", "").ToLowerInvariant();
            AddFilter(filterName, $"C# {type.Name}", obj => FetchPropertyValue(obj, prop));
        }  
  
        foreach (var prop in typeof(T).GetFields())
        {
            var type = Nullable.GetUnderlyingType(prop.FieldType) ?? prop.FieldType;
            var filterName = ObjectNames.NicifyVariableName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.NicifyVariableName.html)(prop.Name).Replace(" ", "").ToLowerInvariant();
            AddFilter(filterName, $"C# {type.Name}", obj => FetchPropertyValue(obj, prop));
        }
    }  
  
    IEnumerable<SearchProposition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProposition.html)> FetchPropositions(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, SearchPropositionOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchPropositionOptions.html) options)
    {
        foreach (var f in m_Filters)
            yield return new SearchProposition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProposition.html)(f.name, f.name, f.label);
    }  
  
    IEnumerable<string> SearchWords(T obj)
    {
        yield return GetName(obj).ToLowerInvariant();
        yield return obj.ToString().ToLowerInvariant();
    }  
  
    string GetName(T obj)
    {
        if (TryGetProperty(obj, "name", out var objName) && objName is string ons && !string.IsNullOrEmpty(ons))
            return ons.ToString();
        return obj.ToString();
    }  
  
    bool TryGetProperty(in T obj, string name, out object value)
    {
        var p = obj.GetType().GetProperty(name);
        if (p != null)
        {
            value = p.GetValue(obj);
            return true;
        }  
  
        value = null;
        return false;
    }  
  
    IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> FetchItems(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context)
    {
        if (string.IsNullOrEmpty(context.searchQuery))
        {
            if (HasOption(EasyOptions.YieldAllItemsIfSearchQueryEmpty))
                return SortObjects(m_FetchObjects(context)).Select((o, index) => CreateItem(context, GetName(o), index, o));
            return Enumerable.Empty<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)>();
        }  
  
        if (!m_FiltersAdded)
            AddFilters(m_FetchObjects(context).FirstOrDefault());  
  
        var query = m_QueryEngine.Parse(context.searchQuery);
        if (!query.valid)
        {
            context.AddSearchQueryErrors(query.errors.Select(e => new SearchQueryError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryError.html)(e, context, this)));
            return Enumerable.Empty<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)>();
        }  
  
        return SearchItems(context, query);
    }  
  
    string FetchDescription(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context)
    {
        if ((item.options & SearchItemOptions.Compacted[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.Compacted.html)) != 0 || m_Options.HasAny(EasyOptions.DescriptionSameAsLabel))
            return item.GetLabel(context);  
  
        if (m_Options.HasAny(EasyOptions.DisplayFilterValueInDescription))
        {
            var description = "";
            foreach (var f in m_Filters)
            {
                if (context.searchQuery.LastIndexOf(f.name) == -1)
                    continue;  
  
                if (description.Length != 0)
                    description += ", ";
                description += $"{f.name}={f.func(item.data)}";
            }  
  
            return description;
        }  
  
        return item.data.ToString();
    }  
  
    private Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) FetchThumbnail(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context)
    {
        if (item.data is UnityEngine.Object uo)
            return AssetPreview.GetMiniThumbnail[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPreview.GetMiniThumbnail.html)(uo);
        return EditorGUIUtility.FindTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.FindTexture.html)(item.data.GetType().Name);
    }  
  
    private UnityEngine.Object ToObject(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, Type type)
    {
        return item.data as UnityEngine.Object;
    }  
  
    IEnumerable<T> SortObjects(IEnumerable<T> items)
    {
        if (m_Options.HasAny(EasyOptions.SortByName))
            items = items.OrderBy(e => GetName(e));
        return items;
    }  
  
    IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> SearchItems(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, Query<T> query)
    {
        int index = 0;
        foreach (var o in SortObjects(m_FetchObjects(context)))
        {
            if (o == null || o.Equals(default(T)))
            {
                yield return null;
                continue;
            }  
  
            if (!query.Test(o))
            {
                yield return null;
                continue;
            }  
  
            var score = index++;
            var name = GetName(o);
            if (!m_Options.HasAny(EasyOptions.SortByName))
                score = ComputeScore(name);
            yield return CreateItem(context, name, score, o);
        }
    }  
  
    void AddFilters(T o)
    {
        if (o == null)
            return;  
  
        if (o is UnityEngine.Object uo)
        {
            using (var so = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(uo))
            {
                var p = so.GetIterator();
                var next = p.NextVisible(true);
                while (next)
                {
                    var propertyPath = p.propertyPath;
                    var filterName = ObjectNames.NicifyVariableName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.NicifyVariableName.html)(propertyPath).Replace(" ", "").ToLowerInvariant();  
  
                    AddFilter(filterName, $"{p.displayName} ({p.propertyType})", obj => FetchPropertyValue(obj, propertyPath));
                    next = p.NextVisible(p.hasChildren);
                }
            }
        }  
  
        m_FiltersAdded = true;
    }  
  
    private void HandleMethod(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, MethodInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.MethodInfo.html) mi)
    {
        var result = mi.Invoke(item.data, null);
        var unityObject = item.data as UnityEngine.Object;
        if (result != null)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(result, unityObject);
        else
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Executed {mi.DeclaringType.FullName}.{mi.Name}", unityObject);
    }  
  
    SearchValue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue.html) FetchPropertyValue(in T obj, in FieldInfo prop) => new SearchValue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue.html)(prop.GetValue(obj));
    SearchValue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue.html) FetchPropertyValue(in T obj, in PropertyInfo prop) => new SearchValue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue.html)(prop.GetValue(obj));  
  
    SearchValue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue.html) FetchPropertyValue(in T obj, in string propertyPath)
    {
        if (obj is UnityEngine.Object uo)
        {
            using (var so = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(uo))
            {
                var p = so.FindProperty(propertyPath);
                if (p == null)
                    return SearchValue.invalid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue-invalid.html);
                return SearchValue.ConvertPropertyValue(p);
            }
        }  
  
        return SearchValue.invalid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue-invalid.html);
    }  
  
    SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) CreateItem(in SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, in string name, in int score, in T o)
    {
        if (o == null)
            return null;
        return CreateItem(context, Guid.NewGuid().ToString("N"), score, name, null, null, o);
    }  
  
    int ComputeScore(in string name)
    {
        if (name.Length > 2)
        {
            var sp = Math.Max(0, name.LastIndexOf('/'));
            if (sp + 2 < name.Length)
                return name[sp] * 5 + name[sp + 1] * 2 + name[sp + 2];
        }
        return 99;
    }  
  
    bool HasOption(in EasyOptions option)
    {
        return m_Options.HasAny(option);
    }
}
```

* * *
