* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.ItemContainsRawFrameDataViewIndex.html

#  [HierarchyFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.html).ItemContainsRawFrameDataViewIndex
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
public bool ItemContainsRawFrameDataViewIndex(int id, int sampleIndex); 
### Parameters
Parameter | Description  
---|---  
id | Hierarchy item identifier.  
sampleIndex | The particular profiler sample index that should be checked if it is represented by this hierarchy item.  
### Returns
**bool** True if the sample index is represented by this hierarchy item, false if it is not. 
### Description
Checks if the provided raw sample index matches any of the raw sample indices associated with this Hierarchy item identifier.
When HierarchyFrameDataView.ViewMode.MergeSamplesWithTheSameName is active, Unity merges multiple samples with the same name at the same hierarchy level together in a single item.  
  
As a result of this behavior, and the hierarchical structure of the samples in _HierarchyFrameDataView_ , the **Hierarchy item identifiers** that _HierarchyFrameDataView_ uses, do not correspond to the **sample indices** that [RawFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.html) uses. To get these indices to use with [RawFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.html), use _GetItemRawFrameDataViewIndices_.  
  
However, if you only want to confirm that an item in the _HierarchyFrameDataView_ corresponds to a particular **sample index** you can use _ItemContainsRawFrameDataViewIndex_ to confirm that without the need to retrieve the entire list of **sample indices**.  
  
**Throws:**  
_System.ArgumentException_ if _id_ is invalid.  
  
Additional resources: [HierarchyFrameDataView.GetItemMergedSamplesCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMergedSamplesCount.html), [HierarchyFrameDataView.GetItemRawFrameDataViewIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemRawFrameDataViewIndices.html), [RawFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.html).
* * *
