* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchTable-ctor.html

# SearchTable Constructor
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
public SearchTable(string id, string name, IEnumerable<SearchColumn> columnModels); 
## Declaration
public SearchTable(string name, IEnumerable<SearchColumn> columnModels); 
## Declaration
public SearchTable([Search.SearchTable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchTable.html) other, string newName); 
### Parameters
Parameter | Description  
---|---  
id | Unique id, usually a GUID.  
name | Name of the table.  
columnModels | Set of initial columns.  
other | Table setup to copy columns from.  
newName | New name of the table if copied from an initial table configuration.  
### Description
Creates a new search table configuration.
* * *
