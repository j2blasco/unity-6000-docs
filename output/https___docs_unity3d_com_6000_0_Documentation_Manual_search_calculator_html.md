* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/search-calculator.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity Search](https://docs.unity3d.com/6000.0/Documentation/Manual/search-overview.html)
  * [Search Providers](https://docs.unity3d.com/6000.0/Documentation/Manual/search-providers.html)
  * The calculator


[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-settings.html)
Search Settings and Preferences
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-files.html)
Search for files
# The calculator
The Calculator Search Provider computes expressions directly in Search. Enter any expression that is valid in a numerical text field in Unity, and Search displays the result in the results area.
**NOTE:** This search requires a search token to execute it. You cannot make it an [active Search Provider](https://docs.unity3d.com/6000.0/Documentation/Manual/search-filters.html#persistent-search-filters), or combine it with other Search Providers.
**[Search token](https://docs.unity3d.com/6000.0/Documentation/Manual/search-filters.html#search-tokens):** `=` (equals sign)
**[Default action](https://docs.unity3d.com/6000.0/Documentation/Manual/search-usage.html#default-actions):** Logs the result of the expression to the console, and copies it to the clipboard.
**[Context menu actions](https://docs.unity3d.com/6000.0/Documentation/Manual/search-usage.html#additional-actions):**
Action: | Function:  
---|---  
**Exec** | Logs the result of the expression to the console, and copies it to the clipboard.  
> **Note:** To query this provider you need to explicitly add `=` to the query.
**Supported operators:** `+ - * / % ^ ( )`
**Example:** `=42/34 + (56 % 6)`  
  
`=23 * 9 ^ 3`
![The Search window returns the result of a mathmetical expression](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/search-calculator.png)  
_Calculator Search Provider_
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-settings.html)
Search Settings and Preferences
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-files.html)
Search for files
