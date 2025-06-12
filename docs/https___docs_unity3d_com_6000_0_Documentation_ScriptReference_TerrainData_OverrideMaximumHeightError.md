* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.OverrideMaximumHeightError.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).OverrideMaximumHeightError
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
public void OverrideMaximumHeightError(float[] maxError); 
### Parameters
Parameter | Description  
---|---  
maxError | Provided maximum height error values.  
### Description
Override the maximum tessellation height error with user provided values. Note that the overriden values get reset when the terrain resolution is changed and stays unchanged when the terrain heightmap is painted or changed via script.
* * *
