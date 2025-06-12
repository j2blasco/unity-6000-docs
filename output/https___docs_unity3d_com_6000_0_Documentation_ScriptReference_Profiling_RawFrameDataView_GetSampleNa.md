* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.GetSampleName.html

#  [RawFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.html).GetSampleName
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
public string GetSampleName(int sampleIndex); 
### Parameters
Parameter | Description  
---|---  
sampleIndex | Index of the Profiler sample.  
### Returns
**string** Returns sample name. Returns _null_ if sample index is invalid. 
### Description
Gets the name of the specific sample.
**Note:** _GetSampleName_ allocates string when called. Use [GetSampleMarkerId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.GetSampleMarkerId.html) to avaoid allocations for simple lookups.
* * *
