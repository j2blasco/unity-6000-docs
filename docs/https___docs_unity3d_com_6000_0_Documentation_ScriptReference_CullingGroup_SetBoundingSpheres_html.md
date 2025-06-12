* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.SetBoundingSpheres.html

#  [CullingGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.html).SetBoundingSpheres
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
public void SetBoundingSpheres(BoundingSphere[] array); 
### Parameters
Parameter | Description  
---|---  
array | The [BoundingSphere](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundingSphere.html)s to cull.  
### Description
Sets the array of bounding sphere definitions that the CullingGroup should compute culling for.
Note that the provided array is simply referenced, not copied; therefore you can simply modify the data in the array on successive frames without calling SetBoundingSpheres again each time.
* * *
