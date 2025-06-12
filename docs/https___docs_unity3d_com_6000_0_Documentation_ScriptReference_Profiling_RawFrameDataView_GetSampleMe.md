* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.GetSampleMetadataAsString.html

#  [RawFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.html).GetSampleMetadataAsString
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
public string GetSampleMetadataAsString(int sampleIndex, int metadataIndex); 
### Parameters
Parameter | Description  
---|---  
sampleIndex | Index of the Profiler sample.  
metadataIndex | Metadata index.  
### Returns
**string** Returns string representation of sample metadata value. 
### Description
Gets sample metadata value as string.
Use to obtain additional data associated with the sample. _metadataIndex_ must be between 0 and [GetSampleMetadataCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.GetSampleMetadataCount.html).
* * *
