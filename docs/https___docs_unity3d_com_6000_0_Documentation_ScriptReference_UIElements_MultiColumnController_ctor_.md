* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnController-ctor.html

# MultiColumnController Constructor
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
public MultiColumnController([UIElements.Columns](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.html) columns, [UIElements.SortColumnDescriptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SortColumnDescriptions.html) sortDescriptions, List<SortColumnDescription> sortedColumns); 
### Parameters
Parameter | Description  
---|---  
columns | The columns data used to initialize the header.  
sortDescriptions | The sort data used to initialize the header.  
sortedColumns | The sorted columns for the view.  
### Description
Constructor. It will create the MultiColumnCollectionHeader to use for the view. 
The header will be added to the view in the PrepareView phase.
* * *
