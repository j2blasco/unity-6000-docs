* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column.html

# Column
class in UnityEngine.UIElements
/
Implemented in:[UnityEngine.UIElementsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html)
Leave feedback
  

Implements interfaces:[INotifyBindablePropertyChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.INotifyBindablePropertyChanged.html)
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
Represents a column in multi-column views such as multi-column list view or multi-column tree view. Provides the properties to define how user interacts with a column in a multi-column view, how its data and the data of each cell in this column are represented. 
### Properties
Property | Description  
---|---  
[bindCell](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-bindCell.html) |  Callback for binding the specified data item at the given row to the visual element.   
[bindHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-bindHeader.html) |  Callback for binding the header element to this column.   
[bindingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-bindingPath.html) |  Path of the target property to be bound.   
[cellTemplate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-cellTemplate.html) |  The VisualElement that is the template for each cell of the column.   
[collection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-collection.html) |  The column collection that contains this column.   
[comparison](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-comparison.html) |  The comparison to use when using ColumnSortingMode.Default. Compares two items by their index in the source.   
[destroyCell](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-destroyCell.html) |  Callback for destroying the VisualElement that was built for this column.   
[destroyHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-destroyHeader.html) |  Callback for destroying the visual representation of the column in the header.   
[headerTemplate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-headerTemplate.html) |  The VisualElement that is the template for the header of the column.   
[icon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-icon.html) |  The icon of the column.   
[makeCell](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-makeCell.html) |  Callback for constructing the VisualElement that is the template for each cell of the column.   
[makeHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-makeHeader.html) |  Callback for constructing the visual representation of the column in the header.   
[maxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-maxWidth.html) |  The maximum width of the column.   
[minWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-minWidth.html) |  The minimum width of the column.   
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-name.html) |  The name of the column.   
[optional](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-optional.html) |  Indicates whether the column is optional. Optional columns be shown or hidden interactively by the user.   
[resizable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-resizable.html) |  Indicates whether the column can be resized interactively by the user.   
[sortable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-sortable.html) |  Indicates whether the column can be sorted.   
[stretchable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-stretchable.html) |  Indicates whether the column will be automatically resized to fill the available space within its container.   
[title](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-title.html) |  The title of the column.   
[unbindCell](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-unbindCell.html) |  Callback for unbinding the specified data item at the given row from the visual element.   
[unbindHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-unbindHeader.html) |  Callback for unbinding the header element to this column.   
[visible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-visible.html) |  Indicates whether the column is visible.   
[width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-width.html) |  The desired width of the column.   
### Events
Event | Description  
---|---  
[propertyChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column-propertyChanged.html) |  Called when a property has changed.   
* * *
