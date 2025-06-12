* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.html

# Columns
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
Represents a collection of columns. 
### Properties
Property | Description  
---|---  
[Count](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.Count.html) |  Gets the number of columns in the collection.   
[IsReadOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.IsReadOnly.html) |  Gets a value indicating whether the collection is readonly.   
[primaryColumnName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns-primaryColumnName.html) |  Indicates the column that needs to be considered as the primary column, by ID.   
[reorderable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns-reorderable.html) |  Indicates whether the columns can be reordered interactively by user.   
[resizable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns-resizable.html) |  Indicates whether the columns can be resized interactively by user.   
[resizePreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns-resizePreview.html) |  Indicates whether columns are resized as the user drags resize handles or only upon mouse release.   
[stretchMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns-stretchMode.html) |  Indicates how the size of columns in this collection is automatically adjusted as other columns or the containing view get resized. The default value is StretchMode.GrowAndFill  
[this[int]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.Index_operator.html) |  Returns the column at the specified index.   
### Public Methods
Method | Description  
---|---  
[Add](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.Add.html) |  Adds a column at the end of the collection.   
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.Clear.html) |  Removes all columns from the collection.   
[Contains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.Contains.html) |  Whether the columns contain the specified name.   
[CopyTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.CopyTo.html) |  Copies the elements of the current collection to a Array, starting at the specified index.   
[GetEnumerator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.GetEnumerator.html) |  Returns an enumerator that iterates through the collection.   
[IndexOf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.IndexOf.html) |  Returns the index of the specified column if it is contained in the collection; returns -1 otherwise.   
[Insert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.Insert.html) |  Inserts a column into the current instance at the specified index.   
[IsPrimary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.IsPrimary.html) |  Checks if the specified column is the primary one.   
[Remove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.Remove.html) |  Removes the first occurence of a column from the collection.   
[RemoveAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.RemoveAt.html) |  Removes the column at the specified index.   
[ReorderDisplay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.ReorderDisplay.html) |  Reorders the display of a column at the specified source index, to the destination index.   
### Events
Event | Description  
---|---  
[propertyChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns-propertyChanged.html) |  Called when a property has changed.   
* * *
