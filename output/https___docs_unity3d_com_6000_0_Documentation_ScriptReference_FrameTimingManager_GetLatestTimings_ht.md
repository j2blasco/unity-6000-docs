* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTimingManager.GetLatestTimings.html

#  [FrameTimingManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTimingManager.html).GetLatestTimings
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
public static uint GetLatestTimings(uint numFrames, FrameTiming[] timings); 
### Parameters
Parameter | Description  
---|---  
numFrames | User supplies a desired number of frames they would like FrameTimings for. This should be equal to or less than the maximum FrameTimings the platform can capture.  
timings | An array of FrameTiming structs that is passed in by the user and will be filled with data as requested. It is the users job to make sure the array that is passed is large enough to hold the requested number of FrameTimings.  
### Returns
**uint** Returns the number of FrameTimings it actually was able to get. This will always be equal to or less than the requested numFrames depending on availability of captured FrameTimings. 
### Description
Allows the user to access the currently captured FrameTimings.
Fills in a user supplied array with the requested number of FrameTimings, assuming there are enough available from the last call to CaptureFrameTimings. The array is filled in from the start with most recent completed frames FrameTimings and works backwards. So element 0 of the returned array will contain the data for the last fully finished frame. Depending on platform, the maximum frames that will ever be captured will vary and it can never return more than its maximum.
* * *
