* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/search-assets.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity Search](https://docs.unity3d.com/6000.0/Documentation/Manual/search-overview.html)
  * [Search Providers](https://docs.unity3d.com/6000.0/Documentation/Manual/search-providers.html)
  * Search Project Assets


[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-providers.html)
Search Providers
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-scene.html)
Search the current Scene
# Search Project Assets
Use the Asset Search Provider to search all Assets in the current Project. You can search using keywords or GUIDs (Instance IDs).
You can also search the [Asset Database](https://docs.unity3d.com/6000.0/Documentation/Manual/search-assets.html#asset-search-provider-vs-asset-database-search) or the [file system](https://docs.unity3d.com/6000.0/Documentation/Manual/search-assets.html#searching-the-file-system) from the Search window.
**[Search token](https://docs.unity3d.com/6000.0/Documentation/Manual/search-filters.html#search-tokens):** `p:` (for “project”)
**[Default action](https://docs.unity3d.com/6000.0/Documentation/Manual/search-usage.html#default-actions):** Open the Asset, either in Unity or in an external editor.
**[Context menu actions](https://docs.unity3d.com/6000.0/Documentation/Manual/search-usage.html#additional-actions):**
Action: | Function:  
---|---  
**Select** | Selects the Asset in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow).  
**Open** | Opens the Asset, either in Unity or in an external editor.  
**Delete** | Deletes the Asset.  
**Copy Path** | Copies the path of the Asset.  
**Reimport** | Reimports the Asset.  
**Reveal** | Selects the Asset in the operating system’s file browser.  
**Properties** | Opens the Asset’s property settings.  
![Search results for the Assets Search provider](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/search-provider-asset.png)  
_Asset Search Provider_
## Asset Search Provider vs. Asset Database search
Search uses its own Asset indexer, which is faster and more flexible than the Asset Database or the Project Browser.
For example:
  * You can type a file extension and it will find all Assets with that extension.
  * It matches against directory name
  * It does a partial search


## Search the file system
If you use the asterisk (*****) in a query, Search performs both a normal search and a wildcard search against the file systems. This allows you to include files not indexed by the Asset database in your searches.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-providers.html)
Search Providers
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-scene.html)
Search the current Scene
