* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetSessionMetaDataCount.html

#  [FrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html).GetSessionMetaDataCount
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
public int GetSessionMetaDataCount(Guid id, int tag); 
### Parameters
Parameter | Description  
---|---  
id | Unique identifier associated with the data.  
tag | Data stream index.  
### Returns
**int** Returns count of metadata chunks. 
### Description
Gets the total number of metadata chunks for each _id_ and _tag_ pair in the Profiler session.
Use the _GetSessionMetaDataCount_ method to retrieve the total number of metadata arrays available in the session this frame occurred in. Profiler data can contain frames from different sessions.  
  
When there are multiple [Profiler.EmitSessionMetaData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EmitSessionMetaData.html) calls in the same frame, it results in multiple metadata arrays that are associated with the frame for a given _id_ , _tag_ pair. This information can be used to write data to the stream in small portions, which reduces the amount of memory needed to hold generated data.  
  
Use _id_ to identify the metadata from your project or package.  
Use _tag_ to distinguish between different data streams.  
  
Additional resources: [GetSessionMetaData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetSessionMetaData.html), [Profiler.EmitSessionMetaData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EmitSessionMetaData.html).
* * *
