* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.SmoothEdges.html

#  [Cubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html).SmoothEdges
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
public void SmoothEdges(int smoothRegionWidthInPixels = 1); 
### Parameters
Parameter | Description  
---|---  
smoothRegionWidthInPixels | Pixel distance at edges over which to apply smoothing.  
### Description
Performs smoothing of near edge regions.
Helps to compensate lack of linear interpolation across the edges of cubemap in GPU.  
  
Usually you will want to call this method for the cubemap which is going to be used for glossy reflections.
* * *
