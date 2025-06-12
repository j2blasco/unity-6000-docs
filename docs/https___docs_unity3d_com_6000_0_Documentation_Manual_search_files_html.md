* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/search-files.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity Search](https://docs.unity3d.com/6000.0/Documentation/Manual/search-overview.html)
  * [Search Providers](https://docs.unity3d.com/6000.0/Documentation/Manual/search-providers.html)
  * Search for files


[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-calculator.html)
The calculator
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-api.html)
Execute API methods
# Search for files
The File Search Provider searches the file system to find files that match a specific pattern.
**NOTE:** This search requires a search token to execute it. You cannot make it an [active Search Provider](https://docs.unity3d.com/6000.0/Documentation/Manual/search-filters.html#persistent-search-filters), or combine it with other Search Providers.
**[Search token](https://docs.unity3d.com/6000.0/Documentation/Manual/search-filters.html#search-tokens):** `find:`
**[Default action](https://docs.unity3d.com/6000.0/Documentation/Manual/search-usage.html#default-actions):** Select the file.
**[Context menu actions](https://docs.unity3d.com/6000.0/Documentation/Manual/search-usage.html#additional-actions):**
Action | Function  
---|---  
**Select** | Selects the file in the **Project** window.  
**Open:** | Opens the file, either in Unity or an external editor.  
**Delete:** | Deletes the file.  
**Copy Path** | Copies the path of the file.  
**Reimport** | Reimports the file.  
**Reveal** | Selects the file in the operating system’s file browser.  
**Properties** | Opens the file’s property settings.  
Your search query can contain a C# regex to perform matching or glob expressions with the following wildcards. A glob expression is converted to a normal regex using the equivalency described in the table below:
Glob wildcards | Description | Example | Matches | Does not match | Equivalent regex  
---|---|---|---|---|---  
* | Matches any number of any characters including none | Law* | Law, Laws, Lawyer | Groklaw, La, aw | .*  
. | Matches any single character including none | Law. | Law, Laws | La, aw | .  
![asset filter](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/search-provider-file.png)  
_File Search Provider_
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-calculator.html)
The calculator
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-api.html)
Execute API methods
