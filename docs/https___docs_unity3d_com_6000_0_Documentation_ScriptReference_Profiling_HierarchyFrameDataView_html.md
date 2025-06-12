* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.html

# HierarchyFrameDataView
class in UnityEditor.Profiling
/
Inherits from:[Profiling.FrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html)
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
Provides access to the Profiler data for a specific frame and thread.
Use _HierarchyFrameDataView_ to retrieve Profiler samples structured as a hierarchy.  
This is used in the **Hierachy mode** of the [CPU Usage Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html), for example.  
  
The _HierarchyFrameDataView_ aggregates the data with time and memory information. Each hierarchy item includes accumulated data of its children.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using UnityEditor.Profiling;
using UnityEditorInternal;  
  
public class Example
{
    List<int> parentsCacheList = new List<int>();
    List<int> childrenCacheList = new List<int>();  
  
    public void ProcessFrameData(int frame)
    {
        using (var frameData = ProfilerDriver.GetHierarchyFrameDataView(frame, 0, HierarchyFrameDataView.ViewModes.Default[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.ViewModes.Default.html), HierarchyFrameDataView.columnGcMemory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-columnGcMemory.html), false))
        {
            int rootId = frameData.GetRootItemID();
            frameData.GetItemDescendantsThatHaveChildren(rootId, parentsCacheList);
            foreach (int parentId in parentsCacheList)
            {
                frameData.GetItemChildren(parentId, childrenCacheList);
                // Process further records
            }
        }
    }
}

```

### Static Properties
Property | Description  
---|---  
[columnCalls](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-columnCalls.html) | The Calls column.  
[columnDontSort](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-columnDontSort.html) | The column identifier that indicates whether sorting is disabled.  
[columnGcMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-columnGcMemory.html) | The amount of managed allocations within a sample.  
[columnName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-columnName.html) | The Profiler Sample Name column.  
[columnObjectName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-columnObjectName.html) | The Object Name column.  
[columnSelfPercent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-columnSelfPercent.html) | The percentage of the CPU time Unity spends in a sample itself, excluding the time from child samples.  
[columnSelfTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-columnSelfTime.html) | The CPU time in milliseconds that Unity spends in a sample itself, excluding the time from child samples.  
[columnStartTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-columnStartTime.html) | The start time of a call in milliseconds.  
[columnTotalPercent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-columnTotalPercent.html) | The percentage of the CPU time Unity spends in a sample, including the time from child samples.  
[columnTotalTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-columnTotalTime.html) | The CPU time in milliseconds that Unity spends in a sample, including the time from child samples.  
[columnWarningCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-columnWarningCount.html) | The amount of samples that are inside a code execution path that is suboptimal for performance.  
[invalidSampleId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-invalidSampleId.html) | Index of the invalid item.  
### Properties
Property | Description  
---|---  
[sortColumn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-sortColumn.html) | The column identifier that defines the sort column.  
[sortColumnAscending](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-sortColumnAscending.html) | Whether the sorting order is ascending, true, or descending, false.  
[viewMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-viewMode.html) | The view mode which defines how data is aggregated.  
### Public Methods
Method | Description  
---|---  
[GetItemAncestors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemAncestors.html) | Retrieves a list of hierarchy item ancestors.  
[GetItemCallstack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemCallstack.html) | Gets the callstack associated with the specified hierarchy item.  
[GetItemCategoryIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemCategoryIndex.html) | Gets Profiler marker category for the specific marker identifier.  
[GetItemChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemChildren.html) | Retrieves a list of hierarchy item children.  
[GetItemColumnData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemColumnData.html) | Returns string representation of hierarchy item value associated with the column.  
[GetItemColumnDataAsDouble](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemColumnDataAsDouble.html) | Returns double representation of hierarchy item value associated with the column.  
[GetItemColumnDataAsFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemColumnDataAsFloat.html) | Returns float representation of hierarchy item value associated with the column.  
[GetItemColumnDataAsSingle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemColumnDataAsSingle.html) | Returns float representation of hierarchy item value associated with the column.  
[GetItemDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemDepth.html) | Returns hierarchy level of the item.  
[GetItemDescendantsThatHaveChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemDescendantsThatHaveChildren.html) | Use to retrieve a list of a hierarchy item descendants which have other children.  
[GetItemInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemInstanceID.html) | Returns InstanceID of the UnityEngine.Object associated with the sample.  
[GetItemMarkerFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMarkerFlags.html) | Use to retrieve a marker usage flags.  
[GetItemMarkerID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMarkerID.html) | Returns Profiler marker which uniquely identifies sample name.  
[GetItemMarkerIDPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMarkerIDPath.html) | Use to retrieve a list of a marker identifiers of all hierarchy item parents.  
[GetItemMergedSampleCallstack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMergedSampleCallstack.html) | Gets the callstack associated with the specified hierarchy item.  
[GetItemMergedSamplesColumnData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMergedSamplesColumnData.html) | Use to retrieve a values of merged samples of a hierarchy item.  
[GetItemMergedSamplesColumnDataAsDoubles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMergedSamplesColumnDataAsDoubles.html) | Retrieves the merged samples for a specific hierarchy item. Merged samples are returned as a list of doubles through the outValues param.  
[GetItemMergedSamplesColumnDataAsFloats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMergedSamplesColumnDataAsFloats.html) | Retrieves the merged samples for a specific hierarchy item. Merged samples are returned as a list of floats through the outValues param.  
[GetItemMergedSamplesCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMergedSamplesCount.html) | Return merged samples count represented by the hierarchy item.  
[GetItemMergedSamplesInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMergedSamplesInstanceID.html) | Retrieves the instanceID of the merged samples corresponding to a hierarchy item.  
[GetItemMergedSamplesMetadata](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMergedSamplesMetadata.html) | Returns string representation of hierarchy item metadata value.  
[GetItemMergedSamplesMetadataAsFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMergedSamplesMetadataAsFloat.html) | Returns float representation of hierarchy item metadata value.  
[GetItemMergedSamplesMetadataAsLong](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMergedSamplesMetadataAsLong.html) | Returns long representation of hierarchy item metadata value.  
[GetItemMergedSamplesMetadataCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMergedSamplesMetadataCount.html) | Returns metadata count associated with hierarchy item.  
[GetItemMetadata](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMetadata.html) | Returns string representation of hierarchy item metadata value.  
[GetItemMetadataAsFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMetadataAsFloat.html) | Returns float representation of hierarchy item metadata value.  
[GetItemMetadataAsLong](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMetadataAsLong.html) | Returns long representation of hierarchy item metadata value.  
[GetItemMetadataCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemMetadataCount.html) | Returns metadata count associated with hierarchy item.  
[GetItemName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemName.html) | Gets the sample name associated with the item.  
[GetItemPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemPath.html) | Retrieves the hierarchy item path as a string. Each level is delimited by forward slashes ('/').  
[GetItemRawFrameDataViewIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetItemRawFrameDataViewIndices.html) | Retrieves the raw indices of all samples associated with this Hierarchy item identifier.  
[GetRootItemID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.GetRootItemID.html) | Gets the identifier for the root tree item.  
[HasItemChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.HasItemChildren.html) | Checks whether the tree item has children.  
[ItemContainsRawFrameDataViewIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.ItemContainsRawFrameDataViewIndex.html) | Checks if the provided raw sample index matches any of the raw sample indices associated with this Hierarchy item identifier.  
[ResolveItemCallstack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.ResolveItemCallstack.html) | Gets the callstack associated with the specified hierarchy item.  
[ResolveItemMergedSampleCallstack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.ResolveItemMergedSampleCallstack.html) | Gets the callstack associated with a specific item sample.  
[Sort](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.Sort.html) | Sorts the hierarchy view.  
### Inherited Members
### Static Properties
Property | Description  
---|---  
[invalidMarkerId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-invalidMarkerId.html) | Identifier of the invalid marker.  
[invalidThreadId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-invalidThreadId.html) | This constant defines a thread id that does not match any valid thread's id.  
[invalidThreadIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-invalidThreadIndex.html) | This constant defines a thread index that does not match any valid thread's index.  
### Properties
Property | Description  
---|---  
[frameFps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-frameFps.html) | The current frames per second (FPS) for the frame.  
[frameGpuTimeMs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-frameGpuTimeMs.html) | The amount of GPU frame time in milliseconds.  
[frameGpuTimeNs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-frameGpuTimeNs.html) | The amount of GPU frame time in nanoseconds.  
[frameIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-frameIndex.html) | The frame index for the FrameDataView.  
[frameStartTimeMs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-frameStartTimeMs.html) | The start time of CPU frame in milliseconds.  
[frameStartTimeNs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-frameStartTimeNs.html) | The start time of CPU frame in nanoseconds.  
[frameTimeMs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-frameTimeMs.html) | The amount of CPU frame time in milliseconds.  
[frameTimeNs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-frameTimeNs.html) | The amount of CPU frame time in nanoseconds.  
[maxDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-maxDepth.html) | Maximum child samples levels in the thread data.  
[sampleCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-sampleCount.html) | The amount of samples in the frame for the thread.  
[threadGroupName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-threadGroupName.html) | The name of the group that the thread belongs to.  
[threadId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-threadId.html) | Persistent identifier associated with the thread.  
[threadIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-threadIndex.html) | The index of the thread in the current frame.  
[threadName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-threadName.html) | Name of the thread.  
[valid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-valid.html) | True after the frame data for the thread is processed and ready for retrieval.  
### Public Methods
Method | Description  
---|---  
[GetAllCategories](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetAllCategories.html) | Gets all the available Profiler Categories for the current profiling session.  
[GetCategoryInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetCategoryInfo.html) | Gets the Profiler category information for a given category ID.  
[GetCounterValueAsDouble](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetCounterValueAsDouble.html) | Gets the last value of a counter marker in the frame as a double data type'.  
[GetCounterValueAsFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetCounterValueAsFloat.html) | Gets the last value of a counter marker in the frame as a float data type'.  
[GetCounterValueAsInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetCounterValueAsInt.html) | Gets the last value of a counter marker in the frame as an int data type'.  
[GetCounterValueAsLong](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetCounterValueAsLong.html) | Gets the last value of a counter marker in the frame as a long data type.  
[GetCounterValuePtr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetCounterValuePtr.html) | Gets unsafe pointer to the last value of a counter marker in the frame.  
[GetFrameMetaData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetFrameMetaData.html) | Retrieves metadata associated with the frame.  
[GetFrameMetaDataCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetFrameMetaDataCount.html) | Gets the total number of metadata chunks for each id and tag pair in the frame.  
[GetGfxResourceInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetGfxResourceInfo.html) | Gets information for a given graphics resource identifier.  
[GetMarkerCategoryIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetMarkerCategoryIndex.html) | Gets Profiler marker category for the specific marker identifier.  
[GetMarkerFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetMarkerFlags.html) | Gets Profiler marker flags for the specific marker identifier.  
[GetMarkerId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetMarkerId.html) | Get Profiler marker identifier for a specific name.  
[GetMarkerMetadataInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetMarkerMetadataInfo.html) | Gets Profiler marker metadata information for the specific marker identifier.  
[GetMarkerName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetMarkerName.html) | Gets Profiler marker name for the specific marker identifier.  
[GetMarkers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetMarkers.html) | Gets all available markers for the current profiling session.  
[GetSessionMetaData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetSessionMetaData.html) | Retrieves the metadata of the session this frame occurred in as a NativeArray.  
[GetSessionMetaDataCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetSessionMetaDataCount.html) | Gets the total number of metadata chunks for each id and tag pair in the Profiler session.  
[GetUnityObjectInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetUnityObjectInfo.html) | Gets the UnityEngine.Object information for a given Instance ID.  
[GetUnityObjectNativeTypeInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetUnityObjectNativeTypeInfo.html) | Gets native Unity type intormation.  
[GetUnityObjectNativeTypeInfoCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetUnityObjectNativeTypeInfoCount.html) | Returns native types count in the capture.  
[HasCounterValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.HasCounterValue.html) | Returns true for a marker that includes a counter in the active frame.  
[ResolveMethodInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.ResolveMethodInfo.html) | Returns method name and location information for the specified method address.  
* * *
