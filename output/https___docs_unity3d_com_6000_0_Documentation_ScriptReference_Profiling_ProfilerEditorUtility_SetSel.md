* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerEditorUtility.SetSelection.html

#  [ProfilerEditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerEditorUtility.html).SetSelection
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
public static bool SetSelection([Profiling.IProfilerFrameTimeViewSampleSelectionController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.IProfilerFrameTimeViewSampleSelectionController.html) controller, string markerNameOrMarkerNamePath, long frameIndex, string threadGroupName, string threadName, ulong threadId); 
### Parameters
Parameter | Description  
---|---  
controller | The controller object of the Profiler module whose selection you want to set. When the value is null, Unity throws a NullArgumentException.  
markerNameOrMarkerNamePath | The name of the sample to be selected, or the names of all samples in the sample stack. Separate each name with a `/`, ending on the sample that should be selected. Do not add a trailing `/`. If Unity cannot find a sample that matches this name or sample stack, it does not set a selection and this method returns false. When this value is null or an empty string, Unity throws an ArgumentException.  
frameIndex | The 0 based frame index. This value defaults to -1 which means the selection is set on the currently shown frame. Note that the Profiler Window UI shows the frame index as n+1. When this value is outside of the range described by [ProfilerWindow.firstAvailableFrameIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-firstAvailableFrameIndex.html) and [ProfilerWindow.lastAvailableFrameIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-lastAvailableFrameIndex.html), or not -1, Unity throws an ArgumentOutOfRangeException.  
threadGroupName | The name of the thread group. The parameter defaults to an empty string. Null or an empty string signify that the thread isn't part of a thread group. "Job", "Loading" and "Scripting Threads" are examples of such thread group names.  
threadName | The Name of the thread, e.g. "Main Thread", "Render Thread" or "Worker 0". This parameter defaults to "Main Thread". When this value is null or an empty string, Unity throws an ArgumentException.  
threadId | The ID of the thread. When the default value of [FrameDataView.invalidThreadId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-invalidThreadId.html) is passed, Unity searches for the sample in the first thread matching the provided threadGroupName and threadName. Specify this threadId if there are multiple threads with the same name. Use a RawFrameDataView.threadId or HierarchyFrameDataView.threadId to retrieve the ID to a specific thread, if you need it to be specific.  
### Returns
**bool** Returns true if the selection was successfully set, false if it was rejected because no fitting sample could be found. 
### Description
Set the current selection in a frame time sample based Profiler Module, such as the [CPU Usage module](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html) and the [GPU Usage Profiler module](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerGPU.html).
Use these extension methods to [IProfilerFrameTimeViewSampleSelectionController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.IProfilerFrameTimeViewSampleSelectionController.html) to search for a sample according to its name or Profiler Marker Id, the frame and the thread it occurred in and optionally a sample stack within which it should be found. If a sample matching these criteria is found, this method will return true and you can get the details on the found and set selection via [IProfilerFrameTimeViewSampleSelectionController.selection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.IProfilerFrameTimeViewSampleSelectionController-selection.html).  
  
When no frame data is available in the Profiler Window, Unity throws an Exception. You can check that [ProfilerWindow.firstAvailableFrameIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-firstAvailableFrameIndex.html) is greater or equal to 0 to validate that frame data is available.  
  
When the specified thread can not be found, Unity throws an ArgumentException.  
  
If you know the rawSampleIndex to the sample you want to select, you can use [IProfilerFrameTimeViewSampleSelectionController.SetSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.IProfilerFrameTimeViewSampleSelectionController.SetSelection.html) directly to set the selection. Additional resources: [IProfilerFrameTimeViewSampleSelectionController.SetSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.IProfilerFrameTimeViewSampleSelectionController.SetSelection.html) and [IProfilerFrameTimeViewSampleSelectionController.ClearSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.IProfilerFrameTimeViewSampleSelectionController.ClearSelection.html).
* * *
## Declaration
public static bool SetSelection([Profiling.IProfilerFrameTimeViewSampleSelectionController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.IProfilerFrameTimeViewSampleSelectionController.html) controller, long frameIndex, string threadGroupName, string threadName, string sampleName, string markerNamePath, ulong threadId); 
## Declaration
public static bool SetSelection([Profiling.IProfilerFrameTimeViewSampleSelectionController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.IProfilerFrameTimeViewSampleSelectionController.html) controller, long frameIndex, string threadGroupName, string threadName, int sampleMarkerId, List<int> markerIdPath, ulong threadId); 
### Parameters
Parameter | Description  
---|---  
controller | The controller object of the Profiler module whose selection you want to set. When the value is null, Unity throws a NullArgumentException.  
frameIndex | The 0 based frame index. Note that the Profiler Window UI shows the frame index as n+1. When this value is outside of the range described by [ProfilerWindow.firstAvailableFrameIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-firstAvailableFrameIndex.html) and [ProfilerWindow.lastAvailableFrameIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-lastAvailableFrameIndex.html), or smaller than 0, Unity throws an ArgumentOutOfRangeException.  
threadGroupName | The name of the thread group. Null or an empty string signify that the thread isn't part of a thread group. "Job", "Loading" and "Scripting Threads" are examples of such thread group names.  
threadName | The Name of the thread, e.g. "Main Thread", "Render Thread" or "Worker 0". When this value is null or an empty string, Unity throws an ArgumentException.  
sampleName | The name of the sample to select. If Unity cannot find a sample that matches this name, it does not set a selection and this method returns false. When this value is null or an empty string, Unity throws an ArgumentNullException or ArgumentException respectively.  
markerNamePath | The names of all samples in the sample stack, each separated by a `/`, that define the base path for the search. Similar to a file folder structure, this base path defines where Unity looks for a sample which matches the sampleName. The searched sampleName can be the last item in that marker path or any child sample of it. Do not add a trailing `/`. If no sample can be found matching this sample stack path and the sampleName, no selection is set and this method returns false. This defaults to null which means no requirement is set on the sample's sample stack and the first sample fitting the sampleName is selected.  
threadId | The ID of the thread. When the default value of [FrameDataView.invalidThreadId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-invalidThreadId.html) is passed, Unity searches for the sample in the first thread matching the provided threadGroupName and threadName. Specify this threadId if there are multiple threads with the same name. Use a RawFrameDataView.threadId or HierarchyFrameDataView.threadId to retrieve the ID to a specific thread, if you need it to be specific.  
sampleMarkerId | Use [HierarchyFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.html) or [RawFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.html) to get the Marker Ids. When no sample can be found matching this sample stack path and the sampleMarkerId, no selection is set and this method returns false.  
markerIdPath | A list of Profiler marker IDs for all samples in the sample stack, that define the base path for the search. Similar to a file folder structure, this base path defines where Unity looks for a sample which matches the sampleMarkerId. The searched sampleMarkerId can be the last item in that marker path or any child sample of it. If no sample can be found matching this sample stack path and the sampleMarkerId, no selection is set and this method returns false. This defaults to null which means no requirement is set on the sample's sample stack and the first sample fitting the sampleMarkerId is selected.  
### Returns
**bool** Returns true if the selection was successfully set, false if it was rejected because no fitting sample could be found. 
### Description
Set the current selection in a frame time sample based Profiler Module, such as the [CPU Usage module](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html) and the [GPU Usage Profiler module](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerGPU.html).
Use these extension methods to [IProfilerFrameTimeViewSampleSelectionController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.IProfilerFrameTimeViewSampleSelectionController.html) to search for a sample according to its name or Profiler Marker Id, the frame and the thread it occurred in and optionally a sample stack within which it should be found. If a sample matching these criteria is found, this method will return true and you can get the details on the found and set selection via [IProfilerFrameTimeViewSampleSelectionController.selection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.IProfilerFrameTimeViewSampleSelectionController-selection.html).  
  
When no frame data is available in the Profiler Window, Unity throws an Exception. You can check that [ProfilerWindow.firstAvailableFrameIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-firstAvailableFrameIndex.html) is greater or equal to 0 to validate that frame data is available.  
  
When no frame data is available in the Profiler Window, Unity throws an Exception. You can check that [ProfilerWindow.firstAvailableFrameIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-firstAvailableFrameIndex.html) is greater or equal to 0 to validate that frame data is available.  
  
When the specified thread can not be found, Unity throws an ArgumentException.  
  
If you know the rawSampleIndex to the sample you want to select, you can use [IProfilerFrameTimeViewSampleSelectionController.SetSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.IProfilerFrameTimeViewSampleSelectionController.SetSelection.html) directly to set the selection. Additional resources: [IProfilerFrameTimeViewSampleSelectionController.SetSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.IProfilerFrameTimeViewSampleSelectionController.SetSelection.html) and [IProfilerFrameTimeViewSampleSelectionController.ClearSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.IProfilerFrameTimeViewSampleSelectionController.ClearSelection.html).
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Profiling;
using UnityEditorInternal;
using UnityEngine;  
  
// This example assumes the profiled scene contained a component of MyScript.cs:
/* using UnityEngine;  
  
public class MyScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        MethodWithABoxingAllocation();
    }  
  
    object MethodWithABoxingAllocation()
    {
        return 1;
    }
}*/  
  
public class Example : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    const string k_MainThreadGroupName = "";
    const string k_MainThreadName = "Main Thread";
    const string k_GCAllocSampleName = "GC.Alloc";
    // Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) samples that were instrumented by Unity's Message[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Message.html) Invoking mechanism,
    // e.g. Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)(), Start(), FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)() ... get an " [Invoke]" postfix
    const string k_InvokePostFix = " [Invoke]";
    public enum UpdateNameMatchType
    {
        Short,
        Full,
    }  
  
    ProfilerWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow.html) m_Profiler = null;
    UpdateNameMatchType m_UpdateNameMatchType = UpdateNameMatchType.Short;
    bool m_UseMarkerNames = true;  
  
    string GetUpdateSampleName(UpdateNameMatchType updateNameMatchType, bool deepProfiling)
    {
        switch (updateNameMatchType)
        {
            case UpdateNameMatchType.Short:
                if (deepProfiling)
                    return k_UpdateSampleNameShort;
                return k_UpdateSampleNameShort + k_InvokePostFix;
            case UpdateNameMatchType.Full:
                if (deepProfiling)
                    return k_UpdateSampleNameFull;  
  
                return k_UpdateSampleNameFull + k_InvokePostFix;
            default:
                throw new NotImplementedException();
        }
    }  
  
    const string k_UpdateSampleNameFull = "Assembly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.Assembly.html)-CSharp.dll!::MyScript.Update()";
    // Invoked method samples or samples instrumented via Deep Profiling will by default be shown
    // without their fully qualifying type name as above
    // Instead the Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) UI will strip out everything before the '!::' part of their name.
    // SetSelection will still find these samples, if the UI is set to not Show Full Scripting Method Names
    // Note that RawFrameDataView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.html) and HierarchyFrameDataView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.html) will not be able to identify the Marker IDs
    // for such samples from this shorter name.
    const string k_UpdateSampleNameShort = "MyScript.Update()";  
  
    static readonly List<string> k_SampleNames = new List<string>
    {
        "PlayerLoop[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoop.html)",
        "Update.ScriptRunBehaviourUpdate",
        "BehaviourUpdate",
    };  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/Analysis/Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) Extension")]
    public static void ShowExampleWindow()
    {
        var window = GetWindow<Example>();
        window.m_Profiler = EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)<ProfilerWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow.html)>();
    }  
  
    void OnGUI()
    {
        // First make sure there is an open Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) Window
        if (m_Profiler == null)
            m_Profiler = EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)<ProfilerWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow.html)>();  
  
        // For demonstration purposes, let the user choose if the names or if Marker IDs should be used.
        m_UseMarkerNames = GUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Toggle.html)(m_UseMarkerNames, "Use Marker names instead of IDs");
        if (!m_UseMarkerNames)
            m_UpdateNameMatchType = UpdateNameMatchType.Full;  
  
        // Marker IDs need to be gotten from the fully qualified type name, so the shorter name is not an option when using IDs
        using (new EditorGUI.DisabledScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DisabledScope.html)(!m_UseMarkerNames))
        {
            // For demonstration purposes, let the user choose if the short or the long name should be used.
            m_UpdateNameMatchType = (UpdateNameMatchType)EditorGUILayout.EnumPopup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EnumPopup.html)(m_UpdateNameMatchType);
        }  
  
        // If the currently selected Module is not the CPU Usage module, setting the selection will not be visible to the user immediately
        if (m_Profiler.selectedModuleIdentifier == ProfilerWindow.cpuModuleIdentifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-cpuModuleIdentifier.html))
        {
            // Get the CPU Usage Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) module's selection controller interface to interact with the selection
            var cpuSampleSelectionController = m_Profiler.GetFrameTimeViewSampleSelectionController(ProfilerWindow.cpuModuleIdentifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-cpuModuleIdentifier.html));
            // If the current selection object is null, there is no selection to print out.
            using (new EditorGUI.DisabledScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DisabledScope.html)(m_Profiler.lastAvailableFrameIndex < 0))
            {
                if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Check my Script for GC.Alloc"))
                {
                    string samplePath = "";
                    for (int i = 0; i < k_SampleNames.Count; i++)
                    {
                        samplePath += $"{k_SampleNames[i]}/";
                    }  
  
                    var samplePathDeepProfiling = samplePath + $"{GetUpdateSampleName(m_UpdateNameMatchType, true)}/";
                    samplePath = samplePath + $"{GetUpdateSampleName(m_UpdateNameMatchType, false)}/";
                    // the sample we are looking for, without a trailing '/'
                    samplePath += k_GCAllocSampleName;
                    samplePathDeepProfiling += k_GCAllocSampleName;  
  
                    // This check will fail in Deep Profiling because "MethodWithABoxingAllocation()" will be instrumented
                    // and sitting in the sample stack between "Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()" and the "GC.Alloc".
                    if (cpuSampleSelectionController.SetSelection(samplePath) || cpuSampleSelectionController.SetSelection(samplePathDeepProfiling))
                    {
                        Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)("MyScript allocates in its Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) loop");
                    }
                    else
                    {
                        if (m_UseMarkerNames)
                        {
                            samplePath = "";
                            for (int i = 0; i < k_SampleNames.Count; i++)
                            {
                                samplePath += $"{k_SampleNames[i]}{ (i < k_SampleNames.Count - 1 ?"/": "")}";
                            }
                            // SetSelection calls that take sample names as strings will find shortened scripting sample names
                            var mySctiprSamplePathDeepProfiling = $"{samplePath}/{GetUpdateSampleName(m_UpdateNameMatchType, true)}";
                            var myScriptSamplePath = $"{samplePath}/{GetUpdateSampleName(m_UpdateNameMatchType, false)}";  
  
                            if (cpuSampleSelectionController.SetSelection(m_Profiler.selectedFrameIndex,
                                k_MainThreadGroupName, k_MainThreadName, k_GCAllocSampleName, myScriptSamplePath) ||
                                cpuSampleSelectionController.SetSelection(m_Profiler.selectedFrameIndex,
                                    k_MainThreadGroupName, k_MainThreadName, k_GCAllocSampleName, mySctiprSamplePathDeepProfiling))
                            {
                                Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)("MyScript allocates in its Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) loop");
                            }
                            // MyScript did not have a GC.Alloc sample underneath it, but maybe a different Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) sample allocated
                            // Search through all Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() samples
                            else if (cpuSampleSelectionController.SetSelection(m_Profiler.selectedFrameIndex,
                                k_MainThreadGroupName, k_MainThreadName, k_GCAllocSampleName, samplePath))
                            {
                                Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)($"MyScript does not allocate but {cpuSampleSelectionController.selection.markerNamePath[k_SampleNames.Count]} allocates in its Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) loop");
                            }
                            else
                            {
                                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("No Script is allocating in its Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) Loop");
                                FindAnyGCAllocSample(cpuSampleSelectionController);
                            }
                        }
                        else
                        {
                            List<int> markerIdPath = new List<int>(k_SampleNames.Count + 1);
                            List<int> deepProfilingmarkerIdPath = new List<int>(k_SampleNames.Count + 1);
                            int gcAllocMarkerId = FrameDataView.invalidMarkerId[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView-invalidMarkerId.html);
                            using (var frameData = ProfilerDriver.GetRawFrameDataView((int)m_Profiler.selectedFrameIndex, 0))
                            {
                                for (int i = 0; i < k_SampleNames.Count; i++)
                                {
                                    markerIdPath.Add(frameData.GetMarkerId(k_SampleNames[i]));
                                }
                                deepProfilingmarkerIdPath.AddRange(markerIdPath);
                                // GetMarkerId needs the full length marker name to be able to identify this sample.
                                markerIdPath.Add(frameData.GetMarkerId(GetUpdateSampleName(UpdateNameMatchType.Full, false)));
                                deepProfilingmarkerIdPath.Add(frameData.GetMarkerId(GetUpdateSampleName(UpdateNameMatchType.Full, true)));  
  
                                gcAllocMarkerId = frameData.GetMarkerId(k_GCAllocSampleName);
                            }  
  
                            if (cpuSampleSelectionController.SetSelection(m_Profiler.selectedFrameIndex,
                                k_MainThreadGroupName, k_MainThreadName, gcAllocMarkerId, markerIdPath) ||
                                cpuSampleSelectionController.SetSelection(m_Profiler.selectedFrameIndex,
                                    k_MainThreadGroupName, k_MainThreadName, gcAllocMarkerId, deepProfilingmarkerIdPath))
                            {
                                Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)("MyScript allocates in its Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) loop");
                            }
                            else
                            {
                                // MyScript did not have a GC.Alloc sample underneath it, but maybe a different Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) sample allocated
                                // Remove the MyScript sample id from the path and search through all Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() samples
                                markerIdPath.Remove(markerIdPath.Count - 1);
                                if (cpuSampleSelectionController.SetSelection(m_Profiler.selectedFrameIndex,
                                    k_MainThreadGroupName, k_MainThreadName,
                                    gcAllocMarkerId, markerIdPath))
                                {
                                    Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)($"MyScript does not allocate but {cpuSampleSelectionController.selection.markerNamePath[k_SampleNames.Count]} allocates in its Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) loop");
                                    return;
                                }
                                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("No Script is allocating in its Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) Loop");
                                FindAnyGCAllocSample(cpuSampleSelectionController);
                            }
                        }
                    }
                }
            }
        }
    }  
  
    void FindAnyGCAllocSample(IProfilerFrameTimeViewSampleSelectionController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.IProfilerFrameTimeViewSampleSelectionController.html) cpuSampleSelectionController)
    {
        using (var frameData = ProfilerDriver.GetRawFrameDataView((int)m_Profiler.selectedFrameIndex, 0))
        {
            var gcAllocMarkerId = frameData.GetMarkerId(k_GCAllocSampleName);
            for (int i = 0; i < frameData.sampleCount; i++)
            {
                if (frameData.GetSampleMarkerId(i) == gcAllocMarkerId)
                {
                    var selection = new ProfilerTimeSampleSelection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerTimeSampleSelection.html)(m_Profiler.selectedFrameIndex, k_MainThreadGroupName,
                        k_MainThreadName, frameData.threadId, i);
                    if (cpuSampleSelectionController.SetSelection(selection))
                    {
                        // do not use the selection object here. The CPU Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) Module created a new one.
                        // Instead Get the selection object from the Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html)
                        Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)($"MyScript does not allocate but {cpuSampleSelectionController.selection.markerNamePath[k_SampleNames.Count]} allocates in its Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) loop");
                        return;
                    }
                }
            }
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("No Script is allocating anything");
        }
    }
}

```

This example shows all major variations of SetSelection and showcases their differences.
* * *
