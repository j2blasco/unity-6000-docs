* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetDetailResolution.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).SetDetailResolution
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
public void SetDetailResolution(int detailResolution, int resolutionPerPatch); 
### Parameters
Parameter | Description  
---|---  
detailResolution | Specifies the number of pixels in the detail resolution map. A larger detailResolution, leads to more accurate detail object painting.  
resolutionPerPatch | Specifies the size in pixels of each individually rendered detail patch. A larger number reduces draw calls, but might increase triangle count since detail patches are culled on a per batch basis. A recommended value is 16. If you use a very large detail object distance and your grass is very sparse, it makes sense to increase the value.  
### Description
Sets the resolution of the detail map.
* * *
