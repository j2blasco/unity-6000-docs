* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorEngineAttribute.html

# ObjectSelectorEngineAttribute
class in UnityEditor.SearchService
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
Use this class attribute to register ObjectSelector search engines automatically. Search engines with this attribute must implement the [IObjectSelectorEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.IObjectSelectorEngine.html) interface.
The following example creates an ObjectSelector search engine:
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEditor.SearchService;
using Object = UnityEngine.Object;

[ObjectSelectorEngine]
class TestObjectSelectorSearchEngine : IObjectSelectorEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.IObjectSelectorEngine.html)
{
    public string name => "My Custom Engine";

    public void BeginSession(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context)
    {
    }

    public void EndSession(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context)
    {
        // EndSession can be called in two ways:
        // 1. Naturally when the onObjectSelectorClosed is called upon closing the window (which you should do in your window).
        // 2. Forcefully when a new session is started before the current one is finished.
        // In the second case, we need to close the window to avoid any issues since the ObjectSelector API does not support concurrent selectors.
        if ((((ObjectSelectorSearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorSearchContext.html))context).endSessionModes & ObjectSelectorSearchEndSessionModes.CloseSelector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorSearchEndSessionModes.CloseSelector.html)) != 0 && ObjectSelectorWindow.instance != null)
        {
            ObjectSelectorWindow.instance.Close();
        }
    }

    public void BeginSearch(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context, string query)
    {
        // Not called.
    }

    public void EndSearch(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context)
    {
        // Not called.
    }

    public bool SelectObject(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<Object, bool> onObjectSelectorClosed, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<Object> onObjectSelectedUpdated)
    {
        ObjectSelectorWindow.Show((ObjectSelectorSearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorSearchContext.html))context, onObjectSelectedUpdated, onObjectSelectorClosed);
        return true;
    }

    public void SetSearchFilter(ISearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ISearchContext.html) context, string searchFilter)
    {
        ObjectSelectorWindow.instance.searchText = searchFilter;
    }
}

```

The following example creates an object selector window that displays returned items as a list of names and paths:
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.SearchService;
using UnityEditor.UIElements;
using UnityEngine.UIElements;
using Object = UnityEngine.Object;

public class ObjectSelectorWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    public class ItemInfo
    {
        public int instanceId;
        public string label;
        public bool isAsset;
        public GlobalObjectId[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html) globalObjectId;
    }

    static ObjectSelectorSearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorSearchContext.html) s_Context;
    static Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<Object> s_OnSelectionChanged;
    static Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<Object, bool> s_OnSelectorClosed;
    public static ObjectSelectorWindow instance { get; private set; }

    List<ItemInfo> m_FilteredItems;
    ToolbarSearchField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToolbarSearchField.html) m_Searchbox;
    ListView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListView.html) m_ListView;
    string m_SearchText;
    ItemInfo m_CurrentItem;
    bool m_Canceled = true;

    public bool initialized { get; private set; } = false;

    public string searchText
    {
        get => m_SearchText;
        set
        {
            m_SearchText = value;
            FilterItems();
        }
    }

    public List<ItemInfo> allItems { get; private set; }

    public static void Show(ObjectSelectorSearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorSearchContext.html) context, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<Object> onSelectionChanged, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<Object, bool> onSelectorClosed)
    {
        s_Context = context;
        s_OnSelectionChanged = onSelectionChanged;
        s_OnSelectorClosed = onSelectorClosed;

        // Create a window with CreateInstance, and show it.
        var window = CreateInstance<ObjectSelectorWindow>();
        instance = window;
        window.Show();
    }

    void Init()
    {
        m_SearchText = "";
        allItems = new List<ItemInfo>();
        m_FilteredItems = new List<ItemInfo>();

        if ((s_Context.visibleObjects & VisibleObjects.Assets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.VisibleObjects.Assets.html)) == VisibleObjects.Assets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.VisibleObjects.Assets.html))
            allItems.AddRange(FetchAllAssets());
        if ((s_Context.visibleObjects & VisibleObjects.Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.VisibleObjects.Scene.html)) == VisibleObjects.Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.VisibleObjects.Scene.html))
            allItems.AddRange(FetchAllGameObjects(s_Context));

        allItems.Sort((item, other) => item.label.CompareTo(other.label));
        m_FilteredItems.AddRange(allItems);
    }

    void OnEnable()
    {
        Init();

        m_Searchbox = new ToolbarSearchField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToolbarSearchField.html)();
        m_Searchbox.RegisterValueChangedCallback(SearchFilterChanged);
        m_Searchbox.style.flexGrow = 1;
        m_Searchbox.style.maxHeight = 16;
        m_Searchbox.style.width = Length.Percent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.Percent.html)(100f);
        m_Searchbox.style.marginRight = 4;
        rootVisualElement.Add(m_Searchbox);

        m_ListView = new ListView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListView.html)(m_FilteredItems, 16, MakeItem, BindItem);
        m_ListView.selectionChanged += ItemSelectionChanged;
        m_ListView.itemsChosen += ItemsChosen;
        m_ListView.style.flexGrow = 1;
        rootVisualElement.Add(m_ListView);

        // Initialize selection
        if (s_Context.currentObject != null)
        {
            var currentSelectedId = s_Context.currentObject.GetInstanceID();
            var selectedIndex = m_FilteredItems.FindIndex(item => item.instanceId == currentSelectedId);
            if (selectedIndex >= 0)
                m_ListView.selectedIndex = selectedIndex;
        }

        FinishInit();
    }

    void FinishInit()
    {
        EditorApplication.delayCall[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-delayCall.html) += () =>
        {
            m_ListView.Focus();
            initialized = true;
        };
    }

    void OnDisable()
    {
        // Call the onSelectorClosed callback when the window is closing.
        s_OnSelectorClosed?.Invoke(GetCurrentObject(), m_Canceled);
        instance = null;
    }

    void SearchFilterChanged(ChangeEvent<string> evt)
    {
        searchText = evt.newValue;
    }

    void FilterItems()
    {
        m_FilteredItems.Clear();
        m_FilteredItems.AddRange(allItems.Where(item => string.IsNullOrEmpty(searchText) || item.label.IndexOf(searchText, StringComparison.InvariantCultureIgnoreCase) >= 0));

        m_ListView.Rebuild();
    }

    void BindItem(VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) listItem, int index)
    {
        if (index < 0 || index >= m_FilteredItems.Count)
            return;

        var label = listItem as Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html);
        if (label == null)
            return;
        label.text = m_FilteredItems[index].label;
    }

    static VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) MakeItem()
    {
        return new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)();
    }

    void ItemSelectionChanged(IEnumerable<object> selectedItems)
    {
        m_CurrentItem = selectedItems.FirstOrDefault() as ItemInfo;
        s_OnSelectionChanged?.Invoke(GetCurrentObject());
    }

    void ItemsChosen(IEnumerable<object> selectedItems)
    {
        m_CurrentItem = selectedItems.FirstOrDefault() as ItemInfo;
        m_Canceled = false;
        Close();
    }

    static IEnumerable<ItemInfo> FetchAllAssets()
    {
        var allPaths = AssetDatabase.GetAllAssetPaths();
        if (allPaths == null)
            yield break;

        var requiredTypes = s_Context.requiredTypeNames != null ? s_Context.requiredTypeNames.ToList() : new List<string>();
        foreach (var path in allPaths)
        {
            var type = AssetDatabase.GetMainAssetTypeAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetMainAssetTypeAtPath.html)(path);
            var typeName = type.FullName ?? "";
            if (requiredTypes.Any(requiredType => typeName.Contains(requiredType)))
            {
                var asset = AssetDatabase.LoadMainAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html)(path);
                var globalObjectId = GlobalObjectId.GetGlobalObjectIdSlow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.GetGlobalObjectIdSlow.html)(asset);
                var instanceId = asset?.GetInstanceID() ?? 0;
                yield return new ItemInfo { instanceId = instanceId, label = path, isAsset = true, globalObjectId = globalObjectId };
            }
        }
    }

    static IEnumerable<ItemInfo> FetchAllGameObjects(ObjectSelectorSearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorSearchContext.html) context)
    {
        var property = new HierarchyProperty(HierarchyType.GameObjects, false);

        var requiredTypes = s_Context.requiredTypeNames != null ? s_Context.requiredTypeNames.ToList() : new List<string>();
        while (property.Next(null))
        {
            var objectReferenced = property.pptrValue;
            if (objectReferenced == null)
                continue;
            var globalObjectId = GlobalObjectId.GetGlobalObjectIdSlow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.GetGlobalObjectIdSlow.html)(property.instanceID);
            var typeName = objectReferenced.GetType().FullName ?? "";
            if (requiredTypes.Any(requiredType => typeName.Contains(requiredType)))
                yield return new ItemInfo { instanceId = property.instanceID, label = property.name, isAsset = false, globalObjectId = globalObjectId };
        }
    }

    Object GetCurrentObject()
    {
        if (m_CurrentItem == null)
            return null;
        var currentInstanceId = m_CurrentItem.instanceId;
        if (m_CurrentItem.isAsset)
        {
            var asset = AssetDatabase.LoadMainAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html)(m_CurrentItem.label);
            currentInstanceId = asset.GetInstanceID();
        }
        return EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(currentInstanceId);
    }
}

```

* * *
