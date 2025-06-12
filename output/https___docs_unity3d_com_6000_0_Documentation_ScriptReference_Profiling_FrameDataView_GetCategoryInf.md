* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetCategoryInfo.html

#  [FrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html).GetCategoryInfo
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
public [Profiling.ProfilerCategoryInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerCategoryInfo.html) GetCategoryInfo(ushort id); 
### Parameters
Parameter | Description  
---|---  
id | The ID for the Category.  
### Returns
**ProfilerCategoryInfo** Returns a ProfilerCategoryInfo struct based on the supplied ID. If the ID doesn't exist, an exception is thrown. 
### Description
Gets the Profiler category information for a given category ID.
* * *
