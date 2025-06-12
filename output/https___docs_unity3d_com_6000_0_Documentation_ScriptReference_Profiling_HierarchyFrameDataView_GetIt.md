* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMarkerIDPath.html

#  [HierarchyFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.html).GetItemMarkerIDPath
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
public void GetItemMarkerIDPath(int id, List<int> outFullIdPath); 
### Parameters
Parameter | Description  
---|---  
id | Hierarchy item identifier.  
outFullIdPath | List filled with marker identifiers of all ancestors of the item as a result of a method call.  
### Description
Use to retrieve a list of a marker identifiers of all hierarchy item parents.
The result is written to _outFullIdPath_ list which is resized if necessary. The list contains marker identifiers of item parents in top-down order. When [HierarchyFrameDataView.ViewModes.InvertHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.ViewModes.InvertHierarchy.html) is active, the sample stack is inverted so that each item's children represents the parent samples in the captured data.
* * *
