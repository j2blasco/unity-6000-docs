* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetMarkerCategoryIndex.html

#  [FrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html).GetMarkerCategoryIndex
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
public ushort GetMarkerCategoryIndex(int markerId); 
### Parameters
Parameter | Description  
---|---  
markerId | Marker identifier.  
### Returns
**ushort** Returns Profiler category index. 
### Description
Gets Profiler marker category for the specific marker identifier.
Use to filter samples data by a specific Profiler category.  
The category index is represented by _ushort_ value and refers to one of the following constants in [ProfilerUnsafeUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.html) class:
  * [ProfilerUnsafeUtility.CategoryRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryRender.html),
  * [ProfilerUnsafeUtility.CategoryScripts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryScripts.html),
  * [ProfilerUnsafeUtility.CategoryGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryGUI.html),
  * [ProfilerUnsafeUtility.CategoryPhysics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryPhysics.html),
  * [ProfilerUnsafeUtility.CategoryAnimation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryAnimation.html),
  * [ProfilerUnsafeUtility.CategoryAi](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryAi.html),
  * [ProfilerUnsafeUtility.CategoryAudio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryAudio.html),
  * [ProfilerUnsafeUtility.CategoryVideo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryVideo.html),
  * [ProfilerUnsafeUtility.CategoryParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryParticles.html),
  * [ProfilerUnsafeUtility.CategoryLighting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryLighting.html),
  * [ProfilerUnsafeUtility.CategoryNetwork](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryNetwork.html),
  * [ProfilerUnsafeUtility.CategoryLoading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryLoading.html),
  * [ProfilerUnsafeUtility.CategoryOther](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryOther.html),
  * [ProfilerUnsafeUtility.CategoryVr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryVr.html),
  * [ProfilerUnsafeUtility.CategoryAllocation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryAllocation.html),
  * [ProfilerUnsafeUtility.CategoryVr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryVr.html),
  * [ProfilerUnsafeUtility.CategoryInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryInput.html).


**Throws:**   
_System.ArgumentException_ if _markerId_ is invalid.  
  
Additional resources: [GetMarkerId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetMarkerId.html), [ProfilerUnsafeUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.html).
* * *
