* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/search-tables.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity Search](https://docs.unity3d.com/6000.0/Documentation/Manual/search-overview.html)
  * Search tables


[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-index-manager.html)
The Index Manager
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-providers.html)
Search Providers
# Search tables
You can use Search tables to view, compare, and sort Search items by properties. From the table you can also modify data and export data to a .csv file or JSON.
## View Search tables
To view your search in table format, enter a search query and click the table icon in the bottom right of the Unity Search window.
![View options in the Search window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/search-tables-intro.png) View options in the Search window
By default, the table will show the Label and Description columns unless you have added new columns or you are using a select{} statement that creates new columns from selectors.
Click the column header to sort the search results in ascending or descending order by that column property.
Click the reset icon (![Reset icon](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/search-reset-icon.png)) if no columns appear, or if the columns appear from the previous search and you want to reset to the default column layout.
## Add columns
![Add more columns with the + icon](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/search-tables-add-column.png) Add more columns with the + icon
To add a new column in the search table, click the plus icon (+) and choose a property or selector.
![Column selection: browse the list, or search it](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/search-tables-add-column-select.png) Column selection: browse the list, or search it
## Customize columns
You can customize the name, icon, alignment and whether the column is sortable.
To edit your column, right-click the column header and select **Edit <column name>**.
![Customizing columns from the columns context menu](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/search-tables-edit-column.png) Customizing columns from the column’s context menu Field | Description  
---|---  
**Format** | Changes the data about the results to another format. If the result has no data for the new format (for example asking for color information from position data), the cell will be blank.  
Icon | Changes the icon.  
**Name** | Changes the name of the column  
**Alignment** | Changes the alignment of the column  
**Sortable** | Select to make the column sortable in the table  
**Path** | Indicates the path of the property or sub property which is useful if you need to understand where a property is located.  
**Selector** | Indicates which property is accessed within the search query. This is useful if you wish to create queries for specific properties, for instance if you have a column for the Height property, you can check the Selector field and create a height search query for Assets using `#m_Height`.  
## Arrange columns
Click and hold the column header and drag it to rearrange the columns.
## Delete columns
Right-click the column header and select **Remove <column name>**.
## Show/hide columns
Once your table is set up, you may wish to hide certain columns temporarily without deleting them.
Right-click in the column header area and select **Show Columns > <name of column>**. The columns with a checkmark appear in the table.
## Reset tables
Reset sets the table back to the default, with the Label and Description columns or will include columns specified in the select{} statement.
Click the reset icon (![Reset icon](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/search-reset-icon.png)) to remove all added columns or if the columns appear from the previous search and you want to reset to the default column layout.
**Note:** If you want to keep your current search table column layout, save your table before resetting.
## Save tables
To save your search table column layout:
  * Click the Save icon in the **Saved Searches** User or Project panel area, or the Save icon to the right of the Search field.
Unity Search includes the table layout with the saved search query. When a query is saved with a table its icon changes to the table icon.


## Export table data
You can export table data in JSON or .csv format. When you save using JSON, you can open the saved table data in Unity. This is static data from the time that you saved it that does not refresh.
To export table data:
![The export data option](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/search-tables-export-data.png) The export data option
  1. From the Save drop-down menu, choose **Export Report** (for JSON) or **Export CSV**.
  2. Name your file, choose a location to store your file, then click **Save**


## Modify table data
If you want to modify the data in the table, apply either the [Serialized](https://docs.unity3d.com/6000.0/Documentation/Manual/FormatDescription.html) or [Material](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html)An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material) Property formats to the column you want to modify.
**Note:** Search is not aware of any dependencies on the data in the Search tables. As such, when you use these formats to change the data in the Unity Search tables, it will not trigger any changes to the custom **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) code related to property editing. To make sure that your changes include dependencies or linked changes which are often embedded in custom code for common properties, make your changes in the Inspector instead.
To modify the data in a column do one of the following:
  * Right-click in the header of the column you want to modify and select **Column Format** > **Serialized Property**.
  * Right-click in the header of the column you want to modify and select **Column Format** > **Material Property**. The data in the column is now editable.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-index-manager.html)
The Index Manager
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-providers.html)
Search Providers
