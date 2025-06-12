* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html

# FrameDataView
class in UnityEditor.Profiling
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
Base funtionality for accessing the Profiler data.
Provides base access to the Profiler data for a specific frame and thread.  
  
Additional resources: [RawFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.html), [HierarchyFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.html).
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
