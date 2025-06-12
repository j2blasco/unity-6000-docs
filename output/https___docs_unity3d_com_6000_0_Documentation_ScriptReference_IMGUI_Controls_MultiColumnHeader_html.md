* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.html

# MultiColumnHeader
class in UnityEditor.IMGUI.Controls
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
The MultiColumnHeader is a general purpose class that e.g can be used with the TreeView to create multi-column tree views and list views.
It supports resizing of columns widths by dragging and provides useful callbacks for reacting to user input. Note that columns can be hidden by the user using the context menu of the MultiColumnHeader.  
  
Terminology used in the API: The parameter name `columnIndex` is used for indices into the columns array in the [MultiColumnHeaderState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeaderState.html) object. While the parameter name `visibleColumnIndex` refers to the currently visible column index shown in the MultiColumnHeader.
### Properties
Property | Description  
---|---  
[allowDraggingColumnsToReorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader-allowDraggingColumnsToReorder.html) | Use this property to control whether the user can drag and drop columns to re-order them.  
[canSort](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader-canSort.html) | Use this property to control whether sorting is enabled for all the columns.  
[currentColumnIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader-currentColumnIndex.html) | The index of the column that is currently being handled during an event. This property can be used for column specific handling when overriding AddColumnHeaderContextMenuItems  
[height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader-height.html) | Customizable height of the multi column header.  
[sortedColumnIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader-sortedColumnIndex.html) | The index of the column that is set to be the primary sorting column. This is the column that shows the sorting arrow above the header text.  
[state](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader-state.html) | This is the state of the MultiColumnHeader.  
### Constructors
Constructor | Description  
---|---  
[MultiColumnHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader-ctor.html) | Constructor.  
### Public Methods
Method | Description  
---|---  
[GetCellRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.GetCellRect.html) | Calculates a cell rect for a column and row using the visibleColumnIndex and rowRect parameters.  
[GetColumn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.GetColumn.html) | Returns the column data for a given column index.  
[GetColumnRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.GetColumnRect.html) | Returns the header column Rect for a given visible column index.  
[GetVisibleColumnIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.GetVisibleColumnIndex.html) | Convert from column index to visible column index.  
[IsColumnVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.IsColumnVisible.html) | Check if a column is currently visible in the MultiColumnHeader.  
[IsSortedAscending](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.IsSortedAscending.html) | Check the sorting order state for a column.  
[OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.OnGUI.html) | Render and handle input for the MultiColumnHeader at the given rect.  
[Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.Repaint.html) | Requests the window which contains the MultiColumnHeader to repaint.  
[ResizeToFit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.ResizeToFit.html) | Resizes the column widths of the columns that have auto-resize enabled to make all the columns fit to the width of the MultiColumnHeader render rect.  
[SetSortDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.SetSortDirection.html) | Change sort direction for a given column.  
[SetSorting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.SetSorting.html) | Sets the primary sorting column and its sorting order.  
[SetSortingColumns](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.SetSortingColumns.html) | Sets multiple sorting columns and the associated sorting orders.  
### Protected Methods
Method | Description  
---|---  
[AddColumnHeaderContextMenuItems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.AddColumnHeaderContextMenuItems.html) | Override this method to extend the default context menu items shown when context clicking the header area.  
[ColumnHeaderClicked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.ColumnHeaderClicked.html) | Override to customize the behavior when clicking a column header.  
[ColumnHeaderGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.ColumnHeaderGUI.html) | Override to customize the GUI of a single column header.  
[OnSortingChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.OnSortingChanged.html) | Called when sorting changes and dispatches the sortingChanged event.  
[OnVisibleColumnsChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.OnVisibleColumnsChanged.html) | Called when the number of visible column changes and dispatches the visibleColumnsChanged event.  
[SortingButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.SortingButton.html) | Provides the button logic for a column header and the rendering of the sorting arrow (if visible).  
[ToggleVisibility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.ToggleVisibility.html) | Method for toggling the visibility of a column.  
### Events
Event | Description  
---|---  
[columnSettingsChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader-columnSettingsChanged.html) | Event raised when any settings from a column has changed (for example, a column width was resized).  
[columnsSwapped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader-columnsSwapped.html) | Event raised when the user switches the order of two columns.  
[sortingChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader-sortingChanged.html) | Subscribe to this event to get notified when sorting has changed.  
[visibleColumnsChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader-visibleColumnsChanged.html) | Subscribe to this event to get notified when the number of visible columns has changed.  
### Delegates
Delegate | Description  
---|---  
[HeaderCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.HeaderCallback.html) | Delegate used for events from the MultiColumnHeader.  
* * *
