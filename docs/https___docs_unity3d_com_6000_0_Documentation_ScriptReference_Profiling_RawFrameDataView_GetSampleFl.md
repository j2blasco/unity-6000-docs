* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.GetSampleFlowEvents.html

#  [RawFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.html).GetSampleFlowEvents
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
public void GetSampleFlowEvents(int sampleIndex, List<FlowEvent> outFlowEvents); 
### Parameters
Parameter | Description  
---|---  
sampleIndex | Index of the Profiler sample.  
outFlowEvents | Returns the list of profiler flow events for the sample in the current frame and thread.  
### Description
Gets the flow events that originate from the specific sample.
* * *
